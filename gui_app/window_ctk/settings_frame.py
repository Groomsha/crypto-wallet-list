"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

import os
from typing import Any, Dict

from PIL import Image
import customtkinter


class SettingsFrame:
    def __init__(self, ctk: customtkinter.CTkFrame, settings: Any, lang: Dict) -> None:
        self._settings: Any = settings
        self._window = ctk
        self._lang = lang

        self._new_settings: Dict = {}
        self._image_icon: customtkinter.CTkImage = None
        self._image_settings_frame()

        self._settings_frame = customtkinter.CTkFrame(self._window, corner_radius=0, fg_color="transparent")
        self._change_settings_mode_event(self._settings.settings_app.get('theme'))

        self._btn_settings_mode = None
        self._btn_settings_save = None
        self._btn_settings_lang = None
        self._btn_settings_frame()

    @property
    def settings_frame(self) -> customtkinter.CTkFrame:
        return self._settings_frame

    def _image_settings_frame(self) -> None:
        self._image_icon = customtkinter.CTkImage(Image.open(os.path.join(self._window.image_path, "image_icon_light.png")), size=(20, 20))

    def _btn_settings_frame(self) -> None:
        self._btn_settings_save = customtkinter.CTkButton(self._settings_frame, text=f"{self._lang.language_app.get('btn_settings_save')}", image=self._image_icon, compound='top', command=self._change_settings_save)
        self._btn_settings_save.grid(row=0, column=3, padx=20, pady=10)

        self._btn_settings_mode = customtkinter.CTkOptionMenu(self._settings_frame, values=[f"{self._lang.language_app.get('mode_settings_theme_one')}", f"{self._lang.language_app.get('mode_settings_theme_two')}"], command=self._change_settings_mode_event)
        self._btn_settings_mode.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self._btn_settings_lang = customtkinter.CTkOptionMenu(self._settings_frame, values=[f"{self._lang.language_app.get('mode_settings_lang_one')}", f"{self._lang.language_app.get('mode_settings_lang_two')}"], command=self._change_settings_language)
        self._btn_settings_lang.grid(row=3, column=0, padx=20, pady=20, sticky="s")

    def _change_settings_mode_event(self, mode: str) -> None:
        if mode == "Light" or mode ==  'Світла':
            ref_mode: str = "Light"
        elif mode == "Dark" or mode == 'Темна':
            ref_mode: str = "Dark"
        else:
            ref_mode: str = "System"

        self._new_settings.update({'theme': ref_mode})
        customtkinter.set_appearance_mode(ref_mode)

    def _change_settings_language(self, lang: str) -> None:
        if lang == "English" or lang ==  'Англійська':
            self._new_settings.update({'language': 'EN'})
        elif lang == "Ukrainian" or lang == 'Українська':
            self._new_settings.update({'language': 'UA'})
        else:
            self._new_settings.update({'language': 'EN'})

    def _change_settings_save(self) -> None:
        for key, val in self._new_settings.items():
            self._settings.save({key: val})
