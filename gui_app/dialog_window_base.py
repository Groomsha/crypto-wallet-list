# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt6_dialog_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_cw_dialog(object):
    def setupUi(self, cw_dialog):
        if not cw_dialog.objectName():
            cw_dialog.setObjectName(u"cw_dialog")
        cw_dialog.resize(400, 300)
        self.frame = QFrame(cw_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 30, 321, 71))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 81, 51))
        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 10, 101, 51))
        self.lineEdit = QLineEdit(cw_dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 120, 261, 31))
        self.lineEdit_2 = QLineEdit(cw_dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 160, 261, 31))
        self.pushButton = QPushButton(cw_dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 220, 111, 61))

        self.retranslateUi(cw_dialog)

        QMetaObject.connectSlotsByName(cw_dialog)
    # setupUi

    def retranslateUi(self, cw_dialog):
        cw_dialog.setWindowTitle(QCoreApplication.translate("cw_dialog", u"Cripto Wallet", None))
        self.label.setText(QCoreApplication.translate("cw_dialog", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("cw_dialog", u"PushButton", None))
    # retranslateUi

