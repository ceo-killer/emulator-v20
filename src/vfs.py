"""Minimal VFS placeholder for the REPL prototype."""


class VFS:
    """Store only the VFS name during stage 1."""

    def __init__(self, vfs_name: str) -> None:
        """Initialize the prototype VFS."""
        self.vfs_name = vfs_name
