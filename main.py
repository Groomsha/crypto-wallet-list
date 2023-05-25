"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

from typing import Any

from sources.path_dir import PathDir
from sources.settings import Settings
from gui_app.window_ctk.gui_ctk import GUI_CTk


def main() -> None:
    settings_app = Settings(PathDir().path_app)

    gui_tk: Any = GUI_CTk(settings_app, PathDir().path_app)
    gui_tk.mainloop()


if __name__ == "__main__":
    main()
