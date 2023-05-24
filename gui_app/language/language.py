"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

from typing import Dict


class Language:
    def __init__(self, settings: Dict) -> None:
        self._settings: Dict = settings
