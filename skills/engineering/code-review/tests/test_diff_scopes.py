"""Offline Git fixtures for the comparison modes documented in ../SKILL.md.

Run with: python3 -m unittest discover -s skills/engineering/code-review/tests -v
"""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class DiffScopes(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1",
                        GIT_CONFIG_GLOBAL=os.devnull)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "commit.gpgsign", "false")

    def git(self, *args):
        return subprocess.check_output(
            ["git", *args], cwd=self.root, env=self.env
        )

    def write(self, name, content="fixture\n"):
        (self.root / name).write_text(content)

    def commit(self, name):
        self.git("add", "--all")
        self.git("commit", "-qm", name)
        return self.git("rev-parse", "HEAD").decode().strip()

    def names(self, *args):
        return set(self.git("diff", "--name-only", "-z", *args).split(b"\0")) - {b""}

    def seed(self):
        for name in ("staged", "unstaged", "cancelled", "deleted"):
            self.write(name, "original\n")
        return self.commit("base")

    def test_wip_index_worktree_and_untracked_are_distinct(self):
        self.seed()
        self.write("staged", "index\n")
        self.write("cancelled", "index\n")
        self.git("add", "staged", "cancelled")
        self.write("cancelled", "original\n")
        self.write("unstaged", "working tree\n")
        (self.root / "deleted").unlink()
        self.write("new file\nwith newline", "untracked addition\n")
        self.write(".gitignore", "ignored\n")
        self.write("ignored", "not review input\n")
        before = self.git("status", "--porcelain=v1", "-z")

        self.assertEqual(self.names("--cached", "--"), {b"staged", b"cancelled"})
        self.assertEqual(self.names("--"), {b"unstaged", b"cancelled", b"deleted"})
        self.assertEqual(self.names("HEAD", "--"), {b"staged", b"unstaged", b"deleted"})
        # The net view hides a staged change undone in the working tree.
        self.assertIn(b"+index", self.git("diff", "--cached", "--", "cancelled"))
        self.assertIn(b"-index", self.git("diff", "--", "cancelled"))
        additions = set(self.git("ls-files", "--others", "--exclude-standard", "-z").split(b"\0")) - {b""}
        self.assertEqual(additions, {b"new file\nwith newline", b".gitignore"})
        self.assertEqual((self.root / os.fsdecode(b"new file\nwith newline")).read_text(), "untracked addition\n")
        self.assertEqual(self.names("HEAD", "--", "unstaged"), {b"unstaged"})
        self.assertEqual(before, self.git("status", "--porcelain=v1", "-z"))

    def test_exact_endpoint_branch_target_and_branch_plus_wip(self):
        base = self.seed()
        self.git("checkout", "-qb", "feature")
        self.write("feature-only", "feature content\n")
        target = self.commit("feature")
        self.git("checkout", "-q", "main")
        self.write("main-only", "main content\n")
        main = self.commit("main diverged")
        # The named target is not checked out. Three-dot excludes base-only work.
        self.assertEqual(self.names("main...feature", "--"), {b"feature-only"})
        self.assertEqual(self.names("main", "feature", "--"), {b"feature-only", b"main-only"})
        self.assertEqual(self.names(target, "HEAD", "--"), {b"feature-only", b"main-only"})
        self.assertEqual(self.git("rev-parse", "--verify", "feature^{commit}").decode().strip(), target)
        self.git("checkout", "-q", "feature")
        self.write("staged", "index\n")
        self.git("add", "staged")
        self.write("unstaged", "worktree\n")
        merge_base = self.git("merge-base", "main", "HEAD").decode().strip()
        self.assertEqual(merge_base, base)
        self.assertEqual(self.names(merge_base, "--"), {b"feature-only", b"staged", b"unstaged"})
        self.assertNotIn(b"main-only", self.names(merge_base, "--"))
        self.assertIn(main.encode(), self.git("log", f"{target}..main", "--format=%H"))

    def test_one_commit_root_commit_and_merge_parent(self):
        root = self.seed()
        root_patch = self.git("show", "--format=fuller", "--patch", root, "--")
        self.assertIn(b"+original", root_patch)
        self.git("checkout", "-qb", "feature")
        self.write("feature-only", "feature line\n")
        target = self.commit("feature")
        self.git("checkout", "-q", "main")
        self.write("main-only", "main line\n")
        self.commit("main")
        patch = self.git("show", "--format=fuller", "--patch", target, "--")
        self.assertIn(b"+feature line", patch)
        self.assertNotIn(b"main line", patch)
        self.git("merge", "--no-ff", "-qm", "merge fixture", "feature")
        self.assertEqual(self.names("HEAD^1", "HEAD", "--"), {b"feature-only"})
        self.assertEqual(self.names("HEAD^2", "HEAD", "--"), {b"main-only"})
        self.assertEqual(self.names("HEAD", "HEAD", "--"), set())

    def test_unborn_repo_needs_no_head(self):
        self.write("staged", "index\n")
        self.git("add", "staged")
        self.write("staged", "worktree\n")
        self.write("untracked")
        self.assertEqual(self.names("--cached", "--"), {b"staged"})
        self.assertEqual(self.names("--"), {b"staged"})
        self.assertEqual(self.git("ls-files", "--others", "--exclude-standard", "-z"), b"untracked\0")


if __name__ == "__main__":
    unittest.main()
