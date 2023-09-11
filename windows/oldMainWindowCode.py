import time

from PySide6 import (QtCore)
from PySide6.QtCore import (Qt, QPoint, QSize, QTimer)
from PySide6.QtGui import (QIcon, QFont, QPixmap, QColor)
from PySide6.QtWidgets import (QMainWindow, QLineEdit, QGraphicsDropShadowEffect, QPushButton, QFrame, QLabel,
                               QPlainTextEdit, QWidget, QVBoxLayout, QScrollArea)
from localDatabase.local_database import (LocalDatabase, BlackedOutWidget, EditADictionary, RemoveSomething)
from uiPythonFiles.ui_MainForm import Ui_MainWindow
from database.database import (select_data_in_the_database, create_connection_to_the_database,
                               update_data_in_the_database)
from memory_profiler import profile

import windows
import json
import os.path
import gc
import tracemalloc


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Initialize variables
        self.clickPosition = None
        self.timer = None
        self.blackedOutWidget = None
        self.object = None

        self.methods = None

        self.uiMainWindow = Ui_MainWindow()
        self.uiMainWindow.setupUi(self)

        self.init_UI()
        self.mouse_events()

    def init_UI(self):

        """
        This function makes some settings to a window and also set the needed information
        to a needed widgets

        :return: None
        """

        # Set settings to the window
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Create an icon to put it in the place of search widget
        search = QIcon("icons/searchIcon_B.png")
        self.uiMainWindow.searchLine.addAction(search, QLineEdit.ActionPosition.LeadingPosition)

        # Create a shadow effect for the widgets
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setBlurRadius(35)
        shadowEffect.setColor(QColor(240, 240, 240, 255))
        shadowEffect.setOffset(0, 2)

        # Apply the shadow effect to the widget
        self.uiMainWindow.buttonsWidget.setGraphicsEffect(shadowEffect)

        # Get connection to the database
        connection = create_connection_to_the_database("database/database.db")

        # Open a host to make connection to succeed
        with connection:

            # Get data from database
            getDataFromDatabase = select_data_in_the_database(connection, "username, photo",
                                                              LocalDatabase.userLoginData.get("email"))

            # Check if there is username in database, if there is, set it to the username label
            if getDataFromDatabase[0][0]:
                self.uiMainWindow.username.setText(getDataFromDatabase[0][0])

            # If there is not, set "user" to the username label
            else:
                self.uiMainWindow.username.setText("user")

            # Check if there is a path to the photo that has been selected
            if getDataFromDatabase[0][1]:

                # Check if the path of the photo exists
                if os.path.exists(getDataFromDatabase[0][1]):

                    # Set the avatar
                    self.uiMainWindow.userIcon.setPixmap(QPixmap(getDataFromDatabase[0][1]))
                else:
                    pass

        # Set the current index of the page in the stacked widget (index - number of the page)
        self.uiMainWindow.stackedWidget.setCurrentIndex(1)

        for name in locals():
            del name

        gc.collect()

    def mouse_events(self):

        """
        This function makes mouse events and responses to them

        :return: None
        """

        # Create a variable that contains object of the class that gives us needed methods
        self.methods = DictionaryMethods(
            parent_window=self,
            main_parent_widget=self.uiMainWindow.mainFrame,
            dictionary_parent=self.uiMainWindow.frameForPage_1
        )

        # Make mouse events for each button on window and responds
        self.uiMainWindow.signOutButton.clicked.connect(self.show_a_login_window)
        self.uiMainWindow.refreshTheListOfVocabularies.clicked.connect(self.methods.refresh_list_of_the_dictionaries)

        for item in [
            self.uiMainWindow.englishDictionariesButton,
            self.uiMainWindow.englishLessonsButton,
            self.uiMainWindow.settingsOfTheProgramButton
        ]:
            item.clicked.connect(self.get_clicks_from_buttons)

        self.uiMainWindow.addANewDictionaryButton.clicked.connect(self.show_a_window_to_create_a_dictionary)

        # When button clicked, close the window
        self.uiMainWindow.closeTheWindowButton.clicked.connect(lambda: self.close())

        # When button clicked, minimize the window
        self.uiMainWindow.minimizeTheWindowButton.clicked.connect(lambda: self.showMinimized())

        # When person clicks or moves the background image, window moves
        self.uiMainWindow.backgroundImage.mouseMoveEvent = self.move_window

    def show_a_login_window(self):

        """

        This function shows the sign in window

        :return:
        """

        self.close()

        window = windows.LoginWindow()
        window.show()

        for name in locals():
            del name

        gc.collect()

    def show_a_window_to_create_a_dictionary(self):

        """

        This function shows us the window to create a dictionary and also sets the blacked out widget
        on parent window

        :return:
        """

        # Make the setting to a child's window
        window = windows.CreatingAVocabularyWindow()
        window.setParent(self)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
        window.setWindowModality(QtCore.Qt.WindowModality.WindowModal)

        # Create a blacked out widget for MainWindow
        widget = QWidget(self)
        widget.setStyleSheet(
            """QWidget {
                background-color: rgba(0, 0, 0, 50);
                border: none;
            }"""
        )
        widget.setGeometry(0, 0, 1280, 720)
        widget.setParent(self.uiMainWindow.mainFrame)
        widget.show()

        # Save the object of the widget in local database
        BlackedOutWidget.widget = widget

        window.show()

        for name in locals():
            del name

        gc.collect()

    def get_clicks_from_buttons(self):

        """

        This function gets clicks from buttons and makes proper responses to them

        :return:
        """

        # Get the object of the clicked button
        sender = self.sender()

        # Make a dict to make the work easy when getting data
        dataOfButtons = {
            "englishLessonsButton": {
                "icon_B": "icons/englishLessonsIcon_B.png",
                "icon_W": "icons/englishLessonsIcon_W.png",
                "index": 2
            },
            "englishDictionariesButton": {
                "icon_B": "icons/wordsIcon_B.png",
                "icon_W": "icons/wordsIcon_W.png",
                "index": 0
            },
            "settingsOfTheProgramButton": {
                "icon_B": "icons/settingsIcon_B",
                "icon_W": "icons/settingsIcon_W"
            }
        }

        # Check if the variable "temporaryData" in local database consists of something
        if LocalDatabase.temporaryData:

            # Create a loop, that goes in the temporaryData dict
            for key, values in LocalDatabase.temporaryData.items():
                # Set the setting to the object, such as icon and shadow
                icon = QIcon(values.get("icon_B"))
                shadow = QGraphicsDropShadowEffect(None)

                key.setIcon(icon)
                key.setStyleSheet(values.get("styleSheet"))
                key.setGraphicsEffect(shadow)

        # Set a specific data to a temporaryData dict in local database
        LocalDatabase.temporaryData = {
            sender: {
                "icon_B": dataOfButtons.get(sender.objectName()).get("icon_B"),
                "styleSheet": sender.styleSheet()
            }
        }

        # Set a new styleSheet to an object "sender", that we got earlier
        sender.setStyleSheet(
            """QPushButton {
                background-color: black;
                border-radius: 7px;
            }"""
        )

        # Set a new icon to an object "sender", that we got earlier
        icon = QIcon(dataOfButtons.get(sender.objectName()).get("icon_W"))
        sender.setIcon(icon)

        # Check, if the objectName of the object equals the objectName in the local dict
        if sender.objectName() == "settingsOfTheProgramButton":
            # Create a blacked out widget for MainWindow
            widget = QWidget(self)
            widget.setStyleSheet(
                """QWidget {
                    background-color: rgba(0, 0, 0, 50);
                    border: none;
                }"""
            )
            widget.setGeometry(0, 0, 1280, 720)
            widget.setParent(self.uiMainWindow.mainFrame)
            widget.show()

            # Save the object of the widget in local database
            BlackedOutWidget.widget = widget

            # Create an instant to a window and set specific setting to it
            window = windows.SettingsOfTheProgramWindow()
            window.setParent(self)
            window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
            window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

            # After the window will be closed, the function below will start
            window.closeEvent = self.update_username_and_avatar_of_user

            window.show()

        # Check if there is index in the local dict of the data
        if "index" in dataOfButtons[sender.objectName()]:
            # Get the index
            index = dataOfButtons.get(sender.objectName()).get("index")

            # Set a current index in the stackedWidget (index - number of the page)
            self.uiMainWindow.stackedWidget.setCurrentIndex(index)

        for name in locals():
            del name

        gc.collect()

    def update_username_and_avatar_of_user(self, event):

        """

        This function updates the avatar and username of user

        :param event: object that comes from closeEvent
        :return:
        """

        # Set current index to a stacked widget (index 1 - dashboard page/empty page)
        self.uiMainWindow.stackedWidget.setCurrentIndex(1)

        # Get connection to the database
        connection = create_connection_to_the_database(f"database/database.db")

        # Open a host to make connection to succeed
        with connection:

            # Get data from database
            get_data_from_database = select_data_in_the_database(
                connection=connection,
                data="username, photo",
                condition=LocalDatabase.userLoginData.get("email")
            )

            # Set text to the username widget in main window
            self.uiMainWindow.username.setText(get_data_from_database[0][0])

            # Check if there is url to the photo on the user's computer
            if get_data_from_database[0][1]:

                # Check, if the path to the url of the photo is actually available on the user's computer
                if os.path.exists(get_data_from_database[0][1]):

                    # Set the photo to the avatar's widget
                    self.uiMainWindow.userIcon.setPixmap(QPixmap(get_data_from_database[0][1]))

                # Do nothing
                else:
                    pass

        for name in locals():
            del name

        gc.collect()

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


# -----------------------------------------------
# CLASS THAT CONTAINS METHODS OF THE DICTIONARIES
# -----------------------------------------------
class WidgetFactory:
    def __init__(self):
        self.widget_pool = {}  # Store a pool of widgets by type

    def create_or_reuse_widget(self, widget_type, text=None, geometry=(0, 0, 0, 0), style_sheet='', fixed_size=False):

        # Check if there's a widget of the desired type in the pool
        if widget_type in self.widget_pool:
            widget = self.widget_pool[widget_type].pop()
        else:

            # If no widget of this type in the pool, create a new one
            widget = self.create_widget(widget_type, text, geometry, style_sheet)

        return widget

    def release_widget(self, widget):

        # Add the widget back to the pool based on its type
        widget_type = type(widget).__name__
        if widget_type not in self.widget_pool:
            self.widget_pool[widget_type] = []
        self.widget_pool[widget_type].append(widget)

    @staticmethod
    def create_widget(widget_type, text=None, geometry=(0, 0, 0, 0), style_sheet='', fixed_size=False):

        widget = None

        if widget_type == 'QPushButton':
            widget = QPushButton(text)
        elif widget_type == 'QLabel':
            widget = QLabel(text)
        elif widget_type == 'QFrame':
            widget = QFrame()

        if widget:
            widget.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
            if style_sheet:
                widget.setStyleSheet(style_sheet)

        return widget


class DictionaryMethods(QMainWindow):
    def __init__(self, parent_window, main_parent_widget, dictionary_parent):
        super(DictionaryMethods, self).__init__()

        # Initialize variables
        self.parentWindow = parent_window
        self.mainParent = main_parent_widget
        self.dictionaryParent = dictionary_parent
        self.object = None

        self.widgetFactory = WidgetFactory()

    def refresh_list_of_the_dictionaries(self):

        tracemalloc.start()

        """

        This function refreshes the list of the dictionaries on the spot of the main window by creating
        visible widgets

        :return:
        """

        # Get connection to the database
        connection = create_connection_to_the_database(f"database/database.db")

        # Open a host to make connection to succeed
        with connection:

            # Get data from database
            getDataFromDatabase = select_data_in_the_database(
                connection,
                "dictionary",
                LocalDatabase.userLoginData.get("email")
            )

        # Check if there is data in database
        if not getDataFromDatabase[0][0]:

            # If not, do nothing
            return

        # If there is data in database...
        else:

            # ---------------------------------------------------------------------------------------------------
            # The dictionary, that we got in the variable "getDataFromDatabase" gives us the string of the dict,
            # that's why we need to convert the string into an object "dict" using the library "json"
            # ---------------------------------------------------------------------------------------------------
            dictionary = json.loads(getDataFromDatabase[0][0].replace("'", ""))

            # Save the positions and sizes in the dict, so later we can use it easily
            geometry = {
                "QMainFrame": [301, 331],
                "QFrameOfTheStuff": [0, 0, 331, 201],
                "QIcon": [30, 20, 61, 61],
                "QNumberOfDictionary": [110, 22, 111, 21],
                "QPriorityLabel": [110, 50, 49, 16],
                "QSeparatedLine_1": [30, 259, 239, 1],
                "QTitle": [30, 110, 241, 31],
                "QDescription": [25, 140, 251, 101],
                "QPriority": [163, 49, 21, 21],
                "QStartButton": [240, 280, 31, 31],
                "QEditButton": [70, 280, 31, 31],
                "QRemoveButton": [30, 280, 31, 31]
            }

            # Create scroll area for dictionaries
            scrollArea = QScrollArea(self.dictionaryParent)
            scrollArea.setGeometry(10, 120, 441, 361)
            scrollArea.setWidgetResizable(True)
            scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            scrollArea.setStyleSheet(
                """QScrollBar:vertical {
                    border: none;
                    background-color: none;
                    width: 8px;
                    border-radius: 4px;
                }

                /*  HANDLE BAR VERTICAL */
                QScrollBar::handle:vertical {
                    background-color: rgb(180, 180, 180);
                    min-height: 50px;
                    border-radius: 4px;
                    margin: 0;
                }
                QScrollBar::handle:vertical:hover{
                    background-color: rgb(200, 200, 200);
                }
                QScrollBar::handle:vertical:pressed {
                    background-color: rgb(160, 160, 160);
                }

                /* BTN TOP - SCROLLBAR */
                QScrollBar::add-line:vertical {
                    height: 0px;
                    subcontrol-position: bottom;
                    subcontrol-origin: margin;
                    width: 0px;
                    background-color: rgb(255, 255, 255);
                }

                QScrollBar::sub-line:vertical {
                    height: 0px;
                    subcontrol-position: top;
                    subcontrol-origin: margin;
                    width: 0px;
                    background-color: rgb(255, 255, 255);
                }

                QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                    background-color: none;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background-color: none;
                }


                """
            )

            # Create widget to set a layout on
            scrollWidget = QWidget()

            # Create a layout and set it on widget
            scrollLayout = QVBoxLayout(scrollWidget)

            # Set content margins (it's basically margins on each side of the scrollArea widget)
            scrollLayout.setContentsMargins(75, 20, 0, 30)

            # Set spacing between content inside the scrollArea widget (in our case on the layout)
            scrollLayout.setSpacing(30)

            # Create a frame for dictionaries to be on
            frame = QFrame()

            # Create a variable, that will be used to count the dictionaries and make for each a number
            number = 1

            for keys, values in dictionary.items():
                # Create a main frame for dictionary and set a specific settings to it
                mainFrame = QWidget(
                    parent=frame
                )

                mainFrame.setStyleSheet(
                    """
                    background-color: rgb(255, 255, 255);
                    border: none;
                    border-radius: 15px;
                    """
                )
                mainFrame.setObjectName(f"{keys}_mainFrame")
                mainFrame.setFixedSize(
                    geometry["QMainFrame"][0],
                    geometry["QMainFrame"][1]
                )

                shadowEffect = QGraphicsDropShadowEffect(self)
                shadowEffect.setBlurRadius(35)
                shadowEffect.setColor(QColor(240, 240, 240, 255))
                shadowEffect.setOffset(0, 2)

                # Apply the shadow effect to the widget
                mainFrame.setGraphicsEffect(shadowEffect)

                # Create an icon for dictionary and set a specific settings to it
                icon = QPushButton(
                    parent=mainFrame
                )

                icon.setIcon(QIcon("icons/dictionaryIcon_W.png"))
                icon.setIconSize(QSize(40, 40))
                icon.setStyleSheet(
                    f"""
                    background-color: rgb({values["color"]});
                    border: none;
                    border-radius: 15px;
                    """
                )
                icon.setObjectName(f"{keys}_icon")
                icon.setGeometry(
                    geometry["QIcon"][0],
                    geometry["QIcon"][1],
                    geometry["QIcon"][2],
                    geometry["QIcon"][3]
                )

                # Create a number of dictionary and set a specific settings to it
                numberOfTheDictionary = QLabel(
                    parent=mainFrame
                )

                numberOfTheDictionary.setFont(QFont("Montserrat SemiBold", 9))
                numberOfTheDictionary.setStyleSheet(
                    f"""
                    background-color: rgb({values['color']});
                    border: none;
                    border-radius: 5px;
                    color: rgba(255, 255, 255, 255);
                    """
                )
                numberOfTheDictionary.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
                numberOfTheDictionary.setObjectName(f"{keys}_numberOfDictionary_{str(number).capitalize()}")
                numberOfTheDictionary.setText(f"DICTIONARY: {number}")
                numberOfTheDictionary.setGeometry(
                    geometry["QNumberOfDictionary"][0],
                    geometry["QNumberOfDictionary"][1],
                    geometry["QNumberOfDictionary"][2],
                    geometry["QNumberOfDictionary"][3]
                )

                # Create a priority label (number of dictionary) and set a specific settings to it
                priorityLabel = QLabel(
                    parent=mainFrame
                )
                priorityLabel.setFont(QFont("Montserrat", 9))

                priorityLabel.setStyleSheet(
                    """
                    background-color: none;
                    border: none;
                    """
                )
                priorityLabel.setObjectName(f"{keys}_priorityLabel")
                priorityLabel.setText("Priority:")
                priorityLabel.setGeometry(
                    geometry["QPriorityLabel"][0],
                    geometry["QPriorityLabel"][1],
                    geometry["QPriorityLabel"][2],
                    geometry["QPriorityLabel"][3]
                )

                # Create a priority icon for the dictionary and set a specific settings to it
                priority = QPushButton(
                    parent=mainFrame
                )

                priority.setStyleSheet(
                    f"""
                    background-color: rgb({values["priority"]["color"]});
                    border: none;
                    border-radius: 7px;
                    color: rgb(255, 255, 255);
                    """
                )
                priority.setFont(QFont("Montserrat SemiBold", 9))

                priority.setText(values["priority"]["number"])
                priority.setObjectName(f"{keys}_priorityButton")
                priority.setGeometry(
                    geometry["QPriority"][0],
                    geometry["QPriority"][1],
                    geometry["QPriority"][2],
                    geometry["QPriority"][3]
                )

                # Create a title label (name of dictionary) and set a specific settings to it
                title = QLineEdit(
                    parent=mainFrame
                )
                font = QFont("Montserrat")
                font.setBold(True)
                font.setPointSize(15)
                title.setFont(font)

                title.setStyleSheet(
                    """
                    background-color: rgba(255, 255, 255, 0);
                    border: none;
                    """
                )

                title.setReadOnly(True)
                title.setObjectName(f"{keys}_title")
                title.setText(f"{keys}")
                title.setGeometry(
                    geometry["QTitle"][0],
                    geometry["QTitle"][1],
                    geometry["QTitle"][2],
                    geometry["QTitle"][3]
                )

                # Create a description for the dictionary and set a specific settings to it
                description = QPlainTextEdit(
                    parent=mainFrame
                )
                font = QFont("Montserrat")
                font.setItalic(True)
                font.setPointSize(9)
                description.setFont(font)

                description.setPlainText(values["description"])
                description.setStyleSheet(
                    """
                    background-color: rgba(255, 255, 255, 0);
                    border: none;
                    """
                )
                description.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
                description.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                description.setReadOnly(True)
                description.setObjectName(f"{keys}_description")
                description.setGeometry(
                    geometry["QDescription"][0],
                    geometry["QDescription"][1],
                    geometry["QDescription"][2],
                    geometry["QDescription"][3]
                )

                separatedLine = QLabel(
                    parent=mainFrame
                )
                separatedLine.setStyleSheet(
                    """QLabel {
                        background-color: rgb(240, 240, 240);
                        border: none;
                    }"""
                )
                separatedLine.setObjectName(f"{keys}_separatedLine")
                separatedLine.setGeometry(
                    geometry["QSeparatedLine_1"][0],
                    geometry["QSeparatedLine_1"][1],
                    geometry["QSeparatedLine_1"][2],
                    geometry["QSeparatedLine_1"][3],
                )

                # Create a remove button to remove a dictionary and set a specific settings to it
                removeButton = QPushButton(
                    parent=mainFrame
                )
                removeButton.setIcon(QIcon("icons/trashIcon_W.png"))
                removeButton.setIconSize(QSize(16, 16))
                removeButton.setStyleSheet(
                    """QPushButton {
                        border: none;
                        background-color: rgb(255, 103, 103);
                        border-radius: 7px;
                    }

                    QPushButton::hover {
                        background-color: rgb(255, 123, 123);
                    }

                    QPushButton:pressed {
                        background-color: rgb(255, 91, 91);
                    }"""
                )
                removeButton.setObjectName(f"{keys}_removeDictionaryButton")
                removeButton.setCursor(Qt.CursorShape.PointingHandCursor)
                removeButton.setGeometry(
                    geometry["QRemoveButton"][0],
                    geometry["QRemoveButton"][1],
                    geometry["QRemoveButton"][2],
                    geometry["QRemoveButton"][3]
                )

                # When button being clicked, the other function will start
                removeButton.clicked.connect(self.open_a_choice_window_and_set_a_signal)

                # # Create an edit button to edit a dictionary and set a specific settings to it
                editButton = QPushButton(
                    parent=mainFrame
                )
                editButton.setIcon(QIcon("icons/editSomethingIcon_W.png"))
                editButton.setIconSize(QSize(16, 16))
                editButton.setStyleSheet(
                    """QPushButton {
                        border: none;
                        background-color: rgb(0, 70, 190);
                        border-radius: 7px;
                    }

                    QPushButton:hover {
                        background-color: rgba(0, 70, 190, 220);
                    }

                    QPushButton:pressed {
                        background-color: rgba(0, 70, 190, 240);
                    }"""
                )
                editButton.setObjectName(f"{keys}_editDictionaryButton")
                editButton.setCursor(Qt.CursorShape.PointingHandCursor)
                editButton.setGeometry(
                    geometry["QEditButton"][0],
                    geometry["QEditButton"][1],
                    geometry["QEditButton"][2],
                    geometry["QEditButton"][3]
                )

                # When button being clicked, the other function will start
                editButton.clicked.connect(self.edit_a_dictionary)

                # Create a button to open a dictionary and set a specific settings to it
                startButton = QPushButton(
                    parent=mainFrame
                )
                startButton.setIcon(QIcon("icons/startSomethingIcon_W.png"))
                startButton.setIconSize(QSize(15, 15))
                startButton.setStyleSheet(
                    f"""
                    border: none;
                    background-color: rgb({values["color"]});
                    border-radius: 7px;
                    """
                )
                startButton.setObjectName(f"{keys}_startLearning")
                startButton.setCursor(Qt.CursorShape.PointingHandCursor)
                startButton.setGeometry(
                    geometry["QStartButton"][0],
                    geometry["QStartButton"][1],
                    geometry["QStartButton"][2],
                    geometry["QStartButton"][3]
                )

                # When button being clicked, the other function will start
                startButton.clicked.connect(self.process_of_vocabularies)

                # Add a mainFrame widget to the layout
                scrollLayout.addWidget(mainFrame)

                # Plus 1 to the variable "number"
                number += 1

            # Set the layout to the frame that holds the content
            frame.setLayout(scrollLayout)

            # Set the widget to the scrollArea widget
            scrollArea.setWidget(frame)

            # Show the scrollArea widget
            scrollArea.show()

    def set_timer_to_refresh_the_list_of_dictionaries(self, event):

        """

        This function sets the timer of 0.1 sec to refresh the list of dictionaries, otherwise that would be
        so sharp looking

        :param event: event object that comes from closeEvent
        :return:
        """

        # Set the timer, after which the other function is going to start
        timer = QTimer(self)

        # Make the timer works once
        timer.setSingleShot(True)

        # Set the action that should be done after finishing the timer
        timer.timeout.connect(self.refresh_list_of_the_dictionaries)

        # Set the duration of the timer
        timer.start(100)

        # for name in locals():
        #     del name
        #
        #     gc.collect()

    def edit_a_dictionary(self):

        """

        This function edits a dictionary

        :return:
        """

        # Get clicked object of a button
        sender = self.sender()

        # Get the parent widget from clicked object of a button
        parentFrameOfTheButton = sender.parentWidget()

        # Find children of the parent widget
        findChildren = [
            parentFrameOfTheButton.findChildren(QLineEdit),
            parentFrameOfTheButton.findChildren(QPlainTextEdit)
        ]

        # Get texts from children objects
        texts = [
            findChildren[0][0].text(),
            findChildren[1][0].toPlainText()
        ]

        # Get connection to the database
        connection = create_connection_to_the_database(f'database/database.db')

        # Open a host to make connection to succeed
        with connection:
            # Get data from database
            getDataFromDatabase = select_data_in_the_database(connection, "dictionary",
                                                              LocalDatabase.userLoginData["email"])

            # ---------------------------------------------------------------------------------------------------
            # The dictionary, that we got in the variable "getDataFromDatabase" gives us the string of the dict,
            # that's white we need to convert the string into an object "dict" using the library "json"
            # ---------------------------------------------------------------------------------------------------
            dictionary = json.loads(getDataFromDatabase[0][0].replace("'", ""))

            # Save specific data to the local database dict variable
            EditADictionary.dataToFillUp.update(
                {
                    "name": texts[0],
                    "description": texts[1],
                    "color": dictionary[texts[0]]["color"],
                    "priority": dictionary[texts[0]]["priority"]
                }
            )

            # Set the signal in the local database variable
            EditADictionary.signal = True

        # Create a blacked out widget for MainWindow
        widget = QWidget(self)
        widget.setStyleSheet(
            """QWidget {
                background-color: rgba(0, 0, 0, 50);
                border: none;
            }"""
        )
        widget.setGeometry(0, 0, 1280, 720)
        widget.setParent(self.mainParent)

        # Save the object of the widget in local database
        BlackedOutWidget.widget = widget

        # Make the setting to a child's window
        window = windows.CreatingAVocabularyWindow()
        window.setParent(widget)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
        window.setWindowModality(QtCore.Qt.WindowModality.WindowModal)

        window.closeEvent = self.set_timer_to_refresh_the_list_of_dictionaries

        widget.show()
        window.show()

        del window, widget
        gc.collect()

        # for name in locals():
        #     del name
        #
        #     gc.collect()

        return

    def open_a_choice_window_and_set_a_signal(self):

        """

        This function shows a choice window, and asks whether user wants to remove a dictionary or not

        :return:
        """

        # Make the setting to a child's window
        window = windows.ChoiceWindow()
        window.setParent(self)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
        window.setWindowModality(QtCore.Qt.WindowModality.WindowModal)

        # When window closed, the signal to call other function works out
        window.closeEvent = self.remove_a_dictionary

        # Save clicked object of a button to the local variable
        self.object = self.sender()

        # Create a blacked out widget for MainWindow
        widget = QWidget(self)
        widget.setStyleSheet(
            """QWidget {
                background-color: rgba(0, 0, 0, 50);
                border: none;
            }"""
        )
        widget.setGeometry(0, 0, 1280, 720)
        widget.setParent(self.mainParent)
        widget.show()

        # Save the object of the widget in local database
        BlackedOutWidget.widget = widget

        window.show()

        del window, widget
        gc.collect()

        # for name in locals():
        #     del name
        #
        #     gc.collect()

        return

    def remove_a_dictionary(self, event):

        """

        This function removes a dictionary

        :param event:
        :return:
        """

        # Check if the removing signal equals True
        if RemoveSomething.signal:
            # Get connection to the database
            connection = create_connection_to_the_database(f'database/database.db')

            # Get the parent widget from clicked object of a button in the local variable
            parentFrameOfTheButton = self.object.parentWidget()

            # Find children from parent widget of clicked object of a button
            findChild = parentFrameOfTheButton.findChildren(QLineEdit)

            # Get texts from children objects
            text = findChild[0].text()

            # Open a host to make connection to succeed
            with connection:
                # Get data from database
                getDataFromDatabase = select_data_in_the_database(connection, "dictionary",
                                                                  LocalDatabase.userLoginData["email"])

                # ---------------------------------------------------------------------------------------------------
                # The dictionary, that we got in the variable "getDataFromDatabase" gives us the string of the dict,
                # that's white we need to convert the string into an object "dict" using the library "json"
                # ---------------------------------------------------------------------------------------------------
                dictionary = json.loads(getDataFromDatabase[0][0].replace("'", ""))

                # Remove the key from dict
                dictionary.pop(text)

                # Update information in the database
                update_data_in_the_database(connection, "dictionary = ?",
                                            (json.dumps(dictionary), LocalDatabase.userLoginData["email"]))

            # Call the function to set the timer to refresh the list of the dictionaries
            self.set_timer_to_refresh_the_list_of_dictionaries(event=None)

            # for name in locals():
            #     del name
            #
            #     gc.collect()

            return

    def process_of_vocabularies(self):

        """

        This function shows dictionary's  window with its name and description so user can create custom
        dictionaries and words in it

        :return:
        """

        # Get clicked object of a button
        sender = self.sender()

        # Get parent widget from clicked object of a button
        parentFrameOfTheButton = sender.parentWidget()

        # Get children from parent widget of clicked object of a button
        children = [
            parentFrameOfTheButton.findChildren(QLineEdit),
            parentFrameOfTheButton.findChildren(QPlainTextEdit)
        ]

        # Get texts from children widgets
        texts = [
            children[0][0].text(),
            children[1][0].toPlainText()
        ]

        # Set texts to the needed widgets in different window
        window = windows.DictionaryAreaWindow()
        window.uiDictionaryAreaWindow.nameOfTheDictionary.setText(texts[0])
        window.uiDictionaryAreaWindow.descriptionOfTheDictionary.setText(texts[1])

        # Save name and description to the variable of the local database
        LocalDatabase.temporaryDictionaryData = {
            "name": texts[0],
            "description": texts[1]
        }

        # Close current window and show another
        self.parentWindow.close()
        window.show()

        # for name in locals():
        #     del name
        #
        #     gc.collect()

        return
