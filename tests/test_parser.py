"""Parser tests for stage 1."""
import os
import unittest

from src.parser import parse_input


class ParserTests(unittest.TestCase):
    """Test parser behavior."""

    def test_simple_command(self):
        """Parse a simple command."""
        self.assertEqual(
            parse_input("ls -l"),
            ("ls", ["-l"]),
        )

    def test_environment_expansion(self):
        """Expand an environment variable."""
        os.environ["V20_HOME"] = "/home/test"
        self.assertEqual(
            parse_input("cd $V20_HOME"),
            ("cd", ["/home/test"]),
        )


if __name__ == "__main__":
    unittest.main()
