"""Logger provider for quiz-tracker."""


class Logger:
    """Simple logging provider with info/debug/error methods."""

    def info(self, msg: str) -> None:
        """Log an info message."""
        print(f"[INFO] {msg}")

    def debug(self, msg: str) -> None:
        """Log a debug message."""
        print(f"[DEBUG] {msg}")

    def error(self, msg: str) -> None:
        """Log an error message."""
        print(f"[ERROR] {msg}")
