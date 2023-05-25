import json
from typing import Dict
from pathlib import Path

SETTINGS: str = f'{Path.cwd()}/settings.json'


class Settings:
    def __init__(self) -> None:
        self._current: Dict = {}
        self._default: Dict = {'language': 'EN',
                               'proxy': 'False',
                               'theme': 'System'}

        try:
            with open(SETTINGS, "r") as j:
                self._current = json.load(j)
        except FileNotFoundError:
            self._current = self._default
            self.save(None)

    @property
    def current(self) -> Dict:
        return self._current

    def save(self, new_settings: Dict):
        temp_new_settings: Dict = {}

        if new_settings == None:
            temp_new_settings = self._default
        elif new_settings != None:
            for key in self._default.keys():
                if key in new_settings.keys():
                    self._default[key] = new_settings[key]

        temp_new_settings = self._default

        with open(SETTINGS, "w") as j:
            json.dump(temp_new_settings, j)
