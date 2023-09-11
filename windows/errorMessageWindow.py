from PySide6.QtCore import (Qt)
from PySide6.QtWidgets import (QMainWindow)

from localDatabase.local_database import BlackedOutWidget
from uiPythonFiles.ui_ErrorMessageForm import Ui_ErrorWindow


class ErrorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.uiErrorMessageWindow = Ui_ErrorWindow()
        self.uiErrorMessageWindow.setupUi(self)

        self.init_UI()
        self.mouse_events()

    def init_UI(self):

        """

        This function sets the specific settings to the window

        :return:
        """

        # Set the specific settings to the window
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def mouse_events(self):

        """

        This function makes mouse events and responses to them

        :return:
        """

        # Make mouse events and responses to them
        self.uiErrorMessageWindow.okButton.clicked.connect(self.close_the_error_message)

    def close_the_error_message(self):

        """

        This function closes current window

        :return:
        """

        # Remove the blacked out widget from parent window and sets the styleSheet to None
        BlackedOutWidget.widget.setParent(None)
        BlackedOutWidget.widget.setStyleSheet(None)

        # Close the window
        self.close()

        BlackedOutWidget.widget = None

