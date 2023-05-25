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

from gui_app.language.language import Language
from gui_app.window_ctk.news_frame import NewsFrame
from gui_app.window_ctk.wallet_frame import WalletFrame
from gui_app.window_ctk.settings_frame import SettingsFrame


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class GUI_CTk(customtkinter.CTk):
    def __init__(self, settings: Any, path: Dict) -> None:
        super().__init__()

        self._path = path
        self._settings: Any = settings
        self._lang = Language(self._settings, path)

        self._app_ctk: customtkinter.CTk = self
        self._app_ctk.geometry("700x450")
        self._app_ctk.title("Crypto Wallet List")
        self._app_ctk.grid_rowconfigure(0, weight=1)
        self._app_ctk.grid_columnconfigure(1, weight=1)

        self._image_path = None
        self._navigation_label = None
        self._news_btn_image = None
        self._wallet_btn_image = None
        self._settings_btn_image = None
        self._navigation_logo_image = None
        self._image_gui_ctk()

        self._navigation_frame = None
        self._create_news_frame = NewsFrame(self._app_ctk, self._lang)
        self._create_wallet_frame = WalletFrame(self._app_ctk, self._lang)
        self._create_settings_frame = SettingsFrame(self._app_ctk,  self._settings, self._lang)
        self._navigation_gui_ctk()

        self._news_frame_button = None
        self._wallet_frame_button = None
        self._settings_frame_button = None
        self._btn_gui_ctk()

        self._select_frame("news")

    @property
    def image_path(self) -> Any:
        return self._image_path

    @property
    def language(self) -> Any:
        return self._lang

    def _image_gui_ctk(self) -> None:
        self._image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), self._path.get('DIR_IMG'))

        self._navigation_logo_image = customtkinter.CTkImage(Image.open(os.path.join(self._image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self._news_btn_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self._image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(self._image_path, "home_light.png")), size=(20, 20))
        self._wallet_btn_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self._image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(self._image_path, "chat_light.png")), size=(20, 20))
        self._settings_btn_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self._image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(self._image_path, "add_user_light.png")), size=(20, 20))

    def _navigation_gui_ctk(self) -> None:
        self._navigation_frame = customtkinter.CTkFrame(self._app_ctk, corner_radius=0)
        self._navigation_frame.grid(row=0, column=0, sticky="nsew")
        self._navigation_frame.grid_rowconfigure(4, weight=1)

        self._navigation_label = customtkinter.CTkLabel(self._navigation_frame, text=f"{self._lang.language_app.get('btn_app_logo')}", image=self._navigation_logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self._navigation_label.grid(row=0, column=0, padx=20, pady=20)

    def _btn_gui_ctk(self) -> None:
        self._news_frame_button = customtkinter.CTkButton(self._navigation_frame, corner_radius=0, height=40, border_spacing=10, text=f"{self._lang.language_app.get('btn_app_news')}",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self._news_btn_image, anchor="w", command=self._btn_news_event)
        self._news_frame_button.grid(row=1, column=0, sticky="ew")

        self._wallet_frame_button = customtkinter.CTkButton(self._navigation_frame, corner_radius=0, height=40, border_spacing=10, text=f"{self._lang.language_app.get('btn_app_wallet')}",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self._wallet_btn_image, anchor="w", command=self._btn_wallet_event)
        self._wallet_frame_button.grid(row=2, column=0, sticky="ew")

        self._settings_frame_button = customtkinter.CTkButton(self._navigation_frame, corner_radius=0, height=40, border_spacing=10, text=f"{self._lang.language_app.get('btn_app_settings')}",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self._settings_btn_image, anchor="w", command=self._btn_settings_event)
        self._settings_frame_button.grid(row=3, column=0, sticky="ew")

    def _select_frame(self, name: str) -> None:
        self._news_frame_button.configure(fg_color=("gray75", "gray25") if name == "news" else "transparent")
        self._wallet_frame_button.configure(fg_color=("gray75", "gray25") if name == "wallet" else "transparent")
        self._settings_frame_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")

        if name == "news":
            self._create_news_frame.news_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self._create_news_frame.news_frame.grid_forget()
        if name == "wallet":
            self._create_wallet_frame.wallet_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self._create_wallet_frame.wallet_frame.grid_forget()
        if name == "settings":
            self._create_settings_frame.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self._create_settings_frame.settings_frame.grid_forget()


    def _btn_news_event(self) -> None:
        self._select_frame("news")

    def _btn_wallet_event(self) -> None:
        self._select_frame("wallet")

    def _btn_settings_event(self) -> None:
        self._select_frame("settings")

