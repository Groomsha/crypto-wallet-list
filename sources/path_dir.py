import platform
from pathlib import Path
from typing import Dict


class PathDir:
    def __init__(self) -> None:
        self._literal: str = ''
        self._cwd_app = Path.cwd()

        if platform.system() == 'Linux':
            self._literal = '/'
        elif platform.system() == 'Windows':
            self._literal = '\\'

        self._path_app: Dict = {'SETTINGS': f'{self._cwd_app}{self._literal}settings.json',
                                'DIR_IMG': Path(Path.cwd(), 'gui_app', 'images'),
                                "DIR_LANG": Path(Path.cwd(), 'gui_app', 'language')}

    @property
    def path_app(self) -> Dict:
        return self._path_app
