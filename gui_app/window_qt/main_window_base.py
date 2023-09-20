# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt6_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(1024, 768))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_tab_widget = QTabWidget(self.centralwidget)
        self.frame_tab_widget.setObjectName(u"frame_tab_widget")
        self.frame_tab_widget.setFocusPolicy(Qt.NoFocus)
        self.frame_tab_widget.setTabPosition(QTabWidget.West)
        self.frame_tab_widget.setTabShape(QTabWidget.Rounded)
        self.f_news = QWidget()
        self.f_news.setObjectName(u"f_news")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_news.sizePolicy().hasHeightForWidth())
        self.f_news.setSizePolicy(sizePolicy)
        self.f_news.setSizeIncrement(QSize(0, 0))
        self.f_news.setBaseSize(QSize(0, 0))
        self.frame_tab_widget.addTab(self.f_news, "")
        self.f_wall = QWidget()
        self.f_wall.setObjectName(u"f_wall")
        self.frame_tab_widget.addTab(self.f_wall, "")
        self.f_setti = QWidget()
        self.f_setti.setObjectName(u"f_setti")
        self.frame_tab_widget.addTab(self.f_setti, "")

        self.verticalLayout.addWidget(self.frame_tab_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.frame_tab_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Crypto Wallet List", None))
        self.frame_tab_widget.setTabText(self.frame_tab_widget.indexOf(self.f_news), QCoreApplication.translate("MainWindow", u"News", None))
        self.frame_tab_widget.setTabText(self.frame_tab_widget.indexOf(self.f_wall), QCoreApplication.translate("MainWindow", u"Wallet", None))
        self.frame_tab_widget.setTabText(self.frame_tab_widget.indexOf(self.f_setti), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

