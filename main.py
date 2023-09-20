"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from gui_app.window_qt.main_window_app import MainWindowApp

from sources.path_dir import PathDir
from sources.settings import Settings


class CreateApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.gui_qt_window = MainWindowApp()
        self.gui_qt_window.setupUi(self)


if __name__ == "__main__":
    settings_app = Settings(PathDir().path_app)

    app = QApplication(sys.argv)
    main_window_qt = CreateApp()
    main_window_qt.show()

    sys.exit(app.exec())
