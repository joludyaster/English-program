# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trainingFormpPIBkb.ui'
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

class Ui_TrainingMainWindow(object):
    def setupUi(self, TrainingMainWindow):
        if not TrainingMainWindow.objectName():
            TrainingMainWindow.setObjectName(u"TrainingMainWindow")
        TrainingMainWindow.resize(1021, 592)
        self.trainingCentralWidget = QWidget(TrainingMainWindow)
        self.trainingCentralWidget.setObjectName(u"trainingCentralWidget")
        self.mainFrame = QFrame(self.trainingCentralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 1021, 592))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
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
        icon = QIcon()
        icon.addFile(u":/goBackIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.goBackButton.setIcon(icon)
        self.goBackButton.setIconSize(QSize(16, 16))
        self.nameOfTheDictionary = QLabel(self.infoFrame)
        self.nameOfTheDictionary.setObjectName(u"nameOfTheDictionary")
        self.nameOfTheDictionary.setGeometry(QRect(90, 20, 271, 31))
        font = QFont()
        font.setFamilies([u"Montserrat SemiBold"])
        font.setPointSize(19)
        font.setBold(True)
        self.nameOfTheDictionary.setFont(font)
        self.nameOfTheDictionary.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.descriptionOfTheDictionary = QLabel(self.infoFrame)
        self.descriptionOfTheDictionary.setObjectName(u"descriptionOfTheDictionary")
        self.descriptionOfTheDictionary.setGeometry(QRect(92, 50, 471, 16))
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        self.descriptionOfTheDictionary.setFont(font1)
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
        icon1 = QIcon()
        icon1.addFile(u":/closeSomethingIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeThewindowButton.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u":/minimizeWindowIcon_B.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeTheWindowButton.setIcon(icon2)
        self.minimizeTheWindowButton.setIconSize(QSize(10, 10))
        self.widget = QWidget(self.mainFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 130, 961, 431))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")
        self.helpWidget = QWidget(self.widget)
        self.helpWidget.setObjectName(u"helpWidget")
        self.helpWidget.setGeometry(QRect(30, 30, 171, 371))
        self.helpWidget.setStyleSheet(u"QWidget {\n"
"	background-color: none;\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")
        self.time = QLabel(self.helpWidget)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(20, 20, 131, 21))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(12)
        self.time.setFont(font2)
        self.time.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.separatedLine = QLabel(self.helpWidget)
        self.separatedLine.setObjectName(u"separatedLine")
        self.separatedLine.setGeometry(QRect(20, 60, 131, 1))
        self.separatedLine.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"}")
        self.trainingWidget = QWidget(self.widget)
        self.trainingWidget.setObjectName(u"trainingWidget")
        self.trainingWidget.setGeometry(QRect(220, 30, 711, 371))
        self.trainingWidget.setStyleSheet(u"QWidget {\n"
"	background-color: none;\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"}")
        TrainingMainWindow.setCentralWidget(self.trainingCentralWidget)

        self.retranslateUi(TrainingMainWindow)

        QMetaObject.connectSlotsByName(TrainingMainWindow)
    # setupUi

    def retranslateUi(self, TrainingMainWindow):
        TrainingMainWindow.setWindowTitle(QCoreApplication.translate("TrainingMainWindow", u"MainWindow", None))
        self.goBackButton.setText("")
        self.nameOfTheDictionary.setText(QCoreApplication.translate("TrainingMainWindow", u"My Words", None))
        self.descriptionOfTheDictionary.setText(QCoreApplication.translate("TrainingMainWindow", u"Dictionary for learning new words in English", None))
        self.closeThewindowButton.setText("")
        self.minimizeTheWindowButton.setText("")
        self.time.setText(QCoreApplication.translate("TrainingMainWindow", u"9:29:56", None))
        self.separatedLine.setText("")
    # retranslateUi

