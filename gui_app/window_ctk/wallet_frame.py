"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

import os

from PIL import Image
import customtkinter


class WalletFrame:
    def __init__(self, ctk: customtkinter.CTkFrame) -> None:
        self._window = ctk

        self._image_icon = None
        self._image_wallet_frame()

        self._wallet_frame = customtkinter.CTkFrame(self._window, corner_radius=0, fg_color="transparent")

        self._btn_wallet_1 = None
        self._btn_wallet_frame()

    @property
    def wallet_frame(self):
        return self._wallet_frame

    def _image_wallet_frame(self) -> None:
        self._image_icon = customtkinter.CTkImage(Image.open(os.path.join(self._window.image_path, "image_icon_light.png")), size=(20, 20))

    def _btn_wallet_frame(self) -> None:
        self._btn_wallet_1 = customtkinter.CTkButton(self._wallet_frame, text="CTkButton", image=self._image_icon, compound="right")
        self._btn_wallet_1.grid(row=2, column=0, padx=20, pady=10)
