"""REPL prototype command stubs."""
from typing import List


def _stub(name: str, args: List[str]) -> str:
    """Return a textual representation of a stub command."""
    suffix = " ".join(args)
    return name if not suffix else f"{name} {suffix}"


def cmd_ls(args: List[str]) -> str:
    """Return the ls stub output."""
    return _stub("ls", args)


def cmd_cd(args: List[str]) -> str:
    """Return the cd stub output."""
    return _stub("cd", args)


def cmd_exit(args: List[str]) -> bool:
    """Signal that the application should exit."""
    return True
