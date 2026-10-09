"""Tests for command parsing."""
import os
import unittest
from unittest.mock import patch

from src.parser import parse_input


class ParserTests(unittest.TestCase):
    """Test input splitting and environment expansion."""

    def test_simple_command(self):
        self.assertEqual(parse_input("ls -l"), ("ls", ["-l"]))

    def test_environment_expansion(self):
        with patch.dict(os.environ, {"V20_HOME": "/home/test"}):
            self.assertEqual(
                parse_input("cd $V20_HOME"),
                ("cd", ["/home/test"]),
            )

    def test_windows_path_expansion_preserves_backslashes(self):
        windows_path = r"C:\Users\student"
        with patch.dict(os.environ, {"V20_HOME": windows_path}):
            self.assertEqual(
                parse_input("cd $V20_HOME"),
                ("cd", [windows_path]),
            )

    def test_quoted_argument(self):
        self.assertEqual(
            parse_input('ls "folder with spaces"'),
            ("ls", ["folder with spaces"]),
        )

    def test_empty_input(self):
        self.assertEqual(parse_input("   "), ("", []))

    def test_unclosed_quote_raises_error(self):
        with self.assertRaises(ValueError):
            parse_input('ls "unfinished')


if __name__ == "__main__":
    unittest.main()
