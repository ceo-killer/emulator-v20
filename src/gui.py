"""Tkinter GUI for the REPL prototype."""
import tkinter as tk
from tkinter import scrolledtext
from typing import List, Tuple

from src.commands import cmd_cd, cmd_exit, cmd_ls
from src.parser import parse_input
from src.vfs import VFS


COMMANDS = {
    "ls": cmd_ls,
    "cd": cmd_cd,
    "exit": cmd_exit,
}


class ShellGUI:
    """Display a minimal interactive shell window."""

    def __init__(self, vfs: VFS) -> None:
        """Create the GUI window."""
        self.vfs = vfs
        self.root = tk.Tk()
        self.root.title(f"Emulator - {vfs.vfs_name}")
        self.root.geometry("760x500")
        self._build_widgets()

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
            self._process(user_input)

    def _process(self, user_input: str) -> None:
        """Parse and execute one REPL command."""
        try:
            command, args = parse_input(user_input)
        except ValueError as exc:
            self._print(f"Ошибка: {exc}")
            return
        handler = COMMANDS.get(command)
        if handler is None:
            self._print(f"Ошибка: неизвестная команда: {command}")
            return
        if command == "exit":
            if args:
                self._print("Ошибка: exit не принимает аргументы")
                return
            handler(args)
            self.root.destroy()
            return
        self._print(handler(args))

    def run(self) -> None:
        """Start the GUI loop."""
        self.root.mainloop()
