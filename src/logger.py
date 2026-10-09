"""CSV command logger."""
import csv
import getpass
from datetime import datetime
from pathlib import Path
from typing import Optional


CSV_HEADER = ["timestamp", "username", "command", "error"]


class Logger:
    """Write shell command events to CSV."""

    def __init__(self, log_path: str) -> None:
        """Initialize the logger."""
        self.log_path = Path(log_path)
        self.username = getpass.getuser()
        self._init_csv()

    def _init_csv(self) -> None:
        """Create the CSV header when needed."""
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        if self.log_path.exists() and self.log_path.stat().st_size:
            return
        with self.log_path.open(
            "w", newline="", encoding="utf-8"
        ) as target:
            csv.writer(target).writerow(CSV_HEADER)

    def log(self, command: str, error: Optional[str] = None) -> None:
        """Append one command event."""
        with self.log_path.open(
            "a", newline="", encoding="utf-8"
        ) as target:
            csv.writer(target).writerow(
                [
                    datetime.now().astimezone().isoformat(
                        timespec="seconds"
                    ),
                    self.username,
                    command,
                    error or "",
                ]
            )
