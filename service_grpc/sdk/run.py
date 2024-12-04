from subprocess import Popen
from typing import List, Optional, Callable


class Run:
    """SDK Runtime"""
    def __init__(self, host, port) -> None:
        self.host: str = host if host else "localhost"
        self.port: int = port if port else 50051
        self.process: Optional[Popen] = None
        self.hooks: List[Callable[[], None]] = []

    @property
    def target(self):
        """Return the target string."""
        return f"{self.host}:{self.port}"
