# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainFormaIiWIR.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1221, 720)
        MainWindow.setMinimumSize(QSize(1221, 720))
        MainWindow.setMaximumSize(QSize(1221, 720))
        MainWindow.setStyleSheet(u"")
        self.mainCentralWidget = QWidget(MainWindow)
        self.mainCentralWidget.setObjectName(u"mainCentralWidget")
        self.mainCentralWidget.setStyleSheet(u"")
        self.mainFrame = QFrame(self.mainCentralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setEnabled(True)
        self.mainFrame.setGeometry(QRect(0, 0, 1221, 720))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.frameOfOtherFrames = QFrame(self.mainFrame)
        self.frameOfOtherFrames.setObjectName(u"frameOfOtherFrames")
        self.frameOfOtherFrames.setGeometry(QRect(0, 90, 1221, 631))
        self.frameOfOtherFrames.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.frameOfOtherFrames.setFrameShape(QFrame.NoFrame)
        self.frameOfOtherFrames.setFrameShadow(QFrame.Raised)
        self.displayFrame_2 = QFrame(self.frameOfOtherFrames)
        self.displayFrame_2.setObjectName(u"displayFrame_2")
        self.displayFrame_2.setGeometry(QRect(850, 340, 331, 261))
        self.displayFrame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.displayFrame_2.setFrameShape(QFrame.NoFrame)
        self.displayFrame_2.setFrameShadow(QFrame.Raised)
        self.searchLine = QLineEdit(self.frameOfOtherFrames)
        self.searchLine.setObjectName(u"searchLine")
        self.searchLine.setGeometry(QRect(850, 40, 331, 41))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(11)
        font.setBold(False)
        self.searchLine.setFont(font)
        self.searchLine.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-radius: 15px;\n"
"}")
        self.stackedWidget = QStackedWidget(self.frameOfOtherFrames)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(370, 100, 471, 501))
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}")
        self.frameForPage_1 = QFrame(self.page_1)
        self.frameForPage_1.setObjectName(u"frameForPage_1")
        self.frameForPage_1.setEnabled(True)
        self.frameForPage_1.setGeometry(QRect(0, 0, 471, 501))
        self.frameForPage_1.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	border: none;\n"
"}")
        self.frameForPage_1.setFrameShape(QFrame.NoFrame)
        self.frameForPage_1.setFrameShadow(QFrame.Raised)
        self.buttonsWidget = QWidget(self.frameForPage_1)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.buttonsWidget.setGeometry(QRect(175, 20, 121, 61))
        self.buttonsWidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")
        self.refreshTheListOfVocabularies = QPushButton(self.buttonsWidget)
        self.refreshTheListOfVocabularies.setObjectName(u"refreshTheListOfVocabularies")
        self.refreshTheListOfVocabularies.setGeometry(QRect(70, 15, 31, 31))
        font1 = QFont()
        font1.setFamilies([u"Montserrat SemiBold"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.refreshTheListOfVocabularies.setFont(font1)
        self.refreshTheListOfVocabularies.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshTheListOfVocabularies.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(255, 103, 103);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(255, 123, 123);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 91, 91);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/refreshIcon_W.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshTheListOfVocabularies.setIcon(icon1)
        self.refreshTheListOfVocabularies.setIconSize(QSize(16, 16))
        self.addANewDictionaryButton = QPushButton(self.buttonsWidget)
        self.addANewDictionaryButton.setObjectName(u"addANewDictionaryButton")
        self.addANewDictionaryButton.setGeometry(QRect(20, 15, 31, 31))
        self.addANewDictionaryButton.setFont(font1)
        self.addANewDictionaryButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addANewDictionaryButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 167, 255);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(56, 179, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(34, 162, 248);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/addSomethingIcon_W.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addANewDictionaryButton.setIcon(icon2)
        self.addANewDictionaryButton.setIconSize(QSize(13, 13))
        self.stackedWidget.addWidget(self.page_1)
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.dashboardFrame = QFrame(self.page_0)
        self.dashboardFrame.setObjectName(u"dashboardFrame")
        self.dashboardFrame.setGeometry(QRect(0, 0, 471, 501))
        self.dashboardFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}")
        self.dashboardFrame.setFrameShape(QFrame.StyledPanel)
        self.dashboardFrame.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.page_0)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.warningFrame = QFrame(self.page_2)
        self.warningFrame.setObjectName(u"warningFrame")
        self.warningFrame.setGeometry(QRect(0, 0, 471, 501))
        self.warningFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.warningFrame.setFrameShape(QFrame.NoFrame)
        self.warningFrame.setFrameShadow(QFrame.Raised)
        self.cautionLabel = QLabel(self.warningFrame)
        self.cautionLabel.setObjectName(u"cautionLabel")
        self.cautionLabel.setGeometry(QRect(80, 200, 321, 31))
        font2 = QFont()
        font2.setFamilies([u"Montserrat SemiBold"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.cautionLabel.setFont(font2)
        self.icon = QPushButton(self.warningFrame)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(180, 100, 91, 91))
        self.icon.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/warningIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon3)
        self.icon.setIconSize(QSize(80, 80))
        self.explanationLabel = QLabel(self.warningFrame)
        self.explanationLabel.setObjectName(u"explanationLabel")
        self.explanationLabel.setGeometry(QRect(80, 230, 311, 21))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.explanationLabel.setFont(font3)
        self.stackedWidget.addWidget(self.page_2)
        self.displayStackedWidget = QStackedWidget(self.frameOfOtherFrames)
        self.displayStackedWidget.setObjectName(u"displayStackedWidget")
        self.displayStackedWidget.setGeometry(QRect(850, 100, 331, 231))
        self.displayStackedWidget.setStyleSheet(u"QStackedWidget {\n"
"	background-color: none;\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}")
        self.firstPage = QWidget()
        self.firstPage.setObjectName(u"firstPage")
        self.firstPage.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}")
        self.displayStackedWidget.addWidget(self.firstPage)
        self.secondPage = QWidget()
        self.secondPage.setObjectName(u"secondPage")
        self.secondPage.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}")
        self.displayStackedWidget.addWidget(self.secondPage)
        self.thirdPage = QWidget()
        self.thirdPage.setObjectName(u"thirdPage")
        self.thirdPage.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}")
        self.displayStackedWidget.addWidget(self.thirdPage)
        self.fourthPage = QWidget()
        self.fourthPage.setObjectName(u"fourthPage")
        self.fourthPage.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}")
        self.displayStackedWidget.addWidget(self.fourthPage)
        self.fifthPage = QWidget()
        self.fifthPage.setObjectName(u"fifthPage")
        self.fifthPage.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}")
        self.displayStackedWidget.addWidget(self.fifthPage)
        self.backgroundImage = QLabel(self.mainFrame)
        self.backgroundImage.setObjectName(u"backgroundImage")
        self.backgroundImage.setGeometry(QRect(0, 0, 1221, 91))
        self.backgroundImage.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.backgroundImage.setPixmap(QPixmap(u":/backgroundImage.jpg"))
        self.backgroundImage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.userFrame = QFrame(self.mainFrame)
        self.userFrame.setObjectName(u"userFrame")
        self.userFrame.setGeometry(QRect(40, 30, 291, 661))
        self.userFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	border: none;\n"
"}")
        self.userFrame.setFrameShape(QFrame.NoFrame)
        self.userFrame.setFrameShadow(QFrame.Raised)
        self.nameLabel_2 = QLabel(self.userFrame)
        self.nameLabel_2.setObjectName(u"nameLabel_2")
        self.nameLabel_2.setGeometry(QRect(92, 45, 121, 16))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.nameLabel_2.setFont(font4)
        self.nameLabel_2.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.nameLabel_1 = QLabel(self.userFrame)
        self.nameLabel_1.setObjectName(u"nameLabel_1")
        self.nameLabel_1.setGeometry(QRect(92, 30, 61, 16))
        self.nameLabel_1.setFont(font4)
        self.nameLabel_1.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	color: rgb(84, 110, 122);\n"
"	border: none;\n"
"}")
        self.iconOfTheProgram = QPushButton(self.userFrame)
        self.iconOfTheProgram.setObjectName(u"iconOfTheProgram")
        self.iconOfTheProgram.setGeometry(QRect(60, 30, 31, 31))
        self.iconOfTheProgram.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/programIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconOfTheProgram.setIcon(icon4)
        self.iconOfTheProgram.setIconSize(QSize(35, 35))
        self.userLabel_1 = QLabel(self.userFrame)
        self.userLabel_1.setObjectName(u"userLabel_1")
        self.userLabel_1.setGeometry(QRect(104, 220, 81, 16))
        self.userLabel_1.setFont(font)
        self.userLabel_1.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.userLabel_1.setWordWrap(True)
        self.username = QLabel(self.userFrame)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(34, 240, 221, 21))
        font5 = QFont()
        font5.setFamilies([u"Montserrat"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.username.setFont(font5)
        self.username.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.username.setAlignment(Qt.AlignCenter)
        self.englishLessonsButton = QPushButton(self.userFrame)
        self.englishLessonsButton.setObjectName(u"englishLessonsButton")
        self.englishLessonsButton.setGeometry(QRect(90, 310, 51, 51))
        self.englishLessonsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.englishLessonsButton.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/englishLessonsIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.englishLessonsButton.setIcon(icon5)
        self.englishLessonsButton.setIconSize(QSize(35, 30))
        self.englishDictionariesButton = QPushButton(self.userFrame)
        self.englishDictionariesButton.setObjectName(u"englishDictionariesButton")
        self.englishDictionariesButton.setGeometry(QRect(150, 310, 51, 51))
        self.englishDictionariesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.englishDictionariesButton.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/wordsIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.englishDictionariesButton.setIcon(icon6)
        self.englishDictionariesButton.setIconSize(QSize(35, 35))
        self.settingsOfTheProgramButton = QPushButton(self.userFrame)
        self.settingsOfTheProgramButton.setObjectName(u"settingsOfTheProgramButton")
        self.settingsOfTheProgramButton.setGeometry(QRect(90, 370, 51, 51))
        self.settingsOfTheProgramButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsOfTheProgramButton.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/settingsIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsOfTheProgramButton.setIcon(icon7)
        self.settingsOfTheProgramButton.setIconSize(QSize(35, 35))
        self.signOutButton = QPushButton(self.userFrame)
        self.signOutButton.setObjectName(u"signOutButton")
        self.signOutButton.setGeometry(QRect(125, 570, 51, 51))
        self.signOutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signOutButton.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius: 7px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/exitIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signOutButton.setIcon(icon8)
        self.signOutButton.setIconSize(QSize(35, 35))
        self.userIcon = QLabel(self.userFrame)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setGeometry(QRect(90, 100, 101, 101))
        self.userIcon.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.userIcon.setPixmap(QPixmap(u":/programIcon.png"))
        self.userIcon.setScaledContents(True)
        self.userIcon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.closeTheWindowButton = QPushButton(self.mainFrame)
        self.closeTheWindowButton.setObjectName(u"closeTheWindowButton")
        self.closeTheWindowButton.setGeometry(QRect(1140, 25, 41, 41))
        self.closeTheWindowButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeTheWindowButton.setStyleSheet(u"QPushButton {\n"
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
        icon9 = QIcon()
        icon9.addFile(u":/closeSomethingIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeTheWindowButton.setIcon(icon9)
        self.closeTheWindowButton.setIconSize(QSize(10, 10))
        self.minimizeTheWindowButton = QPushButton(self.mainFrame)
        self.minimizeTheWindowButton.setObjectName(u"minimizeTheWindowButton")
        self.minimizeTheWindowButton.setGeometry(QRect(1080, 25, 41, 41))
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
        icon10 = QIcon()
        icon10.addFile(u":/minimizeWindowIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeTheWindowButton.setIcon(icon10)
        self.minimizeTheWindowButton.setIconSize(QSize(10, 16))
        MainWindow.setCentralWidget(self.mainCentralWidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search anything...", None))
#if QT_CONFIG(tooltip)
        self.refreshTheListOfVocabularies.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-style:italic;\">ADD A NEW DICTIONARY.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.refreshTheListOfVocabularies.setText("")
#if QT_CONFIG(tooltip)
        self.addANewDictionaryButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-style:italic;\">ADD A NEW DICTIONARY.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.addANewDictionaryButton.setText("")
        self.cautionLabel.setText(QCoreApplication.translate("MainWindow", u"Temporary unavailable", None))
        self.icon.setText("")
        self.explanationLabel.setText(QCoreApplication.translate("MainWindow", u"We are so sorry for the inconvieniences", None))
        self.backgroundImage.setText("")
        self.nameLabel_2.setText(QCoreApplication.translate("MainWindow", u"PRODUCTION", None))
        self.nameLabel_1.setText(QCoreApplication.translate("MainWindow", u"ELFAY", None))
        self.iconOfTheProgram.setText("")
        self.userLabel_1.setText(QCoreApplication.translate("MainWindow", u"Welcome, joludyaster", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"ergmrtkohjrthjotrihjtrh", None))
        self.englishLessonsButton.setText("")
        self.englishDictionariesButton.setText("")
        self.settingsOfTheProgramButton.setText("")
        self.signOutButton.setText("")
        self.userIcon.setText("")
        self.closeTheWindowButton.setText("")
        self.minimizeTheWindowButton.setText("")
    # retranslateUi

