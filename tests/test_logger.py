"""Logger tests."""
import csv
import tempfile
import unittest
from pathlib import Path

from src.logger import CSV_HEADER, Logger


class LoggerTests(unittest.TestCase):
    """Test CSV logging."""

    def test_user_command_and_error(self):
        """Store username, command and error."""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "log.csv"
            logger = Logger(str(path))
            logger.log("cd /missing", "Путь не найден")
            with path.open(
                "r", newline="", encoding="utf-8"
            ) as source:
                rows = list(csv.reader(source))
        self.assertEqual(rows[0], CSV_HEADER)
        self.assertEqual(rows[1][1], logger.username)
        self.assertEqual(rows[1][2], "cd /missing")
        self.assertEqual(rows[1][3], "Путь не найден")
