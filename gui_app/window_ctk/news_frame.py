"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

import os

from PIL import Image
import customtkinter


class NewsFrame:
    def __init__(self, ctk: customtkinter.CTkFrame) -> None:
        self._window = ctk

        self._large_image = None
        self._image_icon = None
        self._image_news_frame()

        self._news_frame = customtkinter.CTkFrame(self._window, corner_radius=0, fg_color="transparent")
        self._news_frame.grid_columnconfigure(0, weight=1)

        self._image_label = customtkinter.CTkLabel(self._news_frame, text="", image=self._large_image)
        self._image_label.grid(row=0, column=0, padx=20, pady=10)

        self._btn_news_button_1 = None
        self._btn_news_frame()

    @property
    def news_frame(self) -> customtkinter.CTkFrame:
        return self._news_frame

    def _image_news_frame(self) -> None:
        self._large_image = customtkinter.CTkImage(Image.open(os.path.join(self._window.image_path, "large_test_image.png")), size=(500, 150))
        self._image_icon = customtkinter.CTkImage(Image.open(os.path.join(self._window.image_path, "image_icon_light.png")), size=(20, 20))

    def _btn_news_frame(self) -> None:
        self._news_button_1 = customtkinter.CTkButton(self._news_frame, text="", image=self._image_icon)
        self._news_button_1.grid(row=1, column=0, padx=20, pady=10)
