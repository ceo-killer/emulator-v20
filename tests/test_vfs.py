"""Tests for the stage 1 VFS name placeholder."""
import unittest

from src.vfs import VFS


class VfsTests(unittest.TestCase):
    """Test VFS name handling."""

    def test_name_from_posix_path(self):
        vfs = VFS("scripts/demo-vfs.json")
        self.assertEqual(vfs.vfs_name, "demo-vfs.json")

    def test_name_from_windows_path(self):
        vfs = VFS(r"scripts\demo-vfs.json")
        self.assertEqual(vfs.vfs_name, "demo-vfs.json")

    def test_name_without_directory(self):
        vfs = VFS("demo-vfs.json")
        self.assertEqual(vfs.vfs_name, "demo-vfs.json")


if __name__ == "__main__":
    unittest.main()
