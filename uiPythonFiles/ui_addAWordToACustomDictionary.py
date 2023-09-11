# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addAWordToACustomDictionaryeMXoIJ.ui'
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
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
import icons.icons_rc

class Ui_WordInDictionaryMainWindow(object):
    def setupUi(self, WordInDictionaryMainWindow):
        if not WordInDictionaryMainWindow.objectName():
            WordInDictionaryMainWindow.setObjectName(u"WordInDictionaryMainWindow")
        WordInDictionaryMainWindow.resize(643, 390)
        WordInDictionaryMainWindow.setMinimumSize(QSize(643, 390))
        WordInDictionaryMainWindow.setMaximumSize(QSize(643, 390))
        self.WordInDictionaryCentralWidget = QWidget(WordInDictionaryMainWindow)
        self.WordInDictionaryCentralWidget.setObjectName(u"WordInDictionaryCentralWidget")
        self.mainFrame = QFrame(self.WordInDictionaryCentralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 643, 390))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.mainFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, -1, 631, 391))
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: none;\n"
"	width: 8px;\n"
"	border-radius: 4px;\n"
"	margin: 20px 0 20px 0;\n"
"}\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(180, 180, 180);\n"
"	min-height: 50px;\n"
"	border-radius: 4px;\n"
"	margin: 0;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(160, 160, 160);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	width: 0px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	width: 0px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background-color: none;\n"
""
                        "}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background-color: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -373, 623, 1250))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.displayFrame = QFrame(self.scrollAreaWidgetContents)
        self.displayFrame.setObjectName(u"displayFrame")
        self.displayFrame.setMinimumSize(QSize(0, 1250))
        self.displayFrame.setFrameShape(QFrame.StyledPanel)
        self.displayFrame.setFrameShadow(QFrame.Raised)
        self.wordLineEdit = QLineEdit(self.displayFrame)
        self.wordLineEdit.setObjectName(u"wordLineEdit")
        self.wordLineEdit.setGeometry(QRect(50, 40, 221, 51))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(13)
        font.setBold(False)
        self.wordLineEdit.setFont(font)
        self.wordLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.buttonToSwapWords = QPushButton(self.displayFrame)
        self.buttonToSwapWords.setObjectName(u"buttonToSwapWords")
        self.buttonToSwapWords.setGeometry(QRect(290, 45, 41, 41))
        self.buttonToSwapWords.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonToSwapWords.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(240, 240, 240, 220);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(240, 240, 240, 240);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/exchangeIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonToSwapWords.setIcon(icon)
        self.buttonToSwapWords.setIconSize(QSize(18, 18))
        self.translationLineEdit = QLineEdit(self.displayFrame)
        self.translationLineEdit.setObjectName(u"translationLineEdit")
        self.translationLineEdit.setGeometry(QRect(350, 40, 221, 51))
        self.translationLineEdit.setFont(font)
        self.translationLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.separatedLine_1 = QLabel(self.displayFrame)
        self.separatedLine_1.setObjectName(u"separatedLine_1")
        self.separatedLine_1.setGeometry(QRect(50, 120, 521, 1))
        self.separatedLine_1.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.additionalTranslationLineEdit = QLineEdit(self.displayFrame)
        self.additionalTranslationLineEdit.setObjectName(u"additionalTranslationLineEdit")
        self.additionalTranslationLineEdit.setGeometry(QRect(50, 150, 521, 51))
        self.additionalTranslationLineEdit.setFont(font)
        self.additionalTranslationLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.tagsLineEdit = QLineEdit(self.displayFrame)
        self.tagsLineEdit.setObjectName(u"tagsLineEdit")
        self.tagsLineEdit.setGeometry(QRect(50, 220, 521, 51))
        self.tagsLineEdit.setFont(font)
        self.tagsLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.separatedLine_2 = QLabel(self.displayFrame)
        self.separatedLine_2.setObjectName(u"separatedLine_2")
        self.separatedLine_2.setGeometry(QRect(50, 300, 521, 1))
        self.separatedLine_2.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.examplesLineEdit = QLineEdit(self.displayFrame)
        self.examplesLineEdit.setObjectName(u"examplesLineEdit")
        self.examplesLineEdit.setGeometry(QRect(50, 360, 521, 51))
        self.examplesLineEdit.setFont(font)
        self.examplesLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.examplesLabel = QLabel(self.displayFrame)
        self.examplesLabel.setObjectName(u"examplesLabel")
        self.examplesLabel.setGeometry(QRect(50, 330, 191, 16))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.examplesLabel.setFont(font1)
        self.examplesLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.translationOfTheExamplesLineEdit = QLineEdit(self.displayFrame)
        self.translationOfTheExamplesLineEdit.setObjectName(u"translationOfTheExamplesLineEdit")
        self.translationOfTheExamplesLineEdit.setGeometry(QRect(50, 430, 521, 51))
        self.translationOfTheExamplesLineEdit.setFont(font)
        self.translationOfTheExamplesLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.separatedLine_3 = QLabel(self.displayFrame)
        self.separatedLine_3.setObjectName(u"separatedLine_3")
        self.separatedLine_3.setGeometry(QRect(50, 510, 521, 1))
        self.separatedLine_3.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.photoOfTheWord = QLabel(self.displayFrame)
        self.photoOfTheWord.setObjectName(u"photoOfTheWord")
        self.photoOfTheWord.setGeometry(QRect(50, 540, 81, 81))
        self.photoOfTheWord.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.photoOfTheWord.setPixmap(QPixmap(u":/programIcon.png"))
        self.photoOfTheWord.setScaledContents(True)
        self.photoOfTheWord.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.changePhotoOfTheWord = QPushButton(self.displayFrame)
        self.changePhotoOfTheWord.setObjectName(u"changePhotoOfTheWord")
        self.changePhotoOfTheWord.setGeometry(QRect(115, 605, 31, 31))
        self.changePhotoOfTheWord.setCursor(QCursor(Qt.PointingHandCursor))
        self.changePhotoOfTheWord.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(83, 200, 240);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
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
        self.changePhotoOfTheWord.setIcon(icon1)
        self.changePhotoOfTheWord.setIconSize(QSize(16, 16))
        self.separatedLine_4 = QLabel(self.displayFrame)
        self.separatedLine_4.setObjectName(u"separatedLine_4")
        self.separatedLine_4.setGeometry(QRect(50, 670, 521, 1))
        self.separatedLine_4.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.color_3 = QPushButton(self.displayFrame)
        self.color_3.setObjectName(u"color_3")
        self.color_3.setGeometry(QRect(170, 700, 31, 31))
        self.color_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 187, 205);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 187, 205, 100);\n"
"}")
        self.color_2 = QPushButton(self.displayFrame)
        self.color_2.setObjectName(u"color_2")
        self.color_2.setGeometry(QRect(120, 700, 31, 31))
        self.color_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 194, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(80, 194, 255, 100);\n"
"}")
        self.color_1 = QPushButton(self.displayFrame)
        self.color_1.setObjectName(u"color_1")
        self.color_1.setGeometry(QRect(70, 700, 31, 31))
        self.color_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 0, 123);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 0, 123, 100);\n"
"}")
        self.color_4 = QPushButton(self.displayFrame)
        self.color_4.setObjectName(u"color_4")
        self.color_4.setGeometry(QRect(220, 700, 31, 31))
        self.color_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(158, 255, 215);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(158, 255, 215, 100);\n"
"}")
        self.color_5 = QPushButton(self.displayFrame)
        self.color_5.setObjectName(u"color_5")
        self.color_5.setGeometry(QRect(270, 700, 31, 31))
        self.color_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(169, 203, 183);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(169, 203, 183, 100);\n"
"}")
        self.color_10 = QPushButton(self.displayFrame)
        self.color_10.setObjectName(u"color_10")
        self.color_10.setGeometry(QRect(520, 700, 31, 31))
        self.color_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_10.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(228, 225, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(228, 225, 255, 100);\n"
"}")
        self.color_9 = QPushButton(self.displayFrame)
        self.color_9.setObjectName(u"color_9")
        self.color_9.setGeometry(QRect(470, 700, 31, 31))
        self.color_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_9.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 255, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(170, 255, 0, 100);\n"
"}")
        self.color_6 = QPushButton(self.displayFrame)
        self.color_6.setObjectName(u"color_6")
        self.color_6.setGeometry(QRect(320, 700, 31, 31))
        self.color_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(205, 53, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(205, 53, 255, 100);\n"
"}")
        self.color_7 = QPushButton(self.displayFrame)
        self.color_7.setObjectName(u"color_7")
        self.color_7.setGeometry(QRect(370, 700, 31, 31))
        self.color_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_7.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 201, 64);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 201, 64, 100);\n"
"}")
        self.color_8 = QPushButton(self.displayFrame)
        self.color_8.setObjectName(u"color_8")
        self.color_8.setGeometry(QRect(420, 700, 31, 31))
        self.color_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_8.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 32, 80);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 32, 80, 100);\n"
"}")
        self.color_15 = QPushButton(self.displayFrame)
        self.color_15.setObjectName(u"color_15")
        self.color_15.setGeometry(QRect(270, 750, 31, 31))
        self.color_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_15.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(235, 255, 52);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(235, 255, 52, 100);\n"
"}")
        self.color_14 = QPushButton(self.displayFrame)
        self.color_14.setObjectName(u"color_14")
        self.color_14.setGeometry(QRect(220, 750, 31, 31))
        self.color_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_14.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 107, 235);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 107, 235, 100);\n"
"}")
        self.color_19 = QPushButton(self.displayFrame)
        self.color_19.setObjectName(u"color_19")
        self.color_19.setGeometry(QRect(470, 750, 31, 31))
        self.color_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_19.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(170, 0, 0, 100);\n"
"}")
        self.color_18 = QPushButton(self.displayFrame)
        self.color_18.setObjectName(u"color_18")
        self.color_18.setGeometry(QRect(420, 750, 31, 31))
        self.color_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_18.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 85, 127);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(170, 85, 127, 100);\n"
"}")
        self.color_16 = QPushButton(self.displayFrame)
        self.color_16.setObjectName(u"color_16")
        self.color_16.setGeometry(QRect(320, 750, 31, 31))
        self.color_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_16.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(85, 85, 127);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.color_11 = QPushButton(self.displayFrame)
        self.color_11.setObjectName(u"color_11")
        self.color_11.setGeometry(QRect(70, 750, 31, 31))
        self.color_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_11.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(2, 255, 61);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(2, 255, 61, 100);\n"
"}")
        self.color_17 = QPushButton(self.displayFrame)
        self.color_17.setObjectName(u"color_17")
        self.color_17.setGeometry(QRect(370, 750, 31, 31))
        self.color_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_17.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(85, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 0, 0, 100);\n"
"}")
        self.color_12 = QPushButton(self.displayFrame)
        self.color_12.setObjectName(u"color_12")
        self.color_12.setGeometry(QRect(120, 750, 31, 31))
        self.color_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_12.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(179, 58, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(179, 58, 255, 100);\n"
"}")
        self.color_13 = QPushButton(self.displayFrame)
        self.color_13.setObjectName(u"color_13")
        self.color_13.setGeometry(QRect(170, 750, 31, 31))
        self.color_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_13.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(106, 0, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(106, 0, 255, 100);\n"
"}")
        self.changeColorButton = QPushButton(self.displayFrame)
        self.changeColorButton.setObjectName(u"changeColorButton")
        self.changeColorButton.setGeometry(QRect(520, 750, 31, 31))
        self.changeColorButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.changeColorButton.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/chooseTheColorIconBorder_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeColorButton.setIcon(icon2)
        self.changeColorButton.setIconSize(QSize(25, 25))
        self.chosenColorLabel = QLabel(self.displayFrame)
        self.chosenColorLabel.setObjectName(u"chosenColorLabel")
        self.chosenColorLabel.setGeometry(QRect(200, 820, 121, 16))
        self.chosenColorLabel.setFont(font)
        self.chosenColorLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.chosenColor = QPushButton(self.displayFrame)
        self.chosenColor.setObjectName(u"chosenColor")
        self.chosenColor.setGeometry(QRect(330, 813, 31, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.chosenColor.setFont(font2)
        self.chosenColor.setCursor(QCursor(Qt.PointingHandCursor))
        self.chosenColor.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"}")
        self.separatedLine_5 = QLabel(self.displayFrame)
        self.separatedLine_5.setObjectName(u"separatedLine_5")
        self.separatedLine_5.setGeometry(QRect(50, 900, 521, 1))
        self.separatedLine_5.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.statusLabel = QLabel(self.displayFrame)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(50, 930, 51, 16))
        self.statusLabel.setFont(font1)
        self.statusLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.separatedLine_6 = QLabel(self.displayFrame)
        self.separatedLine_6.setObjectName(u"separatedLine_6")
        self.separatedLine_6.setGeometry(QRect(50, 1140, 521, 1))
        self.separatedLine_6.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.saveAndAddAWord = QPushButton(self.displayFrame)
        self.saveAndAddAWord.setObjectName(u"saveAndAddAWord")
        self.saveAndAddAWord.setGeometry(QRect(430, 1170, 141, 41))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.saveAndAddAWord.setFont(font3)
        self.saveAndAddAWord.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveAndAddAWord.setStyleSheet(u"QPushButton {\n"
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
        self.cancelButton = QPushButton(self.displayFrame)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(270, 1170, 151, 41))
        self.cancelButton.setFont(font3)
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
        self.processStatusButton = QPushButton(self.displayFrame)
        self.processStatusButton.setObjectName(u"processStatusButton")
        self.processStatusButton.setGeometry(QRect(50, 970, 181, 51))
        font4 = QFont()
        font4.setFamilies([u"Montserrat SemiBold"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.processStatusButton.setFont(font4)
        self.processStatusButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.processStatusButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(101, 255, 29);\n"
"	border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(101, 255, 29, 220);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/processIcon_W.png", QSize(), QIcon.Normal, QIcon.Off)
        self.processStatusButton.setIcon(icon3)
        self.processStatusButton.setIconSize(QSize(25, 25))
        self.processStatusButton.setCheckable(False)
        self.processStatusButton.setFlat(False)
        self.learnedStatusButton = QPushButton(self.displayFrame)
        self.learnedStatusButton.setObjectName(u"learnedStatusButton")
        self.learnedStatusButton.setGeometry(QRect(250, 970, 171, 51))
        self.learnedStatusButton.setFont(font4)
        self.learnedStatusButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.learnedStatusButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 167, 255);\n"
"	border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 179, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/learnedIcon_W.png", QSize(), QIcon.Normal, QIcon.Off)
        self.learnedStatusButton.setIcon(icon4)
        self.learnedStatusButton.setIconSize(QSize(20, 20))
        self.learnedStatusButton.setCheckable(False)
        self.learnedStatusButton.setFlat(False)
        self.importantStatusButton = QPushButton(self.displayFrame)
        self.importantStatusButton.setObjectName(u"importantStatusButton")
        self.importantStatusButton.setGeometry(QRect(50, 1040, 181, 51))
        self.importantStatusButton.setFont(font4)
        self.importantStatusButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.importantStatusButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(255, 192, 32);\n"
"	border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 192, 32, 220);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/importantIcon_W.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importantStatusButton.setIcon(icon5)
        self.importantStatusButton.setIconSize(QSize(25, 25))
        self.importantStatusButton.setCheckable(False)
        self.importantStatusButton.setFlat(False)

        self.verticalLayout.addWidget(self.displayFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        WordInDictionaryMainWindow.setCentralWidget(self.WordInDictionaryCentralWidget)

        self.retranslateUi(WordInDictionaryMainWindow)

        QMetaObject.connectSlotsByName(WordInDictionaryMainWindow)
    # setupUi

    def retranslateUi(self, WordInDictionaryMainWindow):
        WordInDictionaryMainWindow.setWindowTitle(QCoreApplication.translate("WordInDictionaryMainWindow", u"MainWindow", None))
        self.wordLineEdit.setPlaceholderText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Word", None))
        self.buttonToSwapWords.setText("")
        self.translationLineEdit.setPlaceholderText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Translation", None))
        self.separatedLine_1.setText("")
        self.additionalTranslationLineEdit.setPlaceholderText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Additional translation", None))
        self.tagsLineEdit.setPlaceholderText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Tags", None))
        self.separatedLine_2.setText("")
        self.examplesLineEdit.setPlaceholderText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Examples", None))
        self.examplesLabel.setText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Examples of using the word", None))
        self.translationOfTheExamplesLineEdit.setPlaceholderText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Translation", None))
        self.separatedLine_3.setText("")
        self.photoOfTheWord.setText("")
        self.changePhotoOfTheWord.setText("")
        self.separatedLine_4.setText("")
        self.color_3.setText("")
        self.color_2.setText("")
        self.color_1.setText("")
        self.color_4.setText("")
        self.color_5.setText("")
        self.color_10.setText("")
        self.color_9.setText("")
        self.color_6.setText("")
        self.color_7.setText("")
        self.color_8.setText("")
        self.color_15.setText("")
        self.color_14.setText("")
        self.color_19.setText("")
        self.color_18.setText("")
        self.color_16.setText("")
        self.color_11.setText("")
        self.color_17.setText("")
        self.color_12.setText("")
        self.color_13.setText("")
        self.changeColorButton.setText("")
        self.chosenColorLabel.setText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Chosen color:", None))
        self.chosenColor.setText("")
        self.separatedLine_5.setText("")
        self.statusLabel.setText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Status", None))
        self.separatedLine_6.setText("")
        self.saveAndAddAWord.setText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Create", None))
        self.cancelButton.setText(QCoreApplication.translate("WordInDictionaryMainWindow", u"Cancel", None))
        self.processStatusButton.setText(QCoreApplication.translate("WordInDictionaryMainWindow", u"IN PROCESS", None))
        self.learnedStatusButton.setText(QCoreApplication.translate("WordInDictionaryMainWindow", u"LEARNED", None))
        self.importantStatusButton.setText(QCoreApplication.translate("WordInDictionaryMainWindow", u"IMPORTANT", None))
    # retranslateUi

