"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

from .main_window_base import Ui_MainWindow


class MainWindowApp(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
