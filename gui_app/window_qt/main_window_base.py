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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

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
        self.btn_save = QPushButton(self.f_setti)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(790, 500, 161, 71))
        self.btn_backup = QPushButton(self.f_setti)
        self.btn_backup.setObjectName(u"btn_backup")
        self.btn_backup.setGeometry(QRect(560, 500, 161, 71))
        self.by_label = QLabel(self.f_setti)
        self.by_label.setObjectName(u"by_label")
        self.by_label.setGeometry(QRect(20, 400, 461, 301))
        self.by_label.setFrameShape(QFrame.Box)
        self.by_label.setFrameShadow(QFrame.Plain)
        self.by_label.setLineWidth(1)
        self.by_label.setMidLineWidth(0)
        self.comboBox = QComboBox(self.f_setti)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(80, 80, 201, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setFocusPolicy(Qt.ClickFocus)
        self.comboBox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.f_proxy_sett = QFrame(self.f_setti)
        self.f_proxy_sett.setObjectName(u"f_proxy_sett")
        self.f_proxy_sett.setGeometry(QRect(360, 80, 591, 191))
        self.f_proxy_sett.setFrameShape(QFrame.StyledPanel)
        self.f_proxy_sett.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.f_proxy_sett)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 80, 261, 41))
        self.lineEdit.setMaxLength(64)
        self.lineEdit_2 = QLineEdit(self.f_proxy_sett)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(430, 80, 121, 41))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setInputMask(u"")
        self.lineEdit_2.setMaxLength(5)
        self.cb_proxy = QCheckBox(self.f_proxy_sett)
        self.cb_proxy.setObjectName(u"cb_proxy")
        self.cb_proxy.setGeometry(QRect(50, 80, 90, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_proxy.sizePolicy().hasHeightForWidth())
        self.cb_proxy.setSizePolicy(sizePolicy1)
        self.cb_proxy.setMaximumSize(QSize(90, 41))
        self.cb_proxy.setSizeIncrement(QSize(0, 0))
        self.cb_proxy.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.cb_proxy.setFont(font2)
        self.cb_proxy.setIconSize(QSize(16, 16))
        self.ps_label = QLabel(self.f_proxy_sett)
        self.ps_label.setObjectName(u"ps_label")
        self.ps_label.setGeometry(QRect(10, 10, 571, 51))
        self.ps_label.setFont(font1)
        self.ps_label.setTextFormat(Qt.PlainText)
        self.ps_label.setAlignment(Qt.AlignCenter)
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
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_backup.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.by_label.setText(QCoreApplication.translate("MainWindow", u"@ By", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Ukrainian", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"English", None))
        self.lineEdit_2.setText("")
        self.cb_proxy.setText(QCoreApplication.translate("MainWindow", u"On Proxy", None))
        self.ps_label.setText(QCoreApplication.translate("MainWindow", u"Proxy Settings", None))
        self.frame_tab_widget.setTabText(self.frame_tab_widget.indexOf(self.f_setti), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

