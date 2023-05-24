"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

import json
from typing import Dict


class Language:
    def __init__(self, settings: Dict) -> None:
        self._settings: Dict = settings
        self._language_app: Dict = {}

        self._default: Dict = {
            "btn_app_logo": "Image Example",
            "btn_app_news": "News",
            "btn_app_wallet": "Wallet",
            "btn_app_settings": "Settings",
            "btn_news_one": "Button News",
            "btn_wallet_one": "Button Wallet",
            "btn_settings_save": "Button Save",
            "mode_settings_theme_one": "Light",
            "mode_settings_theme_two": "Dark",
            "mode_settings_lang_one": "English",
            "mode_settings_lang_two": "Ukrainian"
        }

        if self._settings.get('language') == 'EN':
            self._language_app = self._default
        elif self._settings.get('language') == 'UA':
            self._language_app = self._open_lang_json('ukrainian')
        else:
            self._language_app = self._default

    @property
    def language_app(self) -> Dict:
        return self._language_app

    def _open_lang_json(self, text: str) -> Dict:
        try:
            with open(f"{text}.json", "r") as j:
                lang_temp: Dict = json.load(j)
            return lang_temp
        except FileNotFoundError:
            return self._default
