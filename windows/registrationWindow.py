from sqlite3 import Error

from PySide6 import (QtCore)
from PySide6.QtCore import (Qt, QPoint)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QMainWindow, QLineEdit, QWidget)
from database.database import (create_connection_to_the_database, create_table_in_the_database, insert_data_in_the_database, select_data_in_the_database)
from localDatabase.local_database import (BlackedOutWidget)
from uiPythonFiles.ui_RegistrationForm import Ui_RegistrationWindow
from windows.modules import showErrorMessage

import windows
import os
import re


class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize local variables
        self.clickPosition = None
        self.window = None

        # Initialize local features
        self.status = True

        self.uiRegistrationWindow = Ui_RegistrationWindow()
        self.uiRegistrationWindow.setupUi(self)

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

        # Set echo mode for the password widget
        self.uiRegistrationWindow.blankForThePassword.setEchoMode(QLineEdit.EchoMode.Password)

    def mouse_events(self):

        """
        This function makes mouse events and responds to them

        :return:
        """

        # Make mouse events for each button on window and responses
        self.uiRegistrationWindow.openSignInWindowButton.clicked.connect(self.show_the_login_window)
        self.uiRegistrationWindow.showAndHidePasswordButton.clicked.connect(self.show_and_hide_the_password)
        self.uiRegistrationWindow.movingFrame.mouseMoveEvent = self.move_window

        self.uiRegistrationWindow.closeTheWindowButton.clicked.connect(lambda: self.close())
        self.uiRegistrationWindow.minimizeTheWindowButton.clicked.connect(lambda: self.showMinimized())

        self.uiRegistrationWindow.createAnAccountButton.clicked.connect(self.checking_the_entered_data)

    def checking_the_entered_data(self):

        """
        This function checks the entered data by the user and checks if they meet the standards of the normal
        email, then creates a database with entered data as a unique data of the user

        :return:
        """

        # Get required information from widgets and make new variables
        email = self.uiRegistrationWindow.blankForTheAddress.text()
        username = ""
        password = self.uiRegistrationWindow.blankForThePassword.text()
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        # Check if user entered email and password
        if email and password:

            # Check if the entered email meets the standards of normal email
            if re.search(regex, email):

                # Check if user has any created accounts
                if os.path.exists("database/database.db"):

                    try:

                        # Get connection to the database
                        connection = create_connection_to_the_database("database/database.db")

                        # Check if the connection succeed, in case of unexpected errors
                        if connection is not None:

                            # Open a host to make connection to succeed
                            with connection:

                                # Get data from database
                                getDataFromDatabase = select_data_in_the_database(connection, "email", email)

                                # Check if there is data of entered email by user
                                if getDataFromDatabase:
                                    showErrorMessage.error_message(
                                        text="You have already registered using this e-mail address.",
                                        parent=self.uiRegistrationWindow.mainFrame
                                    )
                                    self.uiRegistrationWindow.blankForTheAddress.setText("")
                                    return

                                # If not, create a required columns in database
                                else:
                                    insert_data_in_the_database(connection, (email, username, password, "", False))
                                    self.show_the_login_window()
                                    return

                        # If the connection failed, show an error
                        else:
                            showErrorMessage.error_message(
                                text="",
                                parent=self.uiRegistrationWindow.mainFrame
                            )
                            self.uiRegistrationWindow.blankForTheAddress.setText("")
                            self.uiRegistrationWindow.blankForThePassword.setText("")
                            return

                    except Error as e:
                        showErrorMessage.error_message(
                            text=e,
                            parent=self.uiRegistrationWindow.mainFrame
                        )
                        print(e)
                        return

                # If user has accounts...
                else:
                    # Create a database.db where program will add all the information about the user
                    with open("database/database.db", "w"):

                        try:

                            # Get the connection to the database
                            connection = create_connection_to_the_database("database/database.db")

                            # Create a cover of sql_table that will be inserted in database
                            sql_create_projects_table = """
                                CREATE TABLE IF NOT EXISTS data (
                                    id integer PRIMARY KEY,
                                    email text DEFAULT "",
                                    username text DEFAULT "",
                                    photo text DEFAULT "",
                                    password text DEFAULT "",
                                    dictionary JSON DEFAULT "",
                                    signing_in boolean DEFAULT False
                                ); 
                            """

                            # If connection succeed, create a sql_table and insert required columns in database
                            if connection is not None:

                                # Open a host to make connection to succeed
                                with connection:
                                    create_table_in_the_database(connection, sql_create_projects_table)
                                    insert_data_in_the_database(connection, (email, username, password, "", False))

                                    self.show_the_login_window()
                                    return

                            # If connection failed, show an error
                            else:
                                showErrorMessage.error_message(
                                    text="",
                                    parent=self.uiRegistrationWindow.mainFrame
                                )
                                self.uiRegistrationWindow.blankForTheAddress.setText("")
                                self.uiRegistrationWindow.blankForThePassword.setText("")
                                return

                        except Error as e:
                            showErrorMessage.error_message(
                                text=e,
                                parent=self.uiRegistrationWindow.mainFrame
                            )
                            print(e)
                            return

            # If entered email doesn't meet the standards of normal email, show an error
            else:
                showErrorMessage.error_message(
                    text="Email is incorrect.",
                    parent=self.uiRegistrationWindow.mainFrame
                )
                self.uiRegistrationWindow.blankForTheAddress.setText("")
                return

        # If user didn't enter none of them, show an error
        else:
            showErrorMessage.error_message(
                text="Email and password have not been filled up.",
                parent=self.uiRegistrationWindow.mainFrame
            )
            self.uiRegistrationWindow.blankForTheAddress.setText("")
            self.uiRegistrationWindow.blankForThePassword.setText("")
            return

    def show_and_hide_the_password(self):

        """
        This function sets and shows the password of the widget

        :return:
        """

        # Check if the status is True, then change an icon and echo mode to the password widget
        if self.status:
            icon = QIcon("icons/showIcon_B.png")

            self.uiRegistrationWindow.blankForThePassword.setEchoMode(QLineEdit.EchoMode.Normal)
            self.uiRegistrationWindow.showAndHidePasswordButton.setIcon(icon)
            self.status = False

        # If the status is False, then change an icon and echo mode to the password widget
        else:
            icon = QIcon("icons/hideIcon_B.png")

            self.uiRegistrationWindow.blankForThePassword.setEchoMode(QLineEdit.EchoMode.Password)
            self.uiRegistrationWindow.showAndHidePasswordButton.setIcon(icon)
            self.status = True

    def show_the_login_window(self):

        """
        This function shows different window

        :return:
        """

        # Close the current window
        self.close()

        # Create an instant to another window and show it
        self.window = windows.LoginWindow()
        self.window.show()

        self.window = None

    # """""""""""""""""""""""""""""""""""""""""
    # FUNCTIONS TO MOVE THE WINDOW
    # """""""""""""""""""""""""""""""""""""""""

    def move_window(self, event):

        """
        This function takes an event parameter and data of local variable "self.clickPosition" to move the window
        to a different position

        :param event: side of the mouse that has been clicked
        :return:
        """

        # Check, if the moving frame was clicked and moved by left button of the mouse
        if event.buttons() == Qt.MouseButton.LeftButton:

            # Move the window to a different position
            self.move(QPoint(self.pos() + event.globalPosition().toPoint() - self.clickPosition).x(),
                      QPoint(self.pos() + event.globalPosition().toPoint() - self.clickPosition).y())

            # Save the position in the local variable
            self.clickPosition = event.globalPosition().toPoint()

            # Proceed the event
            event.accept()

    def mousePressEvent(self, event):

        """
        This function saves the current clicked position of the mouse

        :param event: side of the mouse that has been clicked
        :return:
        """

        # Save the position in the local variable
        self.clickPosition = event.globalPosition().toPoint()
