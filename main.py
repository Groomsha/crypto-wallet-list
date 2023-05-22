"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

import json
from typing import Dict

from gui_app.window_ctk.gui_ctk import GUI_CTk


def main() -> None:
    settings = settings_app()

    gui_tk = GUI_CTk(settings)
    gui_tk.mainloop()


def settings_app() -> Dict:
    try:
        with open("settings.json", "r") as j:
            settings_temp: Dict = json.load(j)
        return settings_temp
    except FileNotFoundError:
        settings_temp: Dict = {'language': 'EN',
                               'proxy': 'False'}

        with open("settings.json", "w") as j:
            json.dump(settings_temp, j)

        return settings_temp


if __name__ == "__main__":
    main()
