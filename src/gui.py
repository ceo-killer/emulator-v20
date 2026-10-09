"""Tkinter GUI with CSV logging and startup scripts."""
import tkinter as tk
from tkinter import scrolledtext
from typing import Optional

from src.commands import execute_command
from src.logger import Logger
from src.parser import parse_input
from src.vfs import VFS


class ShellGUI:
    """Display and control the stage 2 shell."""

    def __init__(
        self,
        vfs: VFS,
        logger: Logger,
        script_path: Optional[str],
    ) -> None:
        """Create the GUI and configure logging."""
        self.vfs = vfs
        self.logger = logger
        self.script_path = script_path
        self.root = tk.Tk()
        self.root.title(f"Emulator - {vfs.vfs_name}")
        self.root.geometry("760x500")
        self._build_widgets()
        if script_path:
            self.root.after(100, self._run_script)

    def _build_widgets(self) -> None:
        """Create output and input widgets."""
        self.output = scrolledtext.ScrolledText(
            self.root,
            state=tk.DISABLED,
            wrap=tk.WORD,
        )
        self.output.pack(expand=True, fill=tk.BOTH, padx=8, pady=8)
        self.entry = tk.Entry(self.root)
        self.entry.pack(fill=tk.X, padx=8, pady=(0, 8))
        self.entry.bind("<Return>", self._on_enter)
        self.entry.focus_set()

    def _print(self, text: str) -> None:
        """Append a line to the output."""
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)
        self.output.config(state=tk.DISABLED)

    def _on_enter(self, event: tk.Event) -> None:
        """Process a line entered by the user."""
        user_input = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        if user_input:
            self._print(f"$ {user_input}")
            self._process_command(user_input)

    def _process_command(self, user_input: str) -> tuple[bool, bool]:
        """Parse, execute and log one command."""
        try:
            command, args = parse_input(user_input)
        except ValueError as exc:
            error = str(exc)
            self._print(f"Ошибка: {error}")
            self.logger.log(user_input, error)
            return False, False

        if not command:
            return True, False

        result = execute_command(command, args)
        if result.output:
            self._print(result.output)
        if result.error:
            self._print(f"Ошибка: {result.error}")
        self.logger.log(user_input, result.error)

        if result.should_exit:
            self.root.after_idle(self.root.destroy)
            return True, True
        return result.success, False

    def _run_script(self) -> None:
        """Run the startup script and stop on its first error."""
        if not self.script_path:
            return

        try:
            with open(
                self.script_path,
                "r",
                encoding="utf-8",
            ) as source:
                for raw_line in source:
                    line = raw_line.strip()
                    if not line or line.startswith("#"):
                        continue
                    self._print(f"$ {line}")
                    success, should_exit = self._process_command(line)
                    if should_exit:
                        break
                    if not success:
                        self._print("Скрипт остановлен после ошибки.")
                        break
        except OSError as exc:
            message = f"Ошибка запуска стартового скрипта: {exc}"
            self._print(message)
            self.logger.log("<startup>", message)

    def run(self) -> None:
        """Start the GUI loop."""
        self.root.mainloop()
