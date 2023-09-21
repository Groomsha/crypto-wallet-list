"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

from .dialog_window_base import Ui_cw_dialog


class MainWindowApp(Ui_cw_dialog):
    def __init__(self) -> None:
        super().__init__()
