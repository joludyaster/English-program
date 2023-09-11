from PySide6 import QtCore
from PySide6.QtWidgets import QWidget

import windows
from localDatabase.local_database import BlackedOutWidget


def error_message(text, parent):

    """
    This function takes a parameter "text" and sets it to a specific widget to show an error window

    :param parent: parent window
    :param text: text, that should be showed on the screen
    :return:
    """

    # Create a blacked out widget for MainWindow
    widget = QWidget()
    widget.setStyleSheet(
        """QWidget {
            background-color: rgba(0, 0, 0, 60);
            border: none;
        }"""
    )
    widget.setGeometry(0, 0, 1280, 720)
    widget.setParent(parent)

    # Create an instant to an error window
    window = windows.ErrorWindow()

    # If parameter has been shared to the function, set the text to an error window
    if text:
        window.uiErrorMessageWindow.explanationLabel.setText(text)

    # Make some settings to a child's window
    window.setParent(widget)
    window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
    window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

    # Save the object of the widget in local database
    BlackedOutWidget.widget = widget

    widget.show()
    window.show()
