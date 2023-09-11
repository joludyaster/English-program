import tracemalloc

from PySide6.QtCore import (Qt, QPoint)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QMainWindow, QLineEdit, QWidget)

from uiPythonFiles.ui_LoginForm import Ui_LoginWindow
from database.database import (create_connection_to_the_database, select_data_in_the_database)
from localDatabase.local_database import (LocalDatabase)
from windows.modules import showErrorMessage, SlidingStackedWidget
from memory_profiler import profile

import windows
import os
import tracemalloc


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize variables
        self.clickPosition = None
        self.window = None

        # Initialize features
        self.status = True
        self.slidingStackedWidget = None

        self.uiLoginWindow = Ui_LoginWindow()
        self.uiLoginWindow.setupUi(self)

        self.init_UI()
        self.mouse_events()
        self.create_a_sliding_stacked_widget()

    def init_UI(self):

        """

        This function sets the specific settings to the window

        :return:
        """

        # Set the specific settings to the window
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Set echo mode for the QLineEdit, so the password doesn't show what user types
        self.uiLoginWindow.blankForThePassword.setEchoMode(QLineEdit.EchoMode.Password)

    def mouse_events(self):


        """

        This function makes mouse events and responses to them

        :return:
        """

        # Make mouse events and responses to them
        self.uiLoginWindow.signUpButton.clicked.connect(self.show_the_registration_window)
        self.uiLoginWindow.showAndHidePasswordButton.clicked.connect(self.show_and_hide_the_password)
        self.uiLoginWindow.movingFrame.mouseMoveEvent = self.move_window

        # When button clicked, close the window
        self.uiLoginWindow.closeTheWindowButton.clicked.connect(lambda: self.close())

        # When the button clicked, minimize the window
        self.uiLoginWindow.minimizeTheWindowButton.clicked.connect(lambda: self.showMinimized())

        self.uiLoginWindow.signInButton.clicked.connect(self.sign_in)

    @profile
    def sign_in(self):

        tracemalloc.start()

        """

        This function checks the entered data by user and decided if they meet the standards

        :return:
        """

        # Get the text from email QLineEdit
        email = self.uiLoginWindow.blankForTheAddress.text()

        # Get the text from password QLineEdit
        password = self.uiLoginWindow.blankForThePassword.text()

        # Check if the database exists
        if os.path.exists(f"database/database.db"):

            # Get connection to the database
            connection = create_connection_to_the_database(f"database/database.db")

            # Open a host to make connection to succeed
            with connection:

                # Get data from database
                getDataFromDatabase = select_data_in_the_database(
                    connection,
                    "email, password",
                    ""
                )

                # Create a loop that goes in dict of items from database
                for items in getDataFromDatabase:

                    # If the items equal the entered by user data
                    if email == items[0] and password == items[1]:

                        # Save login data to the local database
                        LocalDatabase.userLoginData = {
                            "email": email,
                            "password": password
                        }

                        # Close the window
                        self.close()

                        # Create an instant to the different window
                        self.window = windows.MainWindow()

                        # Show this window
                        self.window.show()

                        self.window = None

                        return

                    # If items are not equal the entered by user data
                    else:

                        # Show an error window with explanation label
                        showErrorMessage.error_message(
                            text="Email or password is incorrect. Try again.",
                            parent=self.uiLoginWindow.mainFrame
                        )

                        # Set empty texts to the email and password line edits
                        self.uiLoginWindow.blankForTheAddress.setText("")
                        self.uiLoginWindow.blankForThePassword.setText("")

                        return

        # If database doesn't exist
        else:

            # Show an error window with explanation label
            showErrorMessage.error_message(
                text="Email or password is incorrect. Try again.",
                parent=self.uiLoginWindow.mainFrame
            )

            # Set empty texts to the email and password line edits
            self.uiLoginWindow.blankForTheAddress.setText("")
            self.uiLoginWindow.blankForThePassword.setText("")

            return

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')

        for stat in top_stats:
            print(stat)

    def show_and_hide_the_password(self):

        """

        This function changes echo mode (shows and hides password) by clicking on the button

        :return:
        """

        # Check if password is hidden
        if self.status:

            # Change echo mode to the line edit
            self.uiLoginWindow.blankForThePassword.setEchoMode(QLineEdit.EchoMode.Normal)

            # Change icon of the button
            self.uiLoginWindow.showAndHidePasswordButton.setIcon(QIcon("icons/showIcon_B.png"))

            # Change status to False
            self.status = False

        # If password is shown
        else:

            # Change echo mode to the line edit
            self.uiLoginWindow.blankForThePassword.setEchoMode(QLineEdit.EchoMode.Password)

            # Change icon of the button
            self.uiLoginWindow.showAndHidePasswordButton.setIcon(QIcon("icons/hideIcon_B.png"))

            # Change status to True
            self.status = True

    def show_the_registration_window(self):

        """

        This function shows the registration window and closes the current one

        :return:
        """

        # Close current window
        self.close()

        # Create an instant to the different window
        self.window = windows.RegisterWindow()

        # Show this window
        self.window.show()

        self.window = None

    def create_a_sliding_stacked_widget(self):

        """

        This function takes the pages of the already created stackedWidget in the QtDesigner and applies the
        slidingStackedWidget option

        :return:
        """

        # Create a sliding stacked widget and set the specific setting to it
        self.slidingStackedWidget = SlidingStackedWidget(parent=self.uiLoginWindow.mainFrame)
        self.slidingStackedWidget.setGeometry(60, 110, 461, 541)
        self.slidingStackedWidget.setStyleSheet(
            """
            QStackedWidget {
                background-color: none;
                border: none;
            }
            """
        )

        # Get the children from created stackedWidget
        children = self.uiLoginWindow.stackedWidget.findChildren(QWidget)

        # Get the first page from children objects
        firstPage = [firstPage for firstPage in children if firstPage.objectName() == "signUpPage"]

        # Get the second page from children objects
        secondPage = [secondPage for secondPage in children if secondPage.objectName() == "restoreThePasswordPage"]

        # Get the third page from children objects
        thirdPage = [thirdPage for thirdPage in children if thirdPage.objectName() == "newPasswordConfirmationPage"]

        # Create a loop that goes in the list of 3 pages
        for page in [firstPage, secondPage, thirdPage]:

            # Add widget to the slidingStackedWidget
            self.slidingStackedWidget.addWidget(page[0])

        # Make mouse events and responses to them
        self.uiLoginWindow.forgotPasswordButton.clicked.connect(self.slidingStackedWidget.slide_forward)
        self.uiLoginWindow.goBackButton.clicked.connect(self.slidingStackedWidget.slide_backward)

        # Set current page in the slidingStackedWidget
        self.slidingStackedWidget.setCurrentWidget(firstPage[0])

        # Set the parent of the created stackedWidget to None to make it dissapear
        self.uiLoginWindow.stackedWidget.setParent(None)

    # ------------------------------
    # FUNCTIONS TO MOVE THE WINDOW
    # ------------------------------

    def move_window(self, event):

        """

        This function moves the window according to some data, such as coordinates, current position of the
        window and global position of the window on the screen

        :param event:
        :return:
        """

        # Check, if the press button from the event was left button of the mouse
        if event.buttons() == Qt.MouseButton.LeftButton:

            # Move the window according to current position, global position of the window and coordinates
            self.move(QPoint(self.pos() + event.globalPosition().toPoint() - self.clickPosition).x(),
                      QPoint(self.pos() + event.globalPosition().toPoint() - self.clickPosition).y())

            # Save global position to the local variable
            self.clickPosition = event.globalPosition().toPoint()

            # Proceed the event
            event.accept()

    def mousePressEvent(self, event):

        """

        This function saves global position of the window on the screen by pressed on the moving image

        :param event:
        :return:
        """

        # Save global position to the local variable
        self.clickPosition = event.globalPosition().toPoint()


