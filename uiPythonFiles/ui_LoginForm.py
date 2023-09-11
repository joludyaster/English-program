# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginFormUNEfKE.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)
import icons.icons_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(1031, 720)
        LoginWindow.setMinimumSize(QSize(1031, 720))
        LoginWindow.setMaximumSize(QSize(1031, 720))
        self.loginCentralWidget = QWidget(LoginWindow)
        self.loginCentralWidget.setObjectName(u"loginCentralWidget")
        self.mainFrame = QFrame(self.loginCentralWidget)
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
        icon = QIcon()
        icon.addFile(u":/minimizeWindowIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeTheWindowButton.setIcon(icon)
        self.minimizeTheWindowButton.setIconSize(QSize(9, 9))
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
        icon1 = QIcon()
        icon1.addFile(u":/closeSomethingIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeTheWindowButton.setIcon(icon1)
        self.closeTheWindowButton.setIconSize(QSize(9, 9))
        self.stackedWidget = QStackedWidget(self.mainFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(60, 110, 461, 541))
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"	background-color: none;\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}")
        self.signUpPage = QWidget()
        self.signUpPage.setObjectName(u"signUpPage")
        self.informationFrame = QFrame(self.signUpPage)
        self.informationFrame.setObjectName(u"informationFrame")
        self.informationFrame.setGeometry(QRect(0, 0, 461, 541))
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
        self.programNameLabel = QLabel(self.informationFrame)
        self.programNameLabel.setObjectName(u"programNameLabel")
        self.programNameLabel.setGeometry(QRect(97, 60, 71, 21))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(14)
        font.setBold(True)
        self.programNameLabel.setFont(font)
        self.programNameLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	color: rgb(84, 110, 122);\n"
"	border: none;\n"
"}")
        self.programSubnameLabel = QLabel(self.informationFrame)
        self.programSubnameLabel.setObjectName(u"programSubnameLabel")
        self.programSubnameLabel.setGeometry(QRect(97, 80, 141, 21))
        self.programSubnameLabel.setFont(font)
        self.programSubnameLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.emailAddressLabel_1 = QLabel(self.informationFrame)
        self.emailAddressLabel_1.setObjectName(u"emailAddressLabel_1")
        self.emailAddressLabel_1.setGeometry(QRect(60, 210, 101, 16))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.emailAddressLabel_1.setFont(font1)
        self.emailAddressLabel_1.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.forgotPasswordButton = QPushButton(self.informationFrame)
        self.forgotPasswordButton.setObjectName(u"forgotPasswordButton")
        self.forgotPasswordButton.setGeometry(QRect(280, 300, 121, 16))
        self.forgotPasswordButton.setFont(font1)
        self.forgotPasswordButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgotPasswordButton.setStyleSheet(u"QPushButton {\n"
"	color: rgba(0, 136, 255, 255);\n"
"	background-color: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	text-decoration: underline;\n"
"}\n"
"")
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
        self.signInButton = QPushButton(self.informationFrame)
        self.signInButton.setObjectName(u"signInButton")
        self.signInButton.setGeometry(QRect(60, 390, 341, 51))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.signInButton.setFont(font3)
        self.signInButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signInButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.signInButton.setAcceptDrops(False)
        self.signInButton.setStyleSheet(u"QPushButton {\n"
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
        self.blankForThePassword.setEchoMode(QLineEdit.Normal)
        self.typeOfTheWindowLabel = QLabel(self.informationFrame)
        self.typeOfTheWindowLabel.setObjectName(u"typeOfTheWindowLabel")
        self.typeOfTheWindowLabel.setGeometry(QRect(56, 130, 181, 41))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(35)
        font4.setBold(True)
        self.typeOfTheWindowLabel.setFont(font4)
        self.typeOfTheWindowLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.noAccountLabel = QPushButton(self.informationFrame)
        self.noAccountLabel.setObjectName(u"noAccountLabel")
        self.noAccountLabel.setGeometry(QRect(60, 470, 91, 16))
        self.noAccountLabel.setFont(font1)
        self.noAccountLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.noAccountLabel.setStyleSheet(u"QPushButton {\n"
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
        self.signUpButton = QPushButton(self.informationFrame)
        self.signUpButton.setObjectName(u"signUpButton")
        self.signUpButton.setGeometry(QRect(150, 470, 51, 16))
        self.signUpButton.setFont(font1)
        self.signUpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signUpButton.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.signUpPage)
        self.restoreThePasswordPage = QWidget()
        self.restoreThePasswordPage.setObjectName(u"restoreThePasswordPage")
        self.informationFrame_2 = QFrame(self.restoreThePasswordPage)
        self.informationFrame_2.setObjectName(u"informationFrame_2")
        self.informationFrame_2.setGeometry(QRect(0, 0, 461, 541))
        self.informationFrame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(255, 255, 255, 220);\n"
"	border: none;\n"
"}")
        self.informationFrame_2.setFrameShape(QFrame.NoFrame)
        self.informationFrame_2.setFrameShadow(QFrame.Raised)
        self.programIcon_2 = QPushButton(self.informationFrame_2)
        self.programIcon_2.setObjectName(u"programIcon_2")
        self.programIcon_2.setGeometry(QRect(55, 60, 41, 41))
        self.programIcon_2.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.programIcon_2.setIcon(icon2)
        self.programIcon_2.setIconSize(QSize(45, 45))
        self.programNameLabel_2 = QLabel(self.informationFrame_2)
        self.programNameLabel_2.setObjectName(u"programNameLabel_2")
        self.programNameLabel_2.setGeometry(QRect(97, 60, 71, 21))
        self.programNameLabel_2.setFont(font)
        self.programNameLabel_2.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	color: rgb(84, 110, 122);\n"
"	border: none;\n"
"}")
        self.programSubnameLabel_2 = QLabel(self.informationFrame_2)
        self.programSubnameLabel_2.setObjectName(u"programSubnameLabel_2")
        self.programSubnameLabel_2.setGeometry(QRect(97, 80, 141, 21))
        self.programSubnameLabel_2.setFont(font)
        self.programSubnameLabel_2.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.emailAddressLabel_2 = QLabel(self.informationFrame_2)
        self.emailAddressLabel_2.setObjectName(u"emailAddressLabel_2")
        self.emailAddressLabel_2.setGeometry(QRect(60, 300, 101, 16))
        self.emailAddressLabel_2.setFont(font1)
        self.emailAddressLabel_2.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.blankForTheAddress_2 = QLineEdit(self.informationFrame_2)
        self.blankForTheAddress_2.setObjectName(u"blankForTheAddress_2")
        self.blankForTheAddress_2.setGeometry(QRect(60, 330, 341, 31))
        self.blankForTheAddress_2.setFont(font2)
        self.blankForTheAddress_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")
        self.typeOfTheWindowLabel_2 = QLabel(self.informationFrame_2)
        self.typeOfTheWindowLabel_2.setObjectName(u"typeOfTheWindowLabel_2")
        self.typeOfTheWindowLabel_2.setGeometry(QRect(56, 130, 311, 101))
        self.typeOfTheWindowLabel_2.setFont(font4)
        self.typeOfTheWindowLabel_2.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.typeOfTheWindowLabel_2.setWordWrap(True)
        self.separatedLine_3 = QFrame(self.informationFrame_2)
        self.separatedLine_3.setObjectName(u"separatedLine_3")
        self.separatedLine_3.setGeometry(QRect(60, 360, 341, 1))
        self.separatedLine_3.setStyleSheet(u"background-color: gray;\n"
"border: none;")
        self.separatedLine_3.setFrameShadow(QFrame.Sunken)
        self.separatedLine_3.setFrameShape(QFrame.HLine)
        self.goBackButton = QPushButton(self.informationFrame_2)
        self.goBackButton.setObjectName(u"goBackButton")
        self.goBackButton.setGeometry(QRect(190, 380, 101, 41))
        font5 = QFont()
        font5.setFamilies([u"Montserrat"])
        font5.setPointSize(13)
        font5.setBold(True)
        self.goBackButton.setFont(font5)
        self.goBackButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.goBackButton.setStyleSheet(u"QPushButton {\n"
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
        self.nextStepButton = QPushButton(self.informationFrame_2)
        self.nextStepButton.setObjectName(u"nextStepButton")
        self.nextStepButton.setGeometry(QRect(300, 380, 101, 41))
        self.nextStepButton.setFont(font3)
        self.nextStepButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextStepButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.nextStepButton.setAcceptDrops(False)
        self.nextStepButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 7px;\n"
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
        self.nextStepButton.setIconSize(QSize(20, 20))
        self.stackedWidget.addWidget(self.restoreThePasswordPage)
        self.newPasswordConfirmationPage = QWidget()
        self.newPasswordConfirmationPage.setObjectName(u"newPasswordConfirmationPage")
        self.informationFrame_3 = QFrame(self.newPasswordConfirmationPage)
        self.informationFrame_3.setObjectName(u"informationFrame_3")
        self.informationFrame_3.setGeometry(QRect(0, 0, 461, 541))
        self.informationFrame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(255, 255, 255, 220);\n"
"	border: none;\n"
"}")
        self.informationFrame_3.setFrameShape(QFrame.NoFrame)
        self.informationFrame_3.setFrameShadow(QFrame.Raised)
        self.programIcon_3 = QPushButton(self.informationFrame_3)
        self.programIcon_3.setObjectName(u"programIcon_3")
        self.programIcon_3.setGeometry(QRect(55, 60, 41, 41))
        self.programIcon_3.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.programIcon_3.setIcon(icon2)
        self.programIcon_3.setIconSize(QSize(45, 45))
        self.programNameLabel_3 = QLabel(self.informationFrame_3)
        self.programNameLabel_3.setObjectName(u"programNameLabel_3")
        self.programNameLabel_3.setGeometry(QRect(97, 60, 71, 21))
        self.programNameLabel_3.setFont(font)
        self.programNameLabel_3.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	color: rgb(84, 110, 122);\n"
"	border: none;\n"
"}")
        self.programSubnameLabel_3 = QLabel(self.informationFrame_3)
        self.programSubnameLabel_3.setObjectName(u"programSubnameLabel_3")
        self.programSubnameLabel_3.setGeometry(QRect(97, 80, 141, 21))
        self.programSubnameLabel_3.setFont(font)
        self.programSubnameLabel_3.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.typeOfTheWindowLabel_3 = QLabel(self.informationFrame_3)
        self.typeOfTheWindowLabel_3.setObjectName(u"typeOfTheWindowLabel_3")
        self.typeOfTheWindowLabel_3.setGeometry(QRect(56, 130, 311, 101))
        self.typeOfTheWindowLabel_3.setFont(font4)
        self.typeOfTheWindowLabel_3.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.typeOfTheWindowLabel_3.setWordWrap(True)
        self.newPasswordLAbel = QLabel(self.informationFrame_3)
        self.newPasswordLAbel.setObjectName(u"newPasswordLAbel")
        self.newPasswordLAbel.setGeometry(QRect(60, 270, 101, 16))
        self.newPasswordLAbel.setFont(font1)
        self.newPasswordLAbel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.blankForTheNewPassword = QLineEdit(self.informationFrame_3)
        self.blankForTheNewPassword.setObjectName(u"blankForTheNewPassword")
        self.blankForTheNewPassword.setGeometry(QRect(58, 300, 291, 31))
        self.blankForTheNewPassword.setFont(font2)
        self.blankForTheNewPassword.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 7px;\n"
"}")
        self.blankForTheNewPassword.setEchoMode(QLineEdit.Normal)
        self.separatedLine_4 = QFrame(self.informationFrame_3)
        self.separatedLine_4.setObjectName(u"separatedLine_4")
        self.separatedLine_4.setGeometry(QRect(60, 330, 341, 1))
        self.separatedLine_4.setStyleSheet(u"background-color: gray;\n"
"border: none;")
        self.separatedLine_4.setFrameShape(QFrame.HLine)
        self.separatedLine_4.setFrameShadow(QFrame.Sunken)
        self.blankForTheConfirmationOfTheNewPassword = QLineEdit(self.informationFrame_3)
        self.blankForTheConfirmationOfTheNewPassword.setObjectName(u"blankForTheConfirmationOfTheNewPassword")
        self.blankForTheConfirmationOfTheNewPassword.setGeometry(QRect(58, 360, 291, 31))
        self.blankForTheConfirmationOfTheNewPassword.setFont(font2)
        self.blankForTheConfirmationOfTheNewPassword.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 7px;\n"
"}")
        self.blankForTheConfirmationOfTheNewPassword.setEchoMode(QLineEdit.Normal)
        self.separatedLine_5 = QFrame(self.informationFrame_3)
        self.separatedLine_5.setObjectName(u"separatedLine_5")
        self.separatedLine_5.setGeometry(QRect(60, 390, 341, 1))
        self.separatedLine_5.setStyleSheet(u"background-color: gray;\n"
"border: none;")
        self.separatedLine_5.setFrameShape(QFrame.HLine)
        self.separatedLine_5.setFrameShadow(QFrame.Sunken)
        self.updateThePasswordButton = QPushButton(self.informationFrame_3)
        self.updateThePasswordButton.setObjectName(u"updateThePasswordButton")
        self.updateThePasswordButton.setGeometry(QRect(300, 410, 101, 41))
        self.updateThePasswordButton.setFont(font5)
        self.updateThePasswordButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateThePasswordButton.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.newPasswordConfirmationPage)
        LoginWindow.setCentralWidget(self.loginCentralWidget)

        self.retranslateUi(LoginWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.backgroundImage.setText("")
        self.minimizeTheWindowButton.setText("")
        self.closeTheWindowButton.setText("")
        self.programIcon.setText("")
        self.programNameLabel.setText(QCoreApplication.translate("LoginWindow", u"ELFAY", None))
        self.programSubnameLabel.setText(QCoreApplication.translate("LoginWindow", u"PRODUCTION", None))
        self.emailAddressLabel_1.setText(QCoreApplication.translate("LoginWindow", u"E-mail address", None))
        self.forgotPasswordButton.setText(QCoreApplication.translate("LoginWindow", u"Forgot password?", None))
        self.passwordLabel.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.blankForTheAddress.setInputMask("")
        self.blankForTheAddress.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"you@example.com", None))
        self.signInButton.setText(QCoreApplication.translate("LoginWindow", u"Sign In", None))
#if QT_CONFIG(shortcut)
        self.signInButton.setShortcut(QCoreApplication.translate("LoginWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.blankForThePassword.setText("")
        self.blankForThePassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Your password", None))
        self.typeOfTheWindowLabel.setText(QCoreApplication.translate("LoginWindow", u"SIGN IN", None))
        self.noAccountLabel.setText(QCoreApplication.translate("LoginWindow", u"No account?", None))
        self.signUpButton.setText(QCoreApplication.translate("LoginWindow", u"Sign up", None))
        self.showAndHidePasswordButton.setText("")
        self.programIcon_2.setText("")
        self.programNameLabel_2.setText(QCoreApplication.translate("LoginWindow", u"ELFAY", None))
        self.programSubnameLabel_2.setText(QCoreApplication.translate("LoginWindow", u"PRODUCTION", None))
        self.emailAddressLabel_2.setText(QCoreApplication.translate("LoginWindow", u"E-mail address", None))
        self.blankForTheAddress_2.setInputMask("")
        self.blankForTheAddress_2.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter your e-mail address", None))
        self.typeOfTheWindowLabel_2.setText(QCoreApplication.translate("LoginWindow", u"RESTORING PASSWORD", None))
        self.goBackButton.setText(QCoreApplication.translate("LoginWindow", u"Go back", None))
        self.nextStepButton.setText(QCoreApplication.translate("LoginWindow", u"Next step", None))
#if QT_CONFIG(shortcut)
        self.nextStepButton.setShortcut(QCoreApplication.translate("LoginWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.programIcon_3.setText("")
        self.programNameLabel_3.setText(QCoreApplication.translate("LoginWindow", u"ELFAY", None))
        self.programSubnameLabel_3.setText(QCoreApplication.translate("LoginWindow", u"PRODUCTION", None))
        self.typeOfTheWindowLabel_3.setText(QCoreApplication.translate("LoginWindow", u"RESTORING PASSWORD", None))
        self.newPasswordLAbel.setText(QCoreApplication.translate("LoginWindow", u"New password", None))
        self.blankForTheNewPassword.setText("")
        self.blankForTheNewPassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Type your new password", None))
        self.blankForTheConfirmationOfTheNewPassword.setText("")
        self.blankForTheConfirmationOfTheNewPassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Confirm your new password", None))
        self.updateThePasswordButton.setText(QCoreApplication.translate("LoginWindow", u"Update", None))
    # retranslateUi

