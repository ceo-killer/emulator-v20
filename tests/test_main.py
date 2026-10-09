"""Tests for command-line configuration."""
import contextlib
import io
import unittest

from main import build_parser


class MainTests(unittest.TestCase):
    """Test the three required command-line parameters."""

    def test_all_parameters_are_parsed(self):
        args = build_parser().parse_args(
            [
                "scripts/demo-vfs.json",
                "log.csv",
                "scripts/start.txt",
            ]
        )
        self.assertEqual(args.vfs_path, "scripts/demo-vfs.json")
        self.assertEqual(args.log_path, "log.csv")
        self.assertEqual(args.script_path, "scripts/start.txt")

    def test_parameters_are_required(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                build_parser().parse_args([])


if __name__ == "__main__":
    unittest.main()
