# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dictionaryFormNyQxLe.ui'
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

class Ui_DictionaryAreaWindow(object):
    def setupUi(self, DictionaryAreaWindow):
        if not DictionaryAreaWindow.objectName():
            DictionaryAreaWindow.setObjectName(u"DictionaryAreaWindow")
        DictionaryAreaWindow.resize(1021, 592)
        self.DictionaryAreaCentralWidget = QWidget(DictionaryAreaWindow)
        self.DictionaryAreaCentralWidget.setObjectName(u"DictionaryAreaCentralWidget")
        self.DictionaryAreaCentralWidget.setStyleSheet(u"")
        self.mainFrame = QFrame(self.DictionaryAreaCentralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 1021, 592))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.frameOfCustomDictionaries = QFrame(self.mainFrame)
        self.frameOfCustomDictionaries.setObjectName(u"frameOfCustomDictionaries")
        self.frameOfCustomDictionaries.setGeometry(QRect(30, 130, 301, 431))
        self.frameOfCustomDictionaries.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")
        self.frameOfCustomDictionaries.setFrameShape(QFrame.StyledPanel)
        self.frameOfCustomDictionaries.setFrameShadow(QFrame.Raised)
        self.customLabel = QLabel(self.frameOfCustomDictionaries)
        self.customLabel.setObjectName(u"customLabel")
        self.customLabel.setGeometry(QRect(105, 18, 81, 21))
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(12)
        font.setBold(False)
        self.customLabel.setFont(font)
        self.customLabel.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.dictionariesLabel = QLabel(self.frameOfCustomDictionaries)
        self.dictionariesLabel.setObjectName(u"dictionariesLabel")
        self.dictionariesLabel.setGeometry(QRect(85, 39, 121, 21))
        self.dictionariesLabel.setFont(font)
        self.dictionariesLabel.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.separatedLine_1 = QFrame(self.frameOfCustomDictionaries)
        self.separatedLine_1.setObjectName(u"separatedLine_1")
        self.separatedLine_1.setGeometry(QRect(17, 70, 271, 1))
        self.separatedLine_1.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.separatedLine_1.setFrameShape(QFrame.HLine)
        self.separatedLine_1.setFrameShadow(QFrame.Sunken)
        self.refreshTheListOfCustomDictionariesButton = QPushButton(self.frameOfCustomDictionaries)
        self.refreshTheListOfCustomDictionariesButton.setObjectName(u"refreshTheListOfCustomDictionariesButton")
        self.refreshTheListOfCustomDictionariesButton.setGeometry(QRect(150, 100, 31, 31))
        self.refreshTheListOfCustomDictionariesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshTheListOfCustomDictionariesButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(255, 170, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 170, 0, 220);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 170, 0, 240);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/refreshIcon_W.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshTheListOfCustomDictionariesButton.setIcon(icon)
        self.refreshTheListOfCustomDictionariesButton.setIconSize(QSize(16, 16))
        self.addACustomDictionaryButton = QPushButton(self.frameOfCustomDictionaries)
        self.addACustomDictionaryButton.setObjectName(u"addACustomDictionaryButton")
        self.addACustomDictionaryButton.setGeometry(QRect(110, 100, 31, 31))
        self.addACustomDictionaryButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addACustomDictionaryButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(106, 203, 255);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(106, 203, 255, 220);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(106, 203, 255, 240);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/addSomethingIcon_W.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addACustomDictionaryButton.setIcon(icon1)
        self.addACustomDictionaryButton.setIconSize(QSize(14, 14))
        self.infoFrame = QFrame(self.mainFrame)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setGeometry(QRect(30, 30, 961, 91))
        self.infoFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(0, 70, 190);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QFrame.Raised)
        self.goBackButton = QPushButton(self.infoFrame)
        self.goBackButton.setObjectName(u"goBackButton")
        self.goBackButton.setGeometry(QRect(25, 25, 41, 41))
        self.goBackButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.goBackButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/goBackIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.goBackButton.setIcon(icon2)
        self.goBackButton.setIconSize(QSize(16, 16))
        self.nameOfTheDictionary = QLabel(self.infoFrame)
        self.nameOfTheDictionary.setObjectName(u"nameOfTheDictionary")
        self.nameOfTheDictionary.setGeometry(QRect(90, 20, 271, 31))
        font1 = QFont()
        font1.setFamilies([u"Montserrat SemiBold"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.nameOfTheDictionary.setFont(font1)
        self.nameOfTheDictionary.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.descriptionOfTheDictionary = QLabel(self.infoFrame)
        self.descriptionOfTheDictionary.setObjectName(u"descriptionOfTheDictionary")
        self.descriptionOfTheDictionary.setGeometry(QRect(92, 50, 471, 16))
        font2 = QFont()
        font2.setFamilies([u"Montserrat Medium"])
        self.descriptionOfTheDictionary.setFont(font2)
        self.descriptionOfTheDictionary.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.descriptionOfTheDictionary.setTextFormat(Qt.PlainText)
        self.closeThewindowButton = QPushButton(self.infoFrame)
        self.closeThewindowButton.setObjectName(u"closeThewindowButton")
        self.closeThewindowButton.setGeometry(QRect(895, 25, 41, 41))
        self.closeThewindowButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeThewindowButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 123, 123);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 103, 103);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/closeSomethingIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeThewindowButton.setIcon(icon3)
        self.closeThewindowButton.setIconSize(QSize(10, 10))
        self.minimizeTheWindowButton = QPushButton(self.infoFrame)
        self.minimizeTheWindowButton.setObjectName(u"minimizeTheWindowButton")
        self.minimizeTheWindowButton.setGeometry(QRect(840, 25, 41, 41))
        self.minimizeTheWindowButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeTheWindowButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/minimizeWindowIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeTheWindowButton.setIcon(icon4)
        self.minimizeTheWindowButton.setIconSize(QSize(10, 10))
        self.decorationFrame = QFrame(self.mainFrame)
        self.decorationFrame.setObjectName(u"decorationFrame")
        self.decorationFrame.setGeometry(QRect(900, 130, 91, 431))
        self.decorationFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(0, 70, 190);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")
        self.decorationFrame.setFrameShape(QFrame.StyledPanel)
        self.decorationFrame.setFrameShadow(QFrame.Raised)
        self.decorationCube_1 = QPushButton(self.decorationFrame)
        self.decorationCube_1.setObjectName(u"decorationCube_1")
        self.decorationCube_1.setGeometry(QRect(-10, 50, 21, 31))
        self.decorationCube_1.setCursor(QCursor(Qt.ArrowCursor))
        self.decorationCube_1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"")
        self.decorationCube_1.setIconSize(QSize(10, 10))
        self.decorationCube_4 = QPushButton(self.decorationFrame)
        self.decorationCube_4.setObjectName(u"decorationCube_4")
        self.decorationCube_4.setGeometry(QRect(80, 180, 31, 31))
        self.decorationCube_4.setCursor(QCursor(Qt.ArrowCursor))
        self.decorationCube_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"")
        self.decorationCube_4.setIconSize(QSize(10, 10))
        self.decorationCube_5 = QPushButton(self.decorationFrame)
        self.decorationCube_5.setObjectName(u"decorationCube_5")
        self.decorationCube_5.setGeometry(QRect(71, 280, 31, 31))
        self.decorationCube_5.setCursor(QCursor(Qt.ArrowCursor))
        self.decorationCube_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"")
        self.decorationCube_5.setIconSize(QSize(10, 10))
        self.decorationCube_6 = QPushButton(self.decorationFrame)
        self.decorationCube_6.setObjectName(u"decorationCube_6")
        self.decorationCube_6.setGeometry(QRect(-10, 350, 21, 31))
        self.decorationCube_6.setCursor(QCursor(Qt.ArrowCursor))
        self.decorationCube_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"")
        self.decorationCube_6.setIconSize(QSize(10, 10))
        self.decorationCube_2 = QPushButton(self.decorationFrame)
        self.decorationCube_2.setObjectName(u"decorationCube_2")
        self.decorationCube_2.setGeometry(QRect(80, -10, 21, 31))
        self.decorationCube_2.setCursor(QCursor(Qt.ArrowCursor))
        self.decorationCube_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}\n"
"")
        self.decorationCube_2.setIconSize(QSize(10, 10))
        self.decorationCube_3 = QPushButton(self.decorationFrame)
        self.decorationCube_3.setObjectName(u"decorationCube_3")
        self.decorationCube_3.setGeometry(QRect(-10, 140, 31, 41))
        self.decorationCube_3.setCursor(QCursor(Qt.ArrowCursor))
        self.decorationCube_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"")
        self.decorationCube_3.setIconSize(QSize(10, 10))
        DictionaryAreaWindow.setCentralWidget(self.DictionaryAreaCentralWidget)

        self.retranslateUi(DictionaryAreaWindow)

        QMetaObject.connectSlotsByName(DictionaryAreaWindow)
    # setupUi

    def retranslateUi(self, DictionaryAreaWindow):
        DictionaryAreaWindow.setWindowTitle(QCoreApplication.translate("DictionaryAreaWindow", u"MainWindow", None))
        self.customLabel.setText(QCoreApplication.translate("DictionaryAreaWindow", u"CUSTOM", None))
        self.dictionariesLabel.setText(QCoreApplication.translate("DictionaryAreaWindow", u"DICTIONARIES", None))
        self.refreshTheListOfCustomDictionariesButton.setText("")
        self.addACustomDictionaryButton.setText("")
        self.goBackButton.setText("")
        self.nameOfTheDictionary.setText(QCoreApplication.translate("DictionaryAreaWindow", u"My Words", None))
        self.descriptionOfTheDictionary.setText(QCoreApplication.translate("DictionaryAreaWindow", u"Dictionary for learning new words in English", None))
        self.closeThewindowButton.setText("")
        self.minimizeTheWindowButton.setText("")
        self.decorationCube_1.setText("")
        self.decorationCube_4.setText("")
        self.decorationCube_5.setText("")
        self.decorationCube_6.setText("")
        self.decorationCube_2.setText("")
        self.decorationCube_3.setText("")
    # retranslateUi

