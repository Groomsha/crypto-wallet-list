"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

from typing import Dict

import customtkinter


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class GUI_ctk(customtkinter.CTk):
    def __init__(self, settings: Dict) -> None:
        super().__init__()

        self.app_ctk = self
        self.settings = settings

        self.app_ctk.geometry("400x240")
        self.app_ctk.title("Crypto Wallet List")
