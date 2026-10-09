"""Stage 1 shell command stubs."""
from dataclasses import dataclass


@dataclass(frozen=True)
class CommandResult:
    """Represent the outcome of a command."""

    success: bool
    output: str = ""
    error: str = ""
    should_exit: bool = False


def _format_stub(name: str, args: list[str]) -> str:
    """Format a command name and its arguments."""
    suffix = " ".join(args)
    return name if not suffix else f"{name} {suffix}"


def execute_command(command: str, args: list[str]) -> CommandResult:
    """Execute one supported stage 1 command."""
    if command == "ls":
        return CommandResult(True, output=_format_stub("ls", args))
    if command == "cd":
        return CommandResult(True, output=_format_stub("cd", args))
    if command == "exit":
        if args:
            return CommandResult(
                False,
                error="Использование: exit",
            )
        return CommandResult(
            True,
            output="Выход.",
            should_exit=True,
        )
    return CommandResult(
        False,
        error=f"Неизвестная команда: {command}",
    )
