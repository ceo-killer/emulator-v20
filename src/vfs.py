"""VFS name placeholder for stages 1 and 2."""
from pathlib import PurePosixPath


class VFS:
    """Store the VFS name for the application window."""

    def __init__(self, vfs_path: str) -> None:
        """Initialize the VFS name without loading its contents."""
        normalised_path = vfs_path.replace("\\", "/")
        self.vfs_name = PurePosixPath(normalised_path).name or vfs_path
