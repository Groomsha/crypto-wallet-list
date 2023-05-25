import os
from pathlib import Path
from typing import List


class PathDir:
    def __init__(self) -> None:
        self._path_app: List = []
        self._cwd_app = Path.cwd()

    @property
    def path_app(self) -> List:
        return self._path_app
