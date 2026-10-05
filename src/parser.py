"""Input parsing helpers."""
import os
import shlex
from typing import List, Tuple


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Expand environment variables and split command input."""
    expanded = os.path.expandvars(user_input)
    if not expanded.strip():
        return "", []
    try:
        parts = shlex.split(expanded)
    except ValueError as exc:
        raise ValueError(f"Некорректные кавычки: {exc}") from exc
    return parts[0], parts[1:]
