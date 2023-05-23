"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

import os

from PIL import Image
import customtkinter


class SettingsFrame:
    def __init__(self, ctk: customtkinter.CTkFrame) -> None:
        self._window = ctk

        self._image_icon = None
        self._image_settings_frame()

        self._settings_frame = customtkinter.CTkFrame(self._window, corner_radius=0, fg_color="transparent")

        self._btn_settings_mode = None
        self._btn_settings_1 = None
        self._btn_settings_frame()

    @property
    def settings_frame(self) -> customtkinter.CTkFrame:
        return self._settings_frame

    def _image_settings_frame(self) -> None:
        self._image_icon = customtkinter.CTkImage(Image.open(os.path.join(self._window.image_path, "image_icon_light.png")), size=(20, 20))

    def _btn_settings_frame(self) -> None:
        self._btn_settings_1 = customtkinter.CTkButton(self._settings_frame, text="CTkButton", image=self._image_icon, compound="top")
        self._btn_settings_1.grid(row=3, column=0, padx=20, pady=10)

        self._btn_settings_mode = customtkinter.CTkOptionMenu(self._settings_frame, values=["Light", "Dark", "System"], command=self._change_settings_mode_event)
        self._btn_settings_mode.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def _change_settings_mode_event(self, new_appearance_mode) -> None:
        customtkinter.set_appearance_mode(new_appearance_mode)
