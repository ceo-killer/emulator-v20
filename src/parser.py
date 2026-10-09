"""Input parsing helpers."""
import os
import shlex


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Split input into tokens and expand environment variables."""
    if not user_input.strip():
        return "", []
    try:
        parts = shlex.split(user_input)
    except ValueError as exc:
        raise ValueError(f"Некорректные кавычки: {exc}") from exc
    parts = [os.path.expandvars(part) for part in parts]
    return parts[0], parts[1:]
