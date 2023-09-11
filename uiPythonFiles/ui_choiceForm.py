# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choiceFormAcjirL.ui'
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

class Ui_ChoiceMainWindow(object):
    def setupUi(self, ChoiceMainWindow):
        if not ChoiceMainWindow.objectName():
            ChoiceMainWindow.setObjectName(u"ChoiceMainWindow")
        ChoiceMainWindow.resize(511, 272)
        self.ChoiceCentralWidget = QWidget(ChoiceMainWindow)
        self.ChoiceCentralWidget.setObjectName(u"ChoiceCentralWidget")
        self.mainFrame = QFrame(self.ChoiceCentralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 511, 272))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.icon = QPushButton(self.mainFrame)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(30, 40, 101, 81))
        self.icon.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/warningIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon1)
        self.icon.setIconSize(QSize(70, 70))
        self.cautionLabel = QLabel(self.mainFrame)
        self.cautionLabel.setObjectName(u"cautionLabel")
        self.cautionLabel.setGeometry(QRect(140, 50, 141, 31))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(23)
        font.setBold(True)
        self.cautionLabel.setFont(font)
        self.cautionLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.explanationLabel = QLabel(self.mainFrame)
        self.explanationLabel.setObjectName(u"explanationLabel")
        self.explanationLabel.setGeometry(QRect(140, 82, 321, 41))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(13)
        font1.setBold(False)
        self.explanationLabel.setFont(font1)
        self.explanationLabel.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.explanationLabel.setWordWrap(True)
        self.yesButton = QPushButton(self.mainFrame)
        self.yesButton.setObjectName(u"yesButton")
        self.yesButton.setGeometry(QRect(140, 170, 101, 51))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.yesButton.setFont(font2)
        self.yesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.yesButton.setStyleSheet(u"QPushButton {\n"
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
        self.noButton = QPushButton(self.mainFrame)
        self.noButton.setObjectName(u"noButton")
        self.noButton.setGeometry(QRect(250, 170, 101, 51))
        self.noButton.setFont(font2)
        self.noButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.noButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 36, 36);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 63, 63);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 26, 26);\n"
"}")
        self.noButton.setIconSize(QSize(10, 10))
        ChoiceMainWindow.setCentralWidget(self.ChoiceCentralWidget)

        self.retranslateUi(ChoiceMainWindow)

        QMetaObject.connectSlotsByName(ChoiceMainWindow)
    # setupUi

    def retranslateUi(self, ChoiceMainWindow):
        ChoiceMainWindow.setWindowTitle(QCoreApplication.translate("ChoiceMainWindow", u"MainWindow", None))
        self.icon.setText("")
        self.cautionLabel.setText(QCoreApplication.translate("ChoiceMainWindow", u"Careful!", None))
        self.explanationLabel.setText(QCoreApplication.translate("ChoiceMainWindow", u"Are you sure you want to remove this dictionary?", None))
        self.yesButton.setText(QCoreApplication.translate("ChoiceMainWindow", u"Yes", None))
        self.noButton.setText(QCoreApplication.translate("ChoiceMainWindow", u"No", None))
    # retranslateUi

