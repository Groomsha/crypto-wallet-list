"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""


import customtkinter


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class GUI_ctk(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.app_ctk = self
        self.app_ctk.geometry("400x240")
        self.app_ctk.title("Crypto Wallet List")
