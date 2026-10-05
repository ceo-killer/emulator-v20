"""Stage 1 application entry point."""
import sys

from src.gui import ShellGUI
from src.vfs import VFS


def main() -> int:
    """Start the GUI REPL prototype."""
    vfs_name = sys.argv[1] if len(sys.argv) > 1 else "vfs.json"
    ShellGUI(VFS(vfs_name)).run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
