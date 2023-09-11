from PySide6.QtCore import (Qt, QDir)
from PySide6.QtWidgets import (QMainWindow, QGraphicsDropShadowEffect, QFileDialog)
from PySide6.QtGui import (QIcon, QPixmap)

from uiPythonFiles.ui_settingsForm import Ui_SettingsOfTheProgramWindow
from database.database import (update_data_in_the_database, create_connection_to_the_database, select_data_in_the_database)
from localDatabase.local_database import (LocalDatabase, BlackedOutWidget)
from sqlite3 import Error
from windows.modules import showErrorMessage

import os
import windows


class SettingsOfTheProgramWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize local variables to save some data
        self.photo = None

        self.uiSettingsOfTheProgram = Ui_SettingsOfTheProgramWindow()
        self.uiSettingsOfTheProgram.setupUi(self)

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

        # Get connection to the database
        connection = create_connection_to_the_database(f"database/database.db")

        try:

            # Open a host to make connection to succeed
            with connection:

                # Get data from database
                getDataFromDatabase = select_data_in_the_database(
                    connection=connection,
                    data="email, username, password, photo",
                    condition=LocalDatabase.userLoginData.get("email")
                )

                # Set text to the email address blank from database and settings to it
                self.uiSettingsOfTheProgram.blankForEmailAddress.setText(getDataFromDatabase[0][0])
                self.uiSettingsOfTheProgram.blankForEmailAddress.setReadOnly(True)

                # Set text to the username blank
                self.uiSettingsOfTheProgram.blankForUsername.setText(getDataFromDatabase[0][1])

                # Set text to the username blank
                self.uiSettingsOfTheProgram.blankForPassword.setText(getDataFromDatabase[0][2])

                # Check if there is an existing path to the avatar image
                if getDataFromDatabase[0][3]:

                    # If there is, set an image to the avatar widget
                    if os.path.exists(getDataFromDatabase[0][3]):
                        self.uiSettingsOfTheProgram.accountAvatar.setPixmap(QPixmap(getDataFromDatabase[0][3]))

                    # If not, do nothing
                    else:
                        pass

        except Error as e:
            showErrorMessage.error_message(self, parent=self.uiSettingsOfTheProgram.mainFrame)
            print(e)
            return

    def mouse_events(self):

        """
        This function makes mouse events and responds to them

        :return:
        """

        # Make mouse events for each button on window and responds
        self.uiSettingsOfTheProgram.cancelButton.clicked.connect(self.close_the_window)
        self.uiSettingsOfTheProgram.saveTheSettingsButton.clicked.connect(self.process_the_settings)
        self.uiSettingsOfTheProgram.changeTheAvatarButton.clicked.connect(self.choose_a_photo_for_a_user)

    def process_the_settings(self):

        """
        This function processes the settings and applies and updates the needed information

        :return:
        """

        # Create a loop that goes in items of local database temporary data
        for key, values in LocalDatabase.temporaryData.items():

            # Set requires data to the widget as a "key"
            shadow = QGraphicsDropShadowEffect(None)
            icon = QIcon(values.get("icon_B"))

            key.setIcon(icon)
            key.setStyleSheet(values.get("styleSheet"))
            key.setGraphicsEffect(shadow)

        # Get texts from widgets
        email = self.uiSettingsOfTheProgram.blankForEmailAddress.text()
        username = self.uiSettingsOfTheProgram.blankForUsername.text()
        password = self.uiSettingsOfTheProgram.blankForPassword.text()

        # Get connection to the database
        connection = create_connection_to_the_database(f"database/database.db")

        try:

            # Open a host to make connection to succeed
            with connection:

                # Check if there is some data in self.photo local variable and do needed stuff
                if self.photo:
                    window = windows.MainWindow()
                    window.uiMainWindow.userIcon.setPixmap(QPixmap(self.photo))
                    window.uiMainWindow.username.setText(username)

                    # Update the information in the database
                    update_data_in_the_database(
                        connection,
                        "email = ?, username = ?, password = ?, photo = ?",
                        (email, username, password, self.photo, LocalDatabase.userLoginData.get("email"))
                    )

                    # Save the new email to the local database
                    LocalDatabase.userLoginData["email"] = email

                # If there is not...
                else:

                    # Update the information in the database
                    update_data_in_the_database(
                        connection,
                        "email = ?, username = ?, password = ?",
                        (email, username, password, LocalDatabase.userLoginData.get("email"))
                    )

                    # Save the new email to the local database
                    LocalDatabase.userLoginData["email"] = email

        except Error as e:
            showErrorMessage.error_message(self, parent=self.uiSettingsOfTheProgram.mainFrame)
            print(e)
            return

        # Remove the blacked out widget from dictionary_parent window by setting the dictionary_parent and stylesheet to None
        BlackedOutWidget.widget.setParent(None)
        BlackedOutWidget.widget.setStyleSheet(None)

        self.close()

    def choose_a_photo_for_a_user(self):

        """
        This function saves the selected path to the image that user wants to set to their avatar

        :return:
        """

        # Save a path to the selected image
        filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')

        # If there is not selected path, do nothing
        if not filename:
            pass

        # If there is, save the path to the local variable and set the avatar to the specific widget
        else:
            pixmap = QPixmap(filename)
            self.photo = filename

            self.uiSettingsOfTheProgram.accountAvatar.setPixmap(pixmap)

    def close_the_window(self):

        """
        This function just closes the child's window and makes settings to the blacked out widget

        :return:
        """

        # Create a loop that goes in items of local database temporary data
        for key, values in LocalDatabase.temporaryData.items():

            # Set requires data to the widget as a "key"
            shadow = QGraphicsDropShadowEffect(None)
            icon = QIcon(values.get("icon_B"))

            key.setIcon(icon)
            key.setStyleSheet(values.get("styleSheet"))
            key.setGraphicsEffect(shadow)

        # Remove the blacked out widget from dictionary_parent window by setting the dictionary_parent and stylesheet to None
        BlackedOutWidget.widget.setParent(None)
        BlackedOutWidget.widget.setStyleSheet(None)

        self.close()
