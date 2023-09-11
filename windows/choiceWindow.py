from PySide6.QtCore import (Qt)
from PySide6.QtWidgets import (QMainWindow)

from localDatabase.local_database import (BlackedOutWidget, RemoveSomething)
from uiPythonFiles.ui_choiceForm import Ui_ChoiceMainWindow


class ChoiceWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.uiChoiceWindow = Ui_ChoiceMainWindow()
        self.uiChoiceWindow.setupUi(self)

        self.init_UI()
        self.mouse_events()

    def init_UI(self):

        """

        This function sets the specific settings to the window

        :return:
        """

        # Remove the window hint from the window
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Make the window translucent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def mouse_events(self):

        """

        This function makes mouse events and responses to them

        :return:
        """

        # Make mouse events and responses to them
        self.uiChoiceWindow.yesButton.clicked.connect(self.set_signal)
        self.uiChoiceWindow.noButton.clicked.connect(self.close_the_window)

    def set_signal(self):

        """

        This function sets the signal in the local database

        :return:
        """

        # Set the signal to remove something to True in the local database
        RemoveSomething.signal = True

        # Remove the blacked out widget from parent window and set the styleSheet to None
        BlackedOutWidget.widget.setParent(None)
        BlackedOutWidget.widget.setStyleSheet(None)

        # Close the window
        self.close()

    def close_the_window(self):

        """

        This function closes the window and sets the signal in the local database

        :return:
        """

        # Set the signal to remove something to False in the local database
        RemoveSomething.signal = False

        # Remove the blacked out widget from parent window and set the styleSheet to None
        BlackedOutWidget.widget.setParent(None)
        BlackedOutWidget.widget.setStyleSheet(None)

        # Close the window
        self.close()

