"""Tests for stage 2 startup script handling."""
import csv
import tempfile
import unittest
from pathlib import Path

from src.gui import ShellGUI
from src.logger import Logger


class FakeOutput:
    """Minimal text widget substitute for GUI tests."""

    def __init__(self):
        self.lines = []

    def config(self, **kwargs):
        pass

    def insert(self, _index, text):
        self.lines.append(text.rstrip("\n"))

    def see(self, _index):
        pass


class FakeRoot:
    """Minimal Tk root substitute for GUI tests."""

    def __init__(self):
        self.callbacks = []

    def after_idle(self, callback):
        self.callbacks.append(callback)

    def destroy(self):
        pass


class GuiScriptTests(unittest.TestCase):
    """Test startup scripts without opening a real window."""

    def _make_gui(self, script_path, log_path):
        gui = ShellGUI.__new__(ShellGUI)
        gui.output = FakeOutput()
        gui.root = FakeRoot()
        gui.logger = Logger(str(log_path))
        gui.script_path = str(script_path)
        return gui

    def test_script_stops_at_first_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            script_path = folder / "start.txt"
            log_path = folder / "log.csv"
            script_path.write_text(
                "ls demo\nunknown_command\ncd /tmp\n",
                encoding="utf-8",
            )
            gui = self._make_gui(script_path, log_path)

            gui._run_script()

            self.assertIn(
                "Скрипт остановлен после ошибки.",
                gui.output.lines,
            )
            self.assertNotIn("$ cd /tmp", gui.output.lines)
            with log_path.open(
                "r", newline="", encoding="utf-8"
            ) as source:
                rows = list(csv.reader(source))
            self.assertEqual(
                [row[2] for row in rows[1:]],
                ["ls demo", "unknown_command"],
            )

    def test_exit_stops_script_without_error_message(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            script_path = folder / "start.txt"
            log_path = folder / "log.csv"
            script_path.write_text(
                "exit\nls ignored\n",
                encoding="utf-8",
            )
            gui = self._make_gui(script_path, log_path)

            gui._run_script()

            self.assertNotIn(
                "Скрипт остановлен после ошибки.",
                gui.output.lines,
            )
            self.assertNotIn("$ ls ignored", gui.output.lines)
            self.assertEqual(len(gui.root.callbacks), 1)

    def test_missing_script_is_reported_and_logged(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            script_path = folder / "missing.txt"
            log_path = folder / "log.csv"
            gui = self._make_gui(script_path, log_path)

            gui._run_script()

            self.assertTrue(
                any(
                    "Ошибка запуска стартового скрипта" in line
                    for line in gui.output.lines
                )
            )
            with log_path.open(
                "r", newline="", encoding="utf-8"
            ) as source:
                rows = list(csv.reader(source))
            self.assertEqual(rows[1][2], "<startup>")
            self.assertIn("missing.txt", rows[1][3])


if __name__ == "__main__":
    unittest.main()
