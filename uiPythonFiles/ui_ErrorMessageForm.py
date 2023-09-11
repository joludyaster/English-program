# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorMessageFormvHJoyF.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import icons.icons_rc

class Ui_ErrorWindow(object):
    def setupUi(self, ErrorWindow):
        if not ErrorWindow.objectName():
            ErrorWindow.setObjectName(u"ErrorWindow")
        ErrorWindow.resize(671, 176)
        self.errorCentralWidget = QWidget(ErrorWindow)
        self.errorCentralWidget.setObjectName(u"errorCentralWidget")
        self.mainFrame = QFrame(self.errorCentralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 671, 176))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.icon = QPushButton(self.mainFrame)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(40, 40, 101, 81))
        self.icon.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/warningIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon1)
        self.icon.setIconSize(QSize(70, 70))
        self.okButton = QPushButton(self.mainFrame)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setGeometry(QRect(540, 130, 101, 31))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(12)
        font.setBold(True)
        self.okButton.setFont(font)
        self.okButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.okButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(56, 236, 113);\n"
"	border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(69, 241, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(48, 221, 103);\n"
"}")
        self.cautionLabel = QLabel(self.mainFrame)
        self.cautionLabel.setObjectName(u"cautionLabel")
        self.cautionLabel.setGeometry(QRect(148, 50, 111, 31))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(23)
        font1.setBold(True)
        self.cautionLabel.setFont(font1)
        self.cautionLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.explanationLabel = QLabel(self.mainFrame)
        self.explanationLabel.setObjectName(u"explanationLabel")
        self.explanationLabel.setGeometry(QRect(150, 85, 461, 20))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(13)
        font2.setBold(False)
        self.explanationLabel.setFont(font2)
        self.explanationLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        ErrorWindow.setCentralWidget(self.errorCentralWidget)

        self.retranslateUi(ErrorWindow)

        QMetaObject.connectSlotsByName(ErrorWindow)
    # setupUi

    def retranslateUi(self, ErrorWindow):
        ErrorWindow.setWindowTitle(QCoreApplication.translate("ErrorWindow", u"MainWindow", None))
        self.icon.setText("")
        self.okButton.setText(QCoreApplication.translate("ErrorWindow", u"OK", None))
        self.cautionLabel.setText(QCoreApplication.translate("ErrorWindow", u"Oops...", None))
        self.explanationLabel.setText(QCoreApplication.translate("ErrorWindow", u"Something went wrong. Try again.", None))
    # retranslateUi

