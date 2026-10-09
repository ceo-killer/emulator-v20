"""Tests for stage 1 command stubs."""
import unittest

from src.commands import execute_command


class CommandTests(unittest.TestCase):
    """Test command stubs and argument validation."""

    def test_ls_stub_without_arguments(self):
        result = execute_command("ls", [])
        self.assertTrue(result.success)
        self.assertEqual(result.output, "ls")

    def test_ls_stub_with_arguments(self):
        result = execute_command("ls", ["-l", "/home/student"])
        self.assertTrue(result.success)
        self.assertEqual(result.output, "ls -l /home/student")

    def test_cd_stub_with_arguments(self):
        result = execute_command("cd", ["/home/student"])
        self.assertTrue(result.success)
        self.assertEqual(result.output, "cd /home/student")

    def test_exit_without_arguments(self):
        result = execute_command("exit", [])
        self.assertTrue(result.success)
        self.assertTrue(result.should_exit)

    def test_exit_rejects_arguments(self):
        result = execute_command("exit", ["now"])
        self.assertFalse(result.success)
        self.assertEqual(result.error, "Использование: exit")

    def test_unknown_command_is_rejected(self):
        result = execute_command("unknown_command", [])
        self.assertFalse(result.success)
        self.assertIn("Неизвестная команда", result.error)


if __name__ == "__main__":
    unittest.main()
