"""Stage 2 application entry point."""
import argparse
from typing import Sequence

from src.logger import Logger
from src.vfs import VFS


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Эмулятор UNIX-подобной оболочки."
    )
    parser.add_argument("vfs_path", help="Путь к VFS.")
    parser.add_argument("log_path", help="Путь к CSV-логу.")
    parser.add_argument(
        "script_path",
        help="Путь к стартовому скрипту.",
    )
    return parser


def print_configuration(
    vfs_path: str,
    log_path: str,
    script_path: str,
) -> None:
    """Print all configured parameters."""
    print("Параметры запуска:")
    print(f"  VFS: {vfs_path}")
    print(f"  Лог: {log_path}")
    print(f"  Скрипт: {script_path}")


def main(argv: Sequence[str] | None = None) -> int:
    """Start the configured GUI application."""
    args = build_parser().parse_args(argv)
    print_configuration(
        args.vfs_path,
        args.log_path,
        args.script_path,
    )
    vfs = VFS(args.vfs_path)
    logger = Logger(args.log_path)

    from src.gui import ShellGUI

    ShellGUI(
        vfs,
        logger,
        args.script_path,
    ).run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
