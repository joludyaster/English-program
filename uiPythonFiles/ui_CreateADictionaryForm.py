# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createADictionaryFormXvUlyM.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import icons.icons_rc

class Ui_CreateADictionaryWindow(object):
    def setupUi(self, CreateADictionaryWindow):
        if not CreateADictionaryWindow.objectName():
            CreateADictionaryWindow.setObjectName(u"CreateADictionaryWindow")
        CreateADictionaryWindow.resize(871, 541)
        CreateADictionaryWindow.setMinimumSize(QSize(0, 0))
        CreateADictionaryWindow.setMaximumSize(QSize(16777215, 16777215))
        self.createADictionaryCentralWidget = QWidget(CreateADictionaryWindow)
        self.createADictionaryCentralWidget.setObjectName(u"createADictionaryCentralWidget")
        self.mainWidget = QWidget(self.createADictionaryCentralWidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setGeometry(QRect(0, 0, 871, 541))
        self.mainWidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.saveAndCreateADictionaryButton = QPushButton(self.mainWidget)
        self.saveAndCreateADictionaryButton.setObjectName(u"saveAndCreateADictionaryButton")
        self.saveAndCreateADictionaryButton.setGeometry(QRect(640, 470, 161, 41))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(13)
        font.setBold(True)
        self.saveAndCreateADictionaryButton.setFont(font)
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
        self.cancelButton = QPushButton(self.mainWidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(470, 470, 161, 41))
        self.cancelButton.setFont(font)
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
"	border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(202, 202, 202);\n"
"	border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.nameOfTheDictionaryLabel = QLabel(self.mainWidget)
        self.nameOfTheDictionaryLabel.setObjectName(u"nameOfTheDictionaryLabel")
        self.nameOfTheDictionaryLabel.setGeometry(QRect(60, 26, 181, 16))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.nameOfTheDictionaryLabel.setFont(font1)
        self.nameOfTheDictionaryLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.nameOfTheDictionaryLabel.setWordWrap(True)
        self.blankForTheName = QLineEdit(self.mainWidget)
        self.blankForTheName.setObjectName(u"blankForTheName")
        self.blankForTheName.setGeometry(QRect(60, 50, 281, 51))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(13)
        font2.setBold(False)
        self.blankForTheName.setFont(font2)
        self.blankForTheName.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.blankForTheName.setEchoMode(QLineEdit.Normal)
        self.blankForTheName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.descriptionLabel = QLabel(self.mainWidget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(380, 26, 91, 16))
        self.descriptionLabel.setFont(font1)
        self.descriptionLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.descriptionLabel.setWordWrap(True)
        self.separatedLine_4 = QLabel(self.mainWidget)
        self.separatedLine_4.setObjectName(u"separatedLine_4")
        self.separatedLine_4.setGeometry(QRect(60, 130, 740, 1))
        self.separatedLine_4.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.color_8 = QPushButton(self.mainWidget)
        self.color_8.setObjectName(u"color_8")
        self.color_8.setGeometry(QRect(540, 160, 31, 31))
        self.color_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_8.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 32, 80);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 32, 80, 100);\n"
"}")
        self.color_17 = QPushButton(self.mainWidget)
        self.color_17.setObjectName(u"color_17")
        self.color_17.setGeometry(QRect(490, 210, 31, 31))
        self.color_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_17.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(85, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 0, 0, 100);\n"
"}")
        self.color_5 = QPushButton(self.mainWidget)
        self.color_5.setObjectName(u"color_5")
        self.color_5.setGeometry(QRect(390, 160, 31, 31))
        self.color_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(169, 203, 183);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(169, 203, 183, 100);\n"
"}")
        self.chosenColor = QPushButton(self.mainWidget)
        self.chosenColor.setObjectName(u"chosenColor")
        self.chosenColor.setGeometry(QRect(450, 273, 31, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.chosenColor.setFont(font3)
        self.chosenColor.setCursor(QCursor(Qt.PointingHandCursor))
        self.chosenColor.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"}\n"
"")
        self.color_13 = QPushButton(self.mainWidget)
        self.color_13.setObjectName(u"color_13")
        self.color_13.setGeometry(QRect(290, 210, 31, 31))
        self.color_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_13.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(106, 0, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(106, 0, 255, 100);\n"
"}")
        self.color_4 = QPushButton(self.mainWidget)
        self.color_4.setObjectName(u"color_4")
        self.color_4.setGeometry(QRect(340, 160, 31, 31))
        self.color_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(158, 255, 215);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(158, 255, 215, 100);\n"
"}")
        self.changeColorButton = QPushButton(self.mainWidget)
        self.changeColorButton.setObjectName(u"changeColorButton")
        self.changeColorButton.setGeometry(QRect(640, 210, 31, 31))
        self.changeColorButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.changeColorButton.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/chooseTheColorIconBorder_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeColorButton.setIcon(icon)
        self.changeColorButton.setIconSize(QSize(25, 25))
        self.color_15 = QPushButton(self.mainWidget)
        self.color_15.setObjectName(u"color_15")
        self.color_15.setGeometry(QRect(390, 210, 31, 31))
        self.color_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_15.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(235, 255, 52);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(235, 255, 52, 100);\n"
"}")
        self.color_14 = QPushButton(self.mainWidget)
        self.color_14.setObjectName(u"color_14")
        self.color_14.setGeometry(QRect(340, 210, 31, 31))
        self.color_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_14.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 107, 235);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 107, 235, 100);\n"
"}")
        self.color_2 = QPushButton(self.mainWidget)
        self.color_2.setObjectName(u"color_2")
        self.color_2.setGeometry(QRect(240, 160, 31, 31))
        self.color_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 194, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(80, 194, 255, 100);\n"
"}")
        self.color_1 = QPushButton(self.mainWidget)
        self.color_1.setObjectName(u"color_1")
        self.color_1.setGeometry(QRect(190, 160, 31, 31))
        self.color_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 0, 123);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 0, 123, 100);\n"
"}")
        self.color_12 = QPushButton(self.mainWidget)
        self.color_12.setObjectName(u"color_12")
        self.color_12.setGeometry(QRect(240, 210, 31, 31))
        self.color_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_12.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(179, 58, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(179, 58, 255, 100);\n"
"}")
        self.color_19 = QPushButton(self.mainWidget)
        self.color_19.setObjectName(u"color_19")
        self.color_19.setGeometry(QRect(590, 210, 31, 31))
        self.color_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_19.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(170, 0, 0, 100);\n"
"}")
        self.chosenColorLabel = QLabel(self.mainWidget)
        self.chosenColorLabel.setObjectName(u"chosenColorLabel")
        self.chosenColorLabel.setGeometry(QRect(320, 280, 121, 16))
        self.chosenColorLabel.setFont(font2)
        self.chosenColorLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.color_11 = QPushButton(self.mainWidget)
        self.color_11.setObjectName(u"color_11")
        self.color_11.setGeometry(QRect(190, 210, 31, 31))
        self.color_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_11.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(2, 255, 61);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(2, 255, 61, 100);\n"
"}")
        self.color_3 = QPushButton(self.mainWidget)
        self.color_3.setObjectName(u"color_3")
        self.color_3.setGeometry(QRect(290, 160, 31, 31))
        self.color_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 187, 205);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 187, 205, 100);\n"
"}")
        self.color_10 = QPushButton(self.mainWidget)
        self.color_10.setObjectName(u"color_10")
        self.color_10.setGeometry(QRect(640, 160, 31, 31))
        self.color_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_10.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(228, 225, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(228, 225, 255, 100);\n"
"}")
        self.color_18 = QPushButton(self.mainWidget)
        self.color_18.setObjectName(u"color_18")
        self.color_18.setGeometry(QRect(540, 210, 31, 31))
        self.color_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_18.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 85, 127);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(170, 85, 127, 100);\n"
"}")
        self.color_9 = QPushButton(self.mainWidget)
        self.color_9.setObjectName(u"color_9")
        self.color_9.setGeometry(QRect(590, 160, 31, 31))
        self.color_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_9.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 255, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(170, 255, 0, 100);\n"
"}")
        self.color_7 = QPushButton(self.mainWidget)
        self.color_7.setObjectName(u"color_7")
        self.color_7.setGeometry(QRect(490, 160, 31, 31))
        self.color_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_7.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 201, 64);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 201, 64, 100);\n"
"}")
        self.color_16 = QPushButton(self.mainWidget)
        self.color_16.setObjectName(u"color_16")
        self.color_16.setGeometry(QRect(440, 210, 31, 31))
        self.color_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_16.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(85, 85, 127);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.color_6 = QPushButton(self.mainWidget)
        self.color_6.setObjectName(u"color_6")
        self.color_6.setGeometry(QRect(440, 160, 31, 31))
        self.color_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(205, 53, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(205, 53, 255, 100);\n"
"}")
        self.separatedLine_5 = QLabel(self.mainWidget)
        self.separatedLine_5.setObjectName(u"separatedLine_5")
        self.separatedLine_5.setGeometry(QRect(60, 330, 740, 1))
        self.separatedLine_5.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.firstPriority = QPushButton(self.mainWidget)
        self.firstPriority.setObjectName(u"firstPriority")
        self.firstPriority.setGeometry(QRect(60, 380, 31, 31))
        font4 = QFont()
        font4.setFamilies([u"Montserrat SemiBold"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.firstPriority.setFont(font4)
        self.firstPriority.setCursor(QCursor(Qt.PointingHandCursor))
        self.firstPriority.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 0, 4);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 0, 4, 100);\n"
"}")
        self.firstPriority.setIconSize(QSize(20, 20))
        self.secondPriority = QPushButton(self.mainWidget)
        self.secondPriority.setObjectName(u"secondPriority")
        self.secondPriority.setGeometry(QRect(110, 380, 31, 31))
        self.secondPriority.setFont(font4)
        self.secondPriority.setCursor(QCursor(Qt.PointingHandCursor))
        self.secondPriority.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 128, 24);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 128, 24, 100);\n"
"}")
        self.secondPriority.setIconSize(QSize(20, 20))
        self.thirdPriority = QPushButton(self.mainWidget)
        self.thirdPriority.setObjectName(u"thirdPriority")
        self.thirdPriority.setGeometry(QRect(160, 380, 31, 31))
        self.thirdPriority.setFont(font4)
        self.thirdPriority.setCursor(QCursor(Qt.PointingHandCursor))
        self.thirdPriority.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 244, 87);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 244, 87, 100);\n"
"}")
        self.thirdPriority.setIconSize(QSize(20, 20))
        self.fourthPriority = QPushButton(self.mainWidget)
        self.fourthPriority.setObjectName(u"fourthPriority")
        self.fourthPriority.setGeometry(QRect(210, 380, 31, 31))
        self.fourthPriority.setFont(font4)
        self.fourthPriority.setCursor(QCursor(Qt.PointingHandCursor))
        self.fourthPriority.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(43, 255, 96);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(43, 255, 96, 100);\n"
"}")
        self.fourthPriority.setIconSize(QSize(20, 20))
        self.fifthPriority = QPushButton(self.mainWidget)
        self.fifthPriority.setObjectName(u"fifthPriority")
        self.fifthPriority.setGeometry(QRect(260, 380, 31, 31))
        self.fifthPriority.setFont(font4)
        self.fifthPriority.setCursor(QCursor(Qt.PointingHandCursor))
        self.fifthPriority.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(62, 123, 255);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(62, 123, 255, 100);\n"
"}")
        self.fifthPriority.setIconSize(QSize(20, 20))
        self.separatedLine_6 = QLabel(self.mainWidget)
        self.separatedLine_6.setObjectName(u"separatedLine_6")
        self.separatedLine_6.setGeometry(QRect(60, 435, 740, 1))
        self.separatedLine_6.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.prioriteLabel = QLabel(self.mainWidget)
        self.prioriteLabel.setObjectName(u"prioriteLabel")
        self.prioriteLabel.setGeometry(QRect(60, 350, 61, 16))
        self.prioriteLabel.setFont(font1)
        self.prioriteLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.prioriteLabel.setWordWrap(True)
        self.blankForTheDescription = QLineEdit(self.mainWidget)
        self.blankForTheDescription.setObjectName(u"blankForTheDescription")
        self.blankForTheDescription.setGeometry(QRect(380, 50, 431, 51))
        self.blankForTheDescription.setFont(font2)
        self.blankForTheDescription.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"	border-radius: 7px;\n"
"	padding: 12px;\n"
"}")
        self.blankForTheDescription.setEchoMode(QLineEdit.Normal)
        self.blankForTheDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton = QPushButton(self.mainWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 383, 51, 24))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/arrowToTheRight_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(30, 30))
        self.chosenPriority = QPushButton(self.mainWidget)
        self.chosenPriority.setObjectName(u"chosenPriority")
        self.chosenPriority.setGeometry(QRect(380, 380, 31, 31))
        self.chosenPriority.setFont(font4)
        self.chosenPriority.setCursor(QCursor(Qt.PointingHandCursor))
        self.chosenPriority.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"}")
        self.chosenPriority.setIconSize(QSize(20, 20))
        CreateADictionaryWindow.setCentralWidget(self.createADictionaryCentralWidget)

        self.retranslateUi(CreateADictionaryWindow)

        QMetaObject.connectSlotsByName(CreateADictionaryWindow)
    # setupUi

    def retranslateUi(self, CreateADictionaryWindow):
        CreateADictionaryWindow.setWindowTitle(QCoreApplication.translate("CreateADictionaryWindow", u"MainWindow", None))
        self.saveAndCreateADictionaryButton.setText(QCoreApplication.translate("CreateADictionaryWindow", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("CreateADictionaryWindow", u"Cancel", None))
        self.nameOfTheDictionaryLabel.setText(QCoreApplication.translate("CreateADictionaryWindow", u"Name of the dictionary", None))
        self.blankForTheName.setText("")
        self.blankForTheName.setPlaceholderText(QCoreApplication.translate("CreateADictionaryWindow", u"Enter the name", None))
        self.descriptionLabel.setText(QCoreApplication.translate("CreateADictionaryWindow", u"Descritpion", None))
        self.separatedLine_4.setText("")
        self.color_8.setText("")
        self.color_17.setText("")
        self.color_5.setText("")
        self.chosenColor.setText("")
        self.color_13.setText("")
        self.color_4.setText("")
        self.changeColorButton.setText("")
        self.color_15.setText("")
        self.color_14.setText("")
        self.color_2.setText("")
        self.color_1.setText("")
        self.color_12.setText("")
        self.color_19.setText("")
        self.chosenColorLabel.setText(QCoreApplication.translate("CreateADictionaryWindow", u"Chosen color:", None))
        self.color_11.setText("")
        self.color_3.setText("")
        self.color_10.setText("")
        self.color_18.setText("")
        self.color_9.setText("")
        self.color_7.setText("")
        self.color_16.setText("")
        self.color_6.setText("")
        self.separatedLine_5.setText("")
        self.firstPriority.setText(QCoreApplication.translate("CreateADictionaryWindow", u"1", None))
        self.secondPriority.setText(QCoreApplication.translate("CreateADictionaryWindow", u"2", None))
        self.thirdPriority.setText(QCoreApplication.translate("CreateADictionaryWindow", u"3", None))
        self.fourthPriority.setText(QCoreApplication.translate("CreateADictionaryWindow", u"4", None))
        self.fifthPriority.setText(QCoreApplication.translate("CreateADictionaryWindow", u"5", None))
        self.separatedLine_6.setText("")
        self.prioriteLabel.setText(QCoreApplication.translate("CreateADictionaryWindow", u"Priority", None))
        self.blankForTheDescription.setText("")
        self.blankForTheDescription.setPlaceholderText(QCoreApplication.translate("CreateADictionaryWindow", u"Enter the description", None))
        self.pushButton.setText("")
        self.chosenPriority.setText("")
    # retranslateUi

