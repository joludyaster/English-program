# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createACustomDictionaryFormPrmiPn.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_CreateACustomDictionaryWindow(object):
    def setupUi(self, CreateACustomDictionaryWindow):
        if not CreateACustomDictionaryWindow.objectName():
            CreateACustomDictionaryWindow.setObjectName(u"CreateACustomDictionaryWindow")
        CreateACustomDictionaryWindow.resize(643, 390)
        CreateACustomDictionaryWindow.setMinimumSize(QSize(643, 236))
        CreateACustomDictionaryWindow.setMaximumSize(QSize(16777215, 16777215))
        self.CreateACustomDictionaryCentralWidget = QWidget(CreateACustomDictionaryWindow)
        self.CreateACustomDictionaryCentralWidget.setObjectName(u"CreateACustomDictionaryCentralWidget")
        self.mainFrame = QFrame(self.CreateACustomDictionaryCentralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 643, 391))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.blankForTheNameOfDictionary = QLineEdit(self.mainFrame)
        self.blankForTheNameOfDictionary.setObjectName(u"blankForTheNameOfDictionary")
        self.blankForTheNameOfDictionary.setGeometry(QRect(40, 55, 561, 51))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(13)
        font.setBold(False)
        self.blankForTheNameOfDictionary.setFont(font)
        self.blankForTheNameOfDictionary.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.nameLabel = QLabel(self.mainFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(40, 30, 231, 21))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.nameLabel.setFont(font1)
        self.nameLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.cancelButton = QPushButton(self.mainFrame)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(300, 320, 151, 41))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.cancelButton.setFont(font2)
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(208, 208, 208);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(202, 202, 202);\n"
"}")
        self.saveAndCreateADictionaryButton = QPushButton(self.mainFrame)
        self.saveAndCreateADictionaryButton.setObjectName(u"saveAndCreateADictionaryButton")
        self.saveAndCreateADictionaryButton.setGeometry(QRect(460, 320, 141, 41))
        self.saveAndCreateADictionaryButton.setFont(font2)
        self.saveAndCreateADictionaryButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveAndCreateADictionaryButton.setStyleSheet(u"QPushButton {\n"
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
        self.blankForTheDescription = QPlainTextEdit(self.mainFrame)
        self.blankForTheDescription.setObjectName(u"blankForTheDescription")
        self.blankForTheDescription.setGeometry(QRect(40, 164, 561, 141))
        self.blankForTheDescription.setFont(font)
        self.blankForTheDescription.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.blankForTheDescription.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.blankForTheDescription.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.blankForTheDescription.setOverwriteMode(False)
        self.descriptionLabel = QLabel(self.mainFrame)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(40, 140, 91, 16))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.descriptionLabel.setFont(font3)
        self.descriptionLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.descriptionLabel.setWordWrap(True)
        CreateACustomDictionaryWindow.setCentralWidget(self.CreateACustomDictionaryCentralWidget)

        self.retranslateUi(CreateACustomDictionaryWindow)

        QMetaObject.connectSlotsByName(CreateACustomDictionaryWindow)
    # setupUi

    def retranslateUi(self, CreateACustomDictionaryWindow):
        CreateACustomDictionaryWindow.setWindowTitle(QCoreApplication.translate("CreateACustomDictionaryWindow", u"MainWindow", None))
        self.blankForTheNameOfDictionary.setText("")
        self.blankForTheNameOfDictionary.setPlaceholderText(QCoreApplication.translate("CreateACustomDictionaryWindow", u"Name of the custom dictionary", None))
        self.nameLabel.setText(QCoreApplication.translate("CreateACustomDictionaryWindow", u"Name of the custom dictionary", None))
        self.cancelButton.setText(QCoreApplication.translate("CreateACustomDictionaryWindow", u"Cancel", None))
        self.saveAndCreateADictionaryButton.setText(QCoreApplication.translate("CreateACustomDictionaryWindow", u"Save", None))
        self.blankForTheDescription.setPlainText("")
        self.blankForTheDescription.setPlaceholderText(QCoreApplication.translate("CreateACustomDictionaryWindow", u"Enter the description", None))
        self.descriptionLabel.setText(QCoreApplication.translate("CreateACustomDictionaryWindow", u"Descritpion", None))
    # retranslateUi

