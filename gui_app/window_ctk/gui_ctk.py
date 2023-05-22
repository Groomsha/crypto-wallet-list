"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

from typing import Dict

import customtkinter

from .settings_frame import SettingsFrame


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class GUI_CTk(customtkinter.CTk):
    def __init__(self, settings: Dict) -> None:
        super().__init__()

        self.app_ctk = self
        self.settings = settings

        self.app_ctk.geometry("700x450")
        self.app_ctk.title("Crypto Wallet List")
        self.app_ctk.grid_rowconfigure(0, weight=1)
        self.app_ctk.grid_columnconfigure(1, weight=1)

        self.navigation_window = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_window.grid(row=0, column=0, sticky="nsew")
        self.navigation_window.grid_rowconfigure(4, weight=1)

        self.navigation()

        self.settings_frame = SettingsFrame(self.navigation_window)

    def navigation(self) -> None:
        # self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_window, text="Navigation", image=None,
        #                                                      compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        # self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.button_news = customtkinter.CTkButton(self.navigation_window, corner_radius=0, height=40, border_spacing=10, text="News",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=None, anchor="w", command=None)
        self.button_news.grid(row=1, column=0, sticky="ew")

        self.button_wallet = customtkinter.CTkButton(self.navigation_window, corner_radius=0, height=40, border_spacing=10, text="Wallet",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=None, anchor="w", command=None)
        self.button_wallet.grid(row=2, column=0, sticky="ew")

        self.button_settings = customtkinter.CTkButton(self.navigation_window, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=None, anchor="w", command=None)
        self.button_settings.grid(row=3, column=0, sticky="ew")


    # def settings(self) -> None:

