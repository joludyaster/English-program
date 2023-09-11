from sqlite3 import Error

from PySide6 import (QtCore)
from PySide6.QtCore import (Qt, QPoint)
from PySide6.QtGui import (QIcon, QColor)
from PySide6.QtWidgets import (QMainWindow, QLineEdit, QWidget, QGraphicsDropShadowEffect)
from database.database import (create_connection_to_the_database, create_table_in_the_database, insert_data_in_the_database, select_data_in_the_database)
from localDatabase.local_database import (BlackedOutWidget)
from uiPythonFiles.ui_trainingForm import Ui_TrainingMainWindow
from windows.modules import showErrorMessage

import windows
import os
import re


class TrainingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize local variables
        self.clickPosition = None
        self.window = None

        # Initialize local features
        self.status = True

        self.uiTrainingWindow = Ui_TrainingMainWindow()
        self.uiTrainingWindow.setupUi(self)

        self.init_UI()
        self.mouse_events()

    def init_UI(self):

        """
        This function makes some settings to a window and also set the needed information
        to a needed widgets

        :return:
        """

        # Set settings to the window
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Create a shadow effect for the widgets
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setBlurRadius(35)
        shadowEffect.setColor(QColor(240, 240, 240, 255))
        shadowEffect.setOffset(0, 2)

        self.uiTrainingWindow.helpWidget.setGraphicsEffect(shadowEffect)
        self.uiTrainingWindow.separatedLine.setGraphicsEffect(shadowEffect)
        # self.uiTrainingWindow.trainingWidget.setGraphicsEffect(shadowEffect)

    def mouse_events(self):

        """
        This function makes mouse events and responds to them

        :return:
        """

        # Make mouse events for each button on window and responses
        pass
