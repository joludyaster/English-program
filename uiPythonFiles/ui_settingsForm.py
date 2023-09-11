# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsFormOJNaXS.ui'
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

class Ui_SettingsOfTheProgramWindow(object):
    def setupUi(self, SettingsOfTheProgramWindow):
        if not SettingsOfTheProgramWindow.objectName():
            SettingsOfTheProgramWindow.setObjectName(u"SettingsOfTheProgramWindow")
        SettingsOfTheProgramWindow.resize(936, 618)
        SettingsOfTheProgramWindow.setMinimumSize(QSize(936, 618))
        SettingsOfTheProgramWindow.setMaximumSize(QSize(936, 618))
        self.settingsOfTheProgramCentralWidget = QWidget(SettingsOfTheProgramWindow)
        self.settingsOfTheProgramCentralWidget.setObjectName(u"settingsOfTheProgramCentralWidget")
        self.mainFrame = QFrame(self.settingsOfTheProgramCentralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 936, 618))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.leftMenuFrame = QFrame(self.mainFrame)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setGeometry(QRect(0, 0, 241, 618))
        self.leftMenuFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border: none;\n"
"}")
        self.leftMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.accountSettingFrame = QFrame(self.leftMenuFrame)
        self.accountSettingFrame.setObjectName(u"accountSettingFrame")
        self.accountSettingFrame.setGeometry(QRect(0, 0, 241, 101))
        self.accountSettingFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.accountSettingFrame.setStyleSheet(u"QFrame {\n"
"	border-radius: 0px;\n"
"	border-bottom: 2px solid rgb(240, 240, 240);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QFrame::hover {\n"
"	background-color: rgb(248, 248, 248);\n"
"}")
        self.accountSettingFrame.setFrameShape(QFrame.StyledPanel)
        self.accountSettingFrame.setFrameShadow(QFrame.Raised)
        self.iconOfAccountSettings = QPushButton(self.accountSettingFrame)
        self.iconOfAccountSettings.setObjectName(u"iconOfAccountSettings")
        self.iconOfAccountSettings.setGeometry(QRect(30, 20, 31, 31))
        self.iconOfAccountSettings.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/memberIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconOfAccountSettings.setIcon(icon)
        self.iconOfAccountSettings.setIconSize(QSize(25, 25))
        self.titleOfAccountSettings = QLabel(self.accountSettingFrame)
        self.titleOfAccountSettings.setObjectName(u"titleOfAccountSettings")
        self.titleOfAccountSettings.setGeometry(QRect(70, 28, 71, 16))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(11)
        font.setBold(True)
        self.titleOfAccountSettings.setFont(font)
        self.titleOfAccountSettings.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.descriptionOfAccountSettings = QLabel(self.accountSettingFrame)
        self.descriptionOfAccountSettings.setObjectName(u"descriptionOfAccountSettings")
        self.descriptionOfAccountSettings.setGeometry(QRect(70, 40, 141, 41))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.descriptionOfAccountSettings.setFont(font1)
        self.descriptionOfAccountSettings.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.descriptionOfAccountSettings.setWordWrap(True)
        self.stackedWidget = QStackedWidget(self.mainFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(240, 0, 696, 618))
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}")
        self.accountSettingsPage = QWidget()
        self.accountSettingsPage.setObjectName(u"accountSettingsPage")
        self.accountSettingsPage.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}")
        self.accountAvatar = QLabel(self.accountSettingsPage)
        self.accountAvatar.setObjectName(u"accountAvatar")
        self.accountAvatar.setGeometry(QRect(240, 40, 211, 201))
        self.accountAvatar.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.accountAvatar.setPixmap(QPixmap(u":/maleMemberIcon.png"))
        self.accountAvatar.setScaledContents(True)
        self.accountAvatar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.changeTheAvatarButton = QPushButton(self.accountSettingsPage)
        self.changeTheAvatarButton.setObjectName(u"changeTheAvatarButton")
        self.changeTheAvatarButton.setGeometry(QRect(320, 230, 51, 51))
        self.changeTheAvatarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.changeTheAvatarButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(83, 200, 240);\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(91, 202, 240);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75, 197, 239);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/editSomethingIconBorder_W.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeTheAvatarButton.setIcon(icon1)
        self.changeTheAvatarButton.setIconSize(QSize(20, 20))
        self.separated_line = QFrame(self.accountSettingsPage)
        self.separated_line.setObjectName(u"separated_line")
        self.separated_line.setGeometry(QRect(40, 300, 601, 2))
        self.separated_line.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.separated_line.setFrameShape(QFrame.HLine)
        self.separated_line.setFrameShadow(QFrame.Sunken)
        self.blankForEmailAddress = QLineEdit(self.accountSettingsPage)
        self.blankForEmailAddress.setObjectName(u"blankForEmailAddress")
        self.blankForEmailAddress.setGeometry(QRect(40, 350, 291, 51))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(13)
        font2.setBold(False)
        self.blankForEmailAddress.setFont(font2)
        self.blankForEmailAddress.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.blankForUsername = QLineEdit(self.accountSettingsPage)
        self.blankForUsername.setObjectName(u"blankForUsername")
        self.blankForUsername.setGeometry(QRect(350, 350, 291, 51))
        self.blankForUsername.setFont(font2)
        self.blankForUsername.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.blankForPassword = QLineEdit(self.accountSettingsPage)
        self.blankForPassword.setObjectName(u"blankForPassword")
        self.blankForPassword.setGeometry(QRect(40, 450, 601, 51))
        self.blankForPassword.setFont(font2)
        self.blankForPassword.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.emailLabel = QLabel(self.accountSettingsPage)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(42, 327, 111, 16))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.emailLabel.setFont(font3)
        self.emailLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.usernameLabel = QLabel(self.accountSettingsPage)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(352, 327, 81, 16))
        self.usernameLabel.setFont(font3)
        self.usernameLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.passwordLabel = QLabel(self.accountSettingsPage)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(42, 427, 81, 16))
        self.passwordLabel.setFont(font3)
        self.passwordLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.cancelButton = QPushButton(self.accountSettingsPage)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(330, 540, 151, 41))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.cancelButton.setFont(font4)
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
        self.saveTheSettingsButton = QPushButton(self.accountSettingsPage)
        self.saveTheSettingsButton.setObjectName(u"saveTheSettingsButton")
        self.saveTheSettingsButton.setGeometry(QRect(500, 540, 141, 41))
        self.saveTheSettingsButton.setFont(font4)
        self.saveTheSettingsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveTheSettingsButton.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.accountSettingsPage)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        SettingsOfTheProgramWindow.setCentralWidget(self.settingsOfTheProgramCentralWidget)

        self.retranslateUi(SettingsOfTheProgramWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsOfTheProgramWindow)
    # setupUi

    def retranslateUi(self, SettingsOfTheProgramWindow):
        SettingsOfTheProgramWindow.setWindowTitle(QCoreApplication.translate("SettingsOfTheProgramWindow", u"MainWindow", None))
        self.iconOfAccountSettings.setText("")
        self.titleOfAccountSettings.setText(QCoreApplication.translate("SettingsOfTheProgramWindow", u"Account", None))
        self.descriptionOfAccountSettings.setText(QCoreApplication.translate("SettingsOfTheProgramWindow", u"Change your personal information.", None))
        self.accountAvatar.setText("")
        self.changeTheAvatarButton.setText("")
        self.blankForEmailAddress.setText("")
        self.blankForEmailAddress.setPlaceholderText(QCoreApplication.translate("SettingsOfTheProgramWindow", u"E-mail address", None))
        self.blankForUsername.setText("")
        self.blankForUsername.setPlaceholderText(QCoreApplication.translate("SettingsOfTheProgramWindow", u"Username", None))
        self.blankForPassword.setText("")
        self.blankForPassword.setPlaceholderText(QCoreApplication.translate("SettingsOfTheProgramWindow", u"Password", None))
        self.emailLabel.setText(QCoreApplication.translate("SettingsOfTheProgramWindow", u"E-mail address", None))
        self.usernameLabel.setText(QCoreApplication.translate("SettingsOfTheProgramWindow", u"Username", None))
        self.passwordLabel.setText(QCoreApplication.translate("SettingsOfTheProgramWindow", u"Password", None))
        self.cancelButton.setText(QCoreApplication.translate("SettingsOfTheProgramWindow", u"Cancel", None))
        self.saveTheSettingsButton.setText(QCoreApplication.translate("SettingsOfTheProgramWindow", u"Save", None))
    # retranslateUi

