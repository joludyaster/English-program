# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrationFormUsbDRQ.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import icons.icons_rc

class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        if not RegistrationWindow.objectName():
            RegistrationWindow.setObjectName(u"RegistrationWindow")
        RegistrationWindow.resize(1031, 720)
        RegistrationWindow.setMinimumSize(QSize(1031, 720))
        RegistrationWindow.setMaximumSize(QSize(1031, 720))
        self.registrationCentralWidget = QWidget(RegistrationWindow)
        self.registrationCentralWidget.setObjectName(u"registrationCentralWidget")
        self.mainFrame = QFrame(self.registrationCentralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 1031, 721))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.backgroundImage = QLabel(self.mainFrame)
        self.backgroundImage.setObjectName(u"backgroundImage")
        self.backgroundImage.setGeometry(QRect(-1, 40, 1032, 681))
        self.backgroundImage.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.backgroundImage.setPixmap(QPixmap(u":/backgroundImage.jpg"))
        self.backgroundImage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.movingFrame = QFrame(self.mainFrame)
        self.movingFrame.setObjectName(u"movingFrame")
        self.movingFrame.setGeometry(QRect(-1, 0, 1032, 41))
        self.movingFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.movingFrame.setFrameShape(QFrame.NoFrame)
        self.movingFrame.setFrameShadow(QFrame.Raised)
        self.closeTheWindowButton = QPushButton(self.movingFrame)
        self.closeTheWindowButton.setObjectName(u"closeTheWindowButton")
        self.closeTheWindowButton.setGeometry(QRect(991, 0, 41, 41))
        self.closeTheWindowButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeTheWindowButton.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 123, 123);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 103, 103);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/closeSomethingIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeTheWindowButton.setIcon(icon)
        self.closeTheWindowButton.setIconSize(QSize(10, 10))
        self.minimizeTheWindowButton = QPushButton(self.movingFrame)
        self.minimizeTheWindowButton.setObjectName(u"minimizeTheWindowButton")
        self.minimizeTheWindowButton.setGeometry(QRect(950, 0, 41, 41))
        self.minimizeTheWindowButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeTheWindowButton.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/minimizeWindowIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeTheWindowButton.setIcon(icon1)
        self.minimizeTheWindowButton.setIconSize(QSize(10, 16))
        self.informationFrame = QFrame(self.mainFrame)
        self.informationFrame.setObjectName(u"informationFrame")
        self.informationFrame.setGeometry(QRect(60, 110, 461, 541))
        self.informationFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(255, 255, 255, 220);\n"
"	border: none;\n"
"}")
        self.informationFrame.setFrameShape(QFrame.NoFrame)
        self.informationFrame.setFrameShadow(QFrame.Raised)
        self.programIcon = QPushButton(self.informationFrame)
        self.programIcon.setObjectName(u"programIcon")
        self.programIcon.setGeometry(QRect(55, 60, 41, 41))
        self.programIcon.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/programIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.programIcon.setIcon(icon2)
        self.programIcon.setIconSize(QSize(45, 45))
        self.programNameLabel_1 = QLabel(self.informationFrame)
        self.programNameLabel_1.setObjectName(u"programNameLabel_1")
        self.programNameLabel_1.setGeometry(QRect(97, 60, 71, 21))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(14)
        font.setBold(True)
        self.programNameLabel_1.setFont(font)
        self.programNameLabel_1.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	color: rgb(84, 110, 122);\n"
"	border: none;\n"
"}")
        self.programNameLabel_2 = QLabel(self.informationFrame)
        self.programNameLabel_2.setObjectName(u"programNameLabel_2")
        self.programNameLabel_2.setGeometry(QRect(97, 80, 141, 21))
        self.programNameLabel_2.setFont(font)
        self.programNameLabel_2.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.emailAddressLabel = QLabel(self.informationFrame)
        self.emailAddressLabel.setObjectName(u"emailAddressLabel")
        self.emailAddressLabel.setGeometry(QRect(60, 210, 101, 16))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.emailAddressLabel.setFont(font1)
        self.emailAddressLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.passwordLabel = QLabel(self.informationFrame)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(60, 300, 61, 16))
        self.passwordLabel.setFont(font1)
        self.passwordLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.blankForTheAddress = QLineEdit(self.informationFrame)
        self.blankForTheAddress.setObjectName(u"blankForTheAddress")
        self.blankForTheAddress.setGeometry(QRect(60, 240, 341, 31))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.blankForTheAddress.setFont(font2)
        self.blankForTheAddress.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")
        self.createAnAccountButton = QPushButton(self.informationFrame)
        self.createAnAccountButton.setObjectName(u"createAnAccountButton")
        self.createAnAccountButton.setGeometry(QRect(60, 390, 341, 51))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.createAnAccountButton.setFont(font3)
        self.createAnAccountButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 25px;\n"
"	background-color: rgb(0, 98, 255);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 115, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 90, 255);\n"
"}")
        self.blankForThePassword = QLineEdit(self.informationFrame)
        self.blankForThePassword.setObjectName(u"blankForThePassword")
        self.blankForThePassword.setGeometry(QRect(58, 330, 291, 31))
        self.blankForThePassword.setFont(font2)
        self.blankForThePassword.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 7px;\n"
"}")
        self.typeOfTheWindowLabel = QLabel(self.informationFrame)
        self.typeOfTheWindowLabel.setObjectName(u"typeOfTheWindowLabel")
        self.typeOfTheWindowLabel.setGeometry(QRect(60, 130, 201, 41))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(35)
        font4.setBold(True)
        self.typeOfTheWindowLabel.setFont(font4)
        self.typeOfTheWindowLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.haveAnAccountLabel = QPushButton(self.informationFrame)
        self.haveAnAccountLabel.setObjectName(u"haveAnAccountLabel")
        self.haveAnAccountLabel.setGeometry(QRect(60, 470, 121, 16))
        self.haveAnAccountLabel.setFont(font1)
        self.haveAnAccountLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.haveAnAccountLabel.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.separatedLine_1 = QFrame(self.informationFrame)
        self.separatedLine_1.setObjectName(u"separatedLine_1")
        self.separatedLine_1.setGeometry(QRect(60, 270, 341, 1))
        self.separatedLine_1.setStyleSheet(u"background-color: gray;\n"
"border: none;")
        self.separatedLine_1.setFrameShadow(QFrame.Sunken)
        self.separatedLine_1.setFrameShape(QFrame.HLine)
        self.separatedLine_2 = QFrame(self.informationFrame)
        self.separatedLine_2.setObjectName(u"separatedLine_2")
        self.separatedLine_2.setGeometry(QRect(60, 360, 341, 1))
        self.separatedLine_2.setStyleSheet(u"background-color: gray;\n"
"border: none;")
        self.separatedLine_2.setFrameShape(QFrame.HLine)
        self.separatedLine_2.setFrameShadow(QFrame.Sunken)
        self.openSignInWindowButton = QPushButton(self.informationFrame)
        self.openSignInWindowButton.setObjectName(u"openSignInWindowButton")
        self.openSignInWindowButton.setGeometry(QRect(180, 470, 51, 16))
        self.openSignInWindowButton.setFont(font1)
        self.openSignInWindowButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.openSignInWindowButton.setStyleSheet(u"QPushButton {\n"
"	color: rgba(0, 136, 255, 255);\n"
"	background-color: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	text-decoration: underline;\n"
"}\n"
"")
        self.showAndHidePasswordButton = QPushButton(self.informationFrame)
        self.showAndHidePasswordButton.setObjectName(u"showAndHidePasswordButton")
        self.showAndHidePasswordButton.setGeometry(QRect(359, 332, 31, 24))
        self.showAndHidePasswordButton.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/hideIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showAndHidePasswordButton.setIcon(icon3)
        self.showAndHidePasswordButton.setIconSize(QSize(25, 25))
        RegistrationWindow.setCentralWidget(self.registrationCentralWidget)

        self.retranslateUi(RegistrationWindow)

        QMetaObject.connectSlotsByName(RegistrationWindow)
    # setupUi

    def retranslateUi(self, RegistrationWindow):
        RegistrationWindow.setWindowTitle(QCoreApplication.translate("RegistrationWindow", u"MainWindow", None))
        self.backgroundImage.setText("")
        self.closeTheWindowButton.setText("")
        self.minimizeTheWindowButton.setText("")
        self.programIcon.setText("")
        self.programNameLabel_1.setText(QCoreApplication.translate("RegistrationWindow", u"ELFAY", None))
        self.programNameLabel_2.setText(QCoreApplication.translate("RegistrationWindow", u"PRODUCTION", None))
        self.emailAddressLabel.setText(QCoreApplication.translate("RegistrationWindow", u"E-mail address", None))
        self.passwordLabel.setText(QCoreApplication.translate("RegistrationWindow", u"Password", None))
        self.blankForTheAddress.setInputMask("")
        self.blankForTheAddress.setPlaceholderText(QCoreApplication.translate("RegistrationWindow", u"you@example.com", None))
        self.createAnAccountButton.setText(QCoreApplication.translate("RegistrationWindow", u"Create an account", None))
#if QT_CONFIG(shortcut)
        self.createAnAccountButton.setShortcut(QCoreApplication.translate("RegistrationWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.blankForThePassword.setText("")
        self.blankForThePassword.setPlaceholderText(QCoreApplication.translate("RegistrationWindow", u"Your password", None))
        self.typeOfTheWindowLabel.setText(QCoreApplication.translate("RegistrationWindow", u"SIGN UP", None))
        self.haveAnAccountLabel.setText(QCoreApplication.translate("RegistrationWindow", u"Have an account?", None))
        self.openSignInWindowButton.setText(QCoreApplication.translate("RegistrationWindow", u"Sign in", None))
        self.showAndHidePasswordButton.setText("")
    # retranslateUi

