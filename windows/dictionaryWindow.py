import json
import pyttsx3

from PySide6.QtCore import (Qt, QPoint, QSize, QTimer)
from PySide6.QtWidgets import (QMainWindow, QGraphicsDropShadowEffect, QScrollArea, QWidget, QVBoxLayout, QFrame,
                               QLabel, QPushButton, QStackedWidget, QPlainTextEdit, QHBoxLayout, QLineEdit)
from PySide6.QtGui import (QColor, QIcon, QFont, QPixmap)
from PySide6 import QtCore

from uiPythonFiles.ui_DictionaryForm import Ui_DictionaryAreaWindow
from database.database import update_data_in_the_database, select_data_in_the_database, create_connection_to_the_database
from localDatabase.local_database import LocalDatabase, BlackedOutWidget, CustomDictionaries, EditACustomDictionary, \
    RemoveSomething, EditAWord
import windows
import random

import icons.icons_rc


class DictionaryAreaWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialization widgets
        self.stackedWidget = None

        # Initialization features
        self.clickPosition = None
        self.customDictionaryMethods = None

        self.uiDictionaryAreaWindow = Ui_DictionaryAreaWindow()
        self.uiDictionaryAreaWindow.setupUi(self)

        self.init_UI()
        self.mouse_events()

    def init_UI(self):

        """
        This function makes some settings to a window and also set the needed information
        to a needed widgets

        :return: None
        """

        # Set specific settings to the window
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Create a dynamic stacked widget
        self.stackedWidget = QStackedWidget(self.uiDictionaryAreaWindow.mainFrame)
        self.stackedWidget.setStyleSheet(
            """QStackedWidget {
                background-color: rgb(255, 255, 255);
                border: none;
                border-radius: 7px;
            }"""
        )
        self.stackedWidget.setGeometry(340, 130, 551, 431)

        # Create an instant to the class with methods, so later we can use them
        self.customDictionaryMethods = CustomDictionaryMethods(
            parent_window=self.uiDictionaryAreaWindow,
            main_parent_widget=self.uiDictionaryAreaWindow.mainFrame,
            dictionary_parent=self.uiDictionaryAreaWindow.frameOfCustomDictionaries,
            stacked_widget=self.stackedWidget,
            parent_self=self
        )

    def mouse_events(self):

        """
        This function makes mouse events and responses to them

        :return: None
        """

        # Make mouse events for each button on window and responds
        self.uiDictionaryAreaWindow.infoFrame.mouseMoveEvent = self.move_window

        self.uiDictionaryAreaWindow.goBackButton.clicked.connect(self.show_the_main_window)
        self.uiDictionaryAreaWindow.addACustomDictionaryButton.clicked.connect(self.customDictionaryMethods.create_a_custom_dictionary)
        self.uiDictionaryAreaWindow.refreshTheListOfCustomDictionariesButton.clicked.connect(self.customDictionaryMethods.refresh_list_of_the_custom_dictionaries)

        # When button clicked, close the window
        self.uiDictionaryAreaWindow.closeThewindowButton.clicked.connect(lambda: self.close())

        # When button clicked, minimize the window
        self.uiDictionaryAreaWindow.minimizeTheWindowButton.clicked.connect(lambda: self.showMinimized())

    def show_the_main_window(self):

        """

        This function closes current window and open mainWindow

        :return:
        """

        self.close()
        window = windows.MainWindow()
        window.uiMainWindow.stackedWidget.setCurrentIndex(0)
        window.show()

    # ----------------------------
    # FUNCTIONS TO MOVE THE WINDOW
    # ----------------------------
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


class CustomDictionaryMethods(QMainWindow):
    def __init__(self, parent_self, parent_window, main_parent_widget, dictionary_parent, stacked_widget):
        super(CustomDictionaryMethods, self).__init__()

        # Initialize widgets
        self.parentSelf = parent_self
        self.parentWindow = parent_window
        self.mainParentWidget = main_parent_widget
        self.dictionaryParent = dictionary_parent
        self.stackedWidget = stacked_widget

        self.window = None

        self.viewing_the_words = {}

        # Initialize features
        self.addAWordButton = None
        self.refreshTheWordButton = None
        self.randomizeTheWordsButton = None
        self.trainButton = None

        self.obj = None

        # Create an instant to the class with methods, so later we can use them
        self.wordMethods = WordMethods(
            parent_window=self.parentWindow,
            main_parent_widget=self.mainParentWidget,
            stacked_widget=self.stackedWidget,
            viewing_the_words=None,
        )

    def refresh_list_of_the_custom_dictionaries(self):

        """

        This function refreshes the lift of the custom dictionaries by taking data from the local database

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
                LocalDatabase.userLoginData["email"]
            )

        # Check if there is data in database
        if not getDataFromDatabase[0][0]:

            # If not, do nothing
            pass

        # If there is data in database...
        else:

            # ---------------------------------------------------------------------------------------------------
            # The dictionary, that we got in the variable "getDataFromDatabase" gives us the string of the dict,
            # that's white we need to convert the string into an object "dict" using the library "json"
            # ---------------------------------------------------------------------------------------------------
            dictionary = json.loads(getDataFromDatabase[0][0].replace("'", ""))

            # Save the positions and sizes in the dict, so later we can use it easily
            geometry = {
                "QNumberOfCustomDictionary": [27, 15, 81, 21],
                "QTitle": [27, 60, 151, 20],
                "QDescription": [23, 80, 151, 61],
                "QRemoveButton": [25, 197, 31, 31],
                "QEditButton": [65, 197, 31, 31],
                "QStartButton": [145, 197, 31, 31],
                "QSeparatedLine": [27, 180, 145, 1],
                "QAddButton": [210, 20, 31, 31],
                "QRefreshTheWordsButton": [260, 20, 31, 31],
                "QRandomizeTheWordsButton": [310, 20, 31, 31],
                "QSeparatedLineForTheWords": [30, 70, 495, 1],
                "QTitleOfCustomDictionary": [20, 90, 201, 21],
                "QDescriptionOfCustomDictionary": [16, 110, 331, 41],
                "QTrainButton": [420, 20, 101, 31]
            }

            # Create scroll area for custom dictionaries and set specific settings to it
            scrollArea = QScrollArea(self.dictionaryParent)
            scrollArea.setGeometry(20, 150, 261, 261)
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

            scrollWidget = QWidget()
            scrollLayout = QVBoxLayout(scrollWidget)
            scrollLayout.setContentsMargins(25, 10, 10, 10)

            # Set spacing between content inside the scrollArea widget (in our case on the layout)
            scrollLayout.setSpacing(30)

            frame = QFrame()
            number = 1

            # Check if there are custom dictionaries in the main dictionary folder
            if dictionary[self.parentWindow.nameOfTheDictionary.text()].get("custom_dictionaries"):

                # Get custom dictionaries data
                customDictionaries = dictionary[self.parentWindow.nameOfTheDictionary.text()].get("custom_dictionaries").items()

                # Make a loop and separate data in keys and values, to manipulate them easier
                for keys, values in customDictionaries:

                    # Create a main widget and set the specific settings to it
                    mainWidget = QWidget(
                        parent=frame
                    )
                    mainWidget.setStyleSheet(
                        """QWidget {
                            background-color: rgb(255, 255, 255);
                            border-radius: 7px;
                            border: none;
                        }"""
                    )
                    mainWidget.setObjectName(f"{keys}_main_frame")
                    mainWidget.setFixedSize(201, 241)

                    # Create a shadow effect for main widget
                    shadowEffect = QGraphicsDropShadowEffect(self)
                    shadowEffect.setBlurRadius(35)
                    shadowEffect.setColor(QColor(240, 240, 240, 255))
                    shadowEffect.setOffset(0, 2)

                    # Apply the shadow effect to the widget
                    mainWidget.setGraphicsEffect(shadowEffect)

                    # Create a label that shows number of the custom dictionary and set the specific settings to it
                    numberOfTheCustomDictionary = QLabel(
                        parent=mainWidget
                    )
                    numberOfTheCustomDictionary.setFont(QFont("Montserrat SemiBold", 10))
                    numberOfTheCustomDictionary.setStyleSheet(
                        """QLabel {
                            background-color: rgb(185, 123, 255);
                            border: none;
                            border-radius: 10px;
                            color: rgb(255, 255, 255);
                        }"""
                    )
                    numberOfTheCustomDictionary.setAlignment(
                        Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
                    numberOfTheCustomDictionary.setObjectName(f"{keys}_numberOfDictionary{str(number).capitalize()}")
                    numberOfTheCustomDictionary.setText(f"CD: {number}")
                    numberOfTheCustomDictionary.setGeometry(
                        geometry["QNumberOfCustomDictionary"][0],
                        geometry["QNumberOfCustomDictionary"][1],
                        geometry["QNumberOfCustomDictionary"][2],
                        geometry["QNumberOfCustomDictionary"][3]
                    )

                    # Create a title (name of the dictionary) and set the specific settings to it
                    title = QLabel(
                        parent=mainWidget
                    )
                    title.setFont(QFont("Montserrat SemiBold", 13))
                    title.setStyleSheet(
                        """QLabel {
                            background-color: none;
                            border: none;
                        }"""
                    )
                    title.setObjectName(f"{keys}_title")
                    title.setText(f"{keys}")
                    title.setGeometry(
                        geometry["QTitle"][0],
                        geometry["QTitle"][1],
                        geometry["QTitle"][2],
                        geometry["QTitle"][3]
                    )

                    # Create description on the custom dictionary and set the specific settings to it
                    description = QPlainTextEdit(
                        parent=mainWidget
                    )
                    font = QFont("Montserrat")
                    font.setItalic(True)
                    font.setPointSize(9)
                    description.setFont(font)

                    description.setStyleSheet(
                        """QPlainTextEdit {
                            background-color: none;
                            border: none;
                        }"""
                    )
                    description.setObjectName(f"{keys}_descriptionOfTheCustomDictionary")

                    if not values:
                        pass
                    else:
                        description.setPlainText(f"{values['description']}".upper())

                    description.setGeometry(
                        geometry["QDescription"][0],
                        geometry["QDescription"][1],
                        geometry["QDescription"][2],
                        geometry["QDescription"][3]
                    )
                    description.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
                    description.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                    description.setReadOnly(True)

                    # Create a separated line and set the specific settings to it
                    separatedLine = QLabel(
                        parent=mainWidget
                    )
                    separatedLine.setStyleSheet(
                        """QLabel {
                            background-color: rgb(240, 240, 240);
                            border: none;
                        }"""
                    )
                    separatedLine.setObjectName(f"{keys}_separatedLine")
                    separatedLine.setGeometry(
                        geometry["QSeparatedLine"][0],
                        geometry["QSeparatedLine"][1],
                        geometry["QSeparatedLine"][2],
                        geometry["QSeparatedLine"][3]
                    )

                    # Create an edit button and set the specific settings to it
                    editButton = QPushButton(
                        parent=mainWidget
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

                    # When edit button pressed, call other function to proceed
                    editButton.clicked.connect(self.edit_a_custom_dictionary)

                    # Create a remove button and set the specific settings to it
                    removeButton = QPushButton(
                        parent=mainWidget
                    )
                    removeButton.setIcon(QIcon("icons/trashIcon_W.png"))
                    removeButton.setIconSize(QSize(16, 16))
                    removeButton.setStyleSheet(
                        """QPushButton {
                            border: none;
                            background-color: rgb(255, 85, 70);
                            border-radius: 7px;
                        }
        
                        QPushButton:hover {
                            background-color: rgba(255, 85, 70, 220);
                        }
                        
                        QPushButton:pressed {
                            background-color: rgba(255, 85, 70, 240);
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

                    # When remove button clicked, call other function to proceed
                    removeButton.clicked.connect(self.open_a_choice_window_and_set_a_signal)

                    # Create a start button and set the specific settings to it
                    startButton = QPushButton(
                        parent=mainWidget
                    )

                    startButton.setIcon(QIcon("icons/startSomethingIcon_W.png"))
                    startButton.setIconSize(QSize(16, 16))
                    startButton.setStyleSheet(
                        """QPushButton {
                            border: none;
                            background-color: rgb(255, 99, 200);
                            border-radius: 7px;
                        }

                        QPushButton:hover {
                            background-color: rgba(255, 99, 200, 220);
                        }

                        QPushButton:pressed {
                            background-color: rgba(255, 99, 200, 240);
                        }"""
                    )
                    startButton.setObjectName(f"{keys}_buttonForDictionary")
                    startButton.setCursor(Qt.CursorShape.PointingHandCursor)
                    startButton.setGeometry(
                        geometry["QStartButton"][0],
                        geometry["QStartButton"][1],
                        geometry["QStartButton"][2],
                        geometry["QStartButton"][3]
                    )

                    # When start button clicked, call other function to proceed
                    startButton.clicked.connect(self.show_the_page_with_words_in_custom_dictionary)

                    # Create a page on the stacked widget to connect custom dictionary to it
                    page = QWidget(self)
                    page.setObjectName(f"{keys}_pageOfTheWords")
                    page.setGeometry(0, 0, 551, 431)
                    page.setStyleSheet(
                        """QWidget {
                            background-color: rgb(255, 255, 255);
                            border: none;
                            border-radius: 7px;
                        }"""
                    )

                    # Create a button to add a word to a custom dictionary
                    self.addAWordButton = QPushButton(
                        parent=page
                    )
                    icon = QIcon("icons/addSomethingIcon_W.png")
                    self.addAWordButton.setIcon(icon)
                    self.addAWordButton.setIconSize(QSize(16, 16))
                    self.addAWordButton.setStyleSheet(
                        """QPushButton {
                            border: none;
                            background-color: rgb(106, 203, 255);
                            border-radius: 7px;
                        }

                        QPushButton:hover {
                            background-color: rgba(106, 203, 255, 220);
                        }
                        QPushButton:pressed {
                            background-color: rgba(106, 203, 255, 240);
                        }"""
                    )
                    self.addAWordButton.setObjectName(f"{keys}_addAWord")
                    self.addAWordButton.setCursor(Qt.CursorShape.PointingHandCursor)
                    self.addAWordButton.setGeometry(
                        geometry["QAddButton"][0],
                        geometry["QAddButton"][1],
                        geometry["QAddButton"][2],
                        geometry["QAddButton"][3]
                    )

                    # Create a button to refresh the word in a custom dictionary
                    self.refreshTheWordButton = QPushButton(
                        parent=page
                    )
                    icon = QIcon("icons/refreshIcon_W.png")
                    self.refreshTheWordButton.setIcon(icon)
                    self.refreshTheWordButton.setIconSize(QSize(16, 16))
                    self.refreshTheWordButton.setStyleSheet(
                        """QPushButton {
                            border: none;
                            background-color: rgb(87, 255, 185);
                            border-radius: 7px;
                        }

                        QPushButton:hover {
                            background-color: rgba(87, 255, 185, 220);
                        }
                        QPushButton:pressed {
                            background-color: rgba(87, 255, 185, 240);
                        }"""
                    )
                    self.refreshTheWordButton.setObjectName(f"{keys}_refreshTheWords")
                    self.refreshTheWordButton.setCursor(Qt.CursorShape.PointingHandCursor)
                    self.refreshTheWordButton.setGeometry(
                        geometry["QRefreshTheWordsButton"][0],
                        geometry["QRefreshTheWordsButton"][1],
                        geometry["QRefreshTheWordsButton"][2],
                        geometry["QRefreshTheWordsButton"][3]
                    )

                    # Create a button to randomize the words in a custom dictionary
                    self.randomizeTheWordsButton = QPushButton(
                        parent=page
                    )
                    icon = QIcon("icons/randomizeIcon_W.png")
                    self.randomizeTheWordsButton.setIcon(icon)
                    self.randomizeTheWordsButton.setIconSize(QSize(16, 16))
                    self.randomizeTheWordsButton.setStyleSheet(
                        """QPushButton {
                            border: none;
                            background-color: rgb(170, 110, 159);
                            border-radius: 7px;
                        }

                        QPushButton:hover {
                            background-color: rgba(170, 110, 159, 220);
                        }
                        QPushButton:pressed {
                            background-color: rgba(170, 110, 159, 240);
                        }"""
                    )
                    self.randomizeTheWordsButton.setObjectName(f"{keys}_randomizeTheWords")
                    self.randomizeTheWordsButton.setCursor(Qt.CursorShape.PointingHandCursor)
                    self.randomizeTheWordsButton.setGeometry(
                        geometry["QRandomizeTheWordsButton"][0],
                        geometry["QRandomizeTheWordsButton"][1],
                        geometry["QRandomizeTheWordsButton"][2],
                        geometry["QRandomizeTheWordsButton"][3]
                    )

                    # Create a button to randomize the words in a custom dictionary
                    self.trainButton = QPushButton(
                        parent=page
                    )

                    font = QFont("Montserrat")
                    font.setBold(True)
                    font.setPointSize(13)
                    self.trainButton.setFont(font)

                    self.trainButton.setText("TRAIN")

                    self.trainButton.setStyleSheet(
                        """QPushButton {
                            background-color: rgb(56, 236, 113);
                            border-radius: 7px;
                            color: rgb(255, 255, 255);
                            border: none;
                        }

                        QPushButton:hover {
                            background-color: rgb(69, 241, 124);
                        }

                        QPushButton:pressed {
                            background-color: rgb(48, 221, 103);
                        }"""
                    )
                    self.trainButton.setObjectName(f"{keys}_train")
                    self.trainButton.setCursor(Qt.CursorShape.PointingHandCursor)
                    self.trainButton.setGeometry(
                        geometry["QTrainButton"][0],
                        geometry["QTrainButton"][1],
                        geometry["QTrainButton"][2],
                        geometry["QTrainButton"][3]
                    )

                    # Create a separated line for the words and set the specific settings to it
                    separatedLineForTheWords = QLabel(
                        parent=page
                    )

                    separatedLineForTheWords.setStyleSheet(
                        """QLabel {
                            background-color: rgb(240, 240, 240);
                            border: none;
                        }"""
                    )
                    separatedLineForTheWords.setObjectName(f"{keys}_separatedLine")
                    separatedLineForTheWords.setGeometry(
                        geometry["QSeparatedLineForTheWords"][0],
                        geometry["QSeparatedLineForTheWords"][1],
                        geometry["QSeparatedLineForTheWords"][2],
                        geometry["QSeparatedLineForTheWords"][3]
                    )

                    # Create a title of the custom dictionary to show it on the stacked widget
                    titleOfTheCustomDictionary = QLabel(
                        parent=page
                    )
                    titleOfTheCustomDictionary.setFont(QFont("Montserrat SemiBold", 15))
                    titleOfTheCustomDictionary.setStyleSheet(
                        """QLabel {
                            background-color: none;
                            border: none;
                        }"""
                    )
                    titleOfTheCustomDictionary.setObjectName(f"{keys}_titleOfCustomDictionaryDisplay")
                    titleOfTheCustomDictionary.setText(f"{keys}")
                    titleOfTheCustomDictionary.setGeometry(
                        geometry["QTitleOfCustomDictionary"][0],
                        geometry["QTitleOfCustomDictionary"][1],
                        geometry["QTitleOfCustomDictionary"][2],
                        geometry["QTitleOfCustomDictionary"][3]
                    )

                    # Create a description of the custom dictionary to show it on the stacked widget
                    descriptionOfTheCustomDictionary = QPlainTextEdit(
                        parent=page
                    )
                    font = QFont("Montserrat")
                    font.setItalic(True)
                    font.setPointSize(10)
                    descriptionOfTheCustomDictionary.setFont(font)

                    descriptionOfTheCustomDictionary.setStyleSheet(
                        """QPlainTextEdit {
                            background-color: none;
                            border: none;
                        }"""
                    )
                    descriptionOfTheCustomDictionary.setObjectName(f"{keys}_descriptionOfTheCustomDictionaryDisplay")

                    if not values:
                        pass
                    else:
                        descriptionOfTheCustomDictionary.setPlainText(f"{values['description']}".upper())

                    descriptionOfTheCustomDictionary.setGeometry(
                        geometry["QDescriptionOfCustomDictionary"][0],
                        geometry["QDescriptionOfCustomDictionary"][1],
                        geometry["QDescriptionOfCustomDictionary"][2],
                        geometry["QDescriptionOfCustomDictionary"][3]
                    )
                    descriptionOfTheCustomDictionary.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
                    descriptionOfTheCustomDictionary.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                    descriptionOfTheCustomDictionary.setReadOnly(True)

                    # Add page to the stacked widget
                    self.stackedWidget.addWidget(page)

                    # Save name of the custom dictionary, page object and index of the page
                    self.viewing_the_words.update(
                        {
                            titleOfTheCustomDictionary.text(): {
                                "page": page,
                                "index": 0 if not self.viewing_the_words else len(self.viewing_the_words.keys()) + 1
                            }
                        }
                    )

                    # Add a main widget to the scrollLayout
                    scrollLayout.addWidget(mainWidget)

                    number += 1

                # Create an instant to the class with methods, so later we can use them
                self.wordMethods = WordMethods(
                    parent_window=self.parentWindow,
                    main_parent_widget=self.mainParentWidget,
                    stacked_widget=self.stackedWidget,
                    viewing_the_words=self.viewing_the_words
                )

                # When buttons clicked, call other functions to proceed
                self.addAWordButton.clicked.connect(self.wordMethods.add_a_custom_word_to_a_custom_dictionary)
                self.refreshTheWordButton.clicked.connect(self.wordMethods.refresh_the_list_of_the_words)
                self.randomizeTheWordsButton.clicked.connect(self.wordMethods.randomize_the_words)
                self.trainButton.clicked.connect(self.show_the_training_window)

                # Create a dashboard empty page
                page = QWidget(self)
                page.setObjectName("dashboardPage")
                page.setGeometry(0, 0, 551, 431)
                page.setStyleSheet(
                    """QWidget {
                        background-color: rgb(255, 255, 255);
                        border: none;
                        border-radius: 7px;
                    }"""
                )

                # Add dashboard empty page to the stacked widget
                self.stackedWidget.addWidget(page)

                # Set dashboard empty page as a current widget
                self.stackedWidget.setCurrentWidget(page)

                # Save an object of the page in the local database
                CustomDictionaries.dashboardPage = page

                # Set the layout to the frame that holds the content
                frame.setLayout(scrollLayout)

                # Set the widget to the scrollArea widget
                scrollArea.setWidget(frame)

                # Show the scrollArea widget
                scrollArea.show()

            else:

                # Set the layout to the frame that holds the content
                frame.setLayout(scrollLayout)

                # Set the widget to the scrollArea widget
                scrollArea.setWidget(frame)

                # Show the scrollArea widget
                scrollArea.show()

            # Check if the removing signal equals True
            if RemoveSomething.signal:

                # Get the dashboard empty page from the local database
                dashboardPage = CustomDictionaries.dashboardPage

                # Set dashboard empty page as a current widget
                self.stackedWidget.setCurrentWidget(dashboardPage)

                # Set the removing signal to False
                RemoveSomething.signal = False

    def show_the_training_window(self):

        self.parentWindow.close()

        # Make the setting to a child's window
        window = windows.TrainingWindow()

        window.show()


    def show_the_page_with_words_in_custom_dictionary(self):

        """

        This functions shows the page that equivalents to clicked object's parent widget

        :return:
        """

        # Get object of clicked button
        sender = self.sender()

        # Get the name of the custom dictionary by the dictionary_parent of the clicked button
        parentLabel = sender.parent().findChildren(QLabel)[1].text()

        CustomDictionaries.temporaryCustomDictionaryData = {
            "customDictionaryName": parentLabel,
            "mainDictionaryName": self.parentWindow.nameOfTheDictionary.text()
        }

        # Get the page that connected to each custom dictionary
        page = self.viewing_the_words[parentLabel]["page"]

        # Set the current page to a stacked widget by the custom dictionary
        self.stackedWidget.setCurrentWidget(page)

    def set_timer_to_refresh_the_list_of_the_custom_dictionaries(self, event):

        """

        This function sets the timer of 0.1 seconds and calls other function to proceed

        :param event: event object that comes from closeEvent
        :return:
        """

        # Set the timer, after which the other function is going to start
        timer = QTimer(self)

        # Make the timer works once
        timer.setSingleShot(True)

        # Set the action that should be done after finishing the timer
        timer.timeout.connect(self.refresh_list_of_the_custom_dictionaries)

        timer.start(100)

    def edit_a_custom_dictionary(self):

        """

        This function edits a custom dictionary

        :return:
        """

        # Get clicked object
        sender = self.sender()

        # Get parent widget from the clicked object
        parentFrameOfTheButton = sender.parentWidget()

        # Get parent widget from parent widget of the clicked object
        parentFrameOfTheFrame = parentFrameOfTheButton.parentWidget()

        # Find children objects in the parent widget
        findChildren = [
            parentFrameOfTheFrame.findChildren(QLabel),
            parentFrameOfTheFrame.findChildren(QPlainTextEdit)
        ]

        # Get texts from children objects
        texts = [
            findChildren[0][1].text(),
            findChildren[1][0].toPlainText()
        ]

        # Save name and description in the dict of the local database
        EditACustomDictionary.dataToFillUp.update(
            {
                "name": texts[0],
                "description": texts[1]
            }
        )

        # Set the editing signal to True in the local database
        EditACustomDictionary.signal = True

        # Save the name of the main dictionary in the local database
        EditACustomDictionary.mainDictionary = self.parentWindow.nameOfTheDictionary.text()

        # Make the setting to a child's window
        window = windows.CustomDictionaryArea()
        window.setParent(self)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
        window.setWindowModality(QtCore.Qt.WindowModality.WindowModal)

        window.closeEvent = self.set_timer_to_refresh_the_list_of_the_custom_dictionaries

        # Create a blacked out widget for MainWindow
        widget = QWidget(self)
        widget.setStyleSheet(
            """QWidget {
                background-color: rgba(0, 0, 0, 50);
                border: none;
            }"""
        )
        widget.setGeometry(0, 0, 1280, 720)
        widget.setParent(self.mainParentWidget)
        widget.show()

        # Save the object of the widget in local database
        BlackedOutWidget.widget = widget

        window.show()

    def create_a_custom_dictionary(self):

        """

        This function shows a creating dictionary window on the screen

        :return:
        """

        # Create an instant for another window and set the specific settings to the window
        window = windows.CustomDictionaryArea()
        window.setParent(self)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
        window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        # Create a blacked out widget for MainWindow
        widget = QWidget(self)
        widget.setStyleSheet(
            """QWidget {
                background-color: rgba(0, 0, 0, 50);
                border: none;
            }"""
        )
        widget.setGeometry(0, 0, 1280, 720)
        widget.setParent(self.mainParentWidget)
        widget.show()

        # Save the object of the widget in local database
        BlackedOutWidget.widget = widget

        window.show()

    def open_a_choice_window_and_set_a_signal(self):

        """

        This function opens a choice window for removing word or custom dictionary and depends on the answer,
        does some job

        :return:
        """

        # Save clicked object to the local variable "self.obj"
        self.obj = self.sender()

        # Make the setting to a child's window
        window = windows.ChoiceWindow()
        window.setParent(self)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
        window.setWindowModality(QtCore.Qt.WindowModality.WindowModal)

        window.uiChoiceWindow.explanationLabel.setText("Are you sure you want to remove this custom dictionary?")

        window.closeEvent = self.remove_a_custom_dictionary

        # Create a blacked out widget for MainWindow
        widget = QWidget(self)
        widget.setStyleSheet(
            """QWidget {
                background-color: rgba(0, 0, 0, 50);
                border: none;
            }"""
        )
        widget.setGeometry(0, 0, 1280, 720)
        widget.setParent(self.mainParentWidget)
        widget.show()

        # Save the object of the widget in local database
        BlackedOutWidget.widget = widget

        window.show()

    def remove_a_custom_dictionary(self, event):

        """

        This function removes a custom dictionary from database

        :param event: event object that comes from closeEvent
        :return:
        """

        # Check if the removing signal in the local database equals True
        if RemoveSomething.signal:

            # Get parent widget from the save clicked object in the local variable "self.obj"
            parentFrameOfTheButton = self.obj.parentWidget()

            # Get child (QLabel) from parent widget
            findChild = parentFrameOfTheButton.findChildren(QLabel)

            # Get text from child's object
            text = findChild[1].text()

            # Get main dictionary name from parent widget
            mainDictionary = self.parentWindow.nameOfTheDictionary.text()

            # Get connection to the database
            connection = create_connection_to_the_database(f'database/database.db')

            # Open a host to make connection to succeed
            with connection:

                # Get data from database
                getDataFromDatabase = select_data_in_the_database(
                    connection,
                    "dictionary",
                    LocalDatabase.userLoginData["email"]
                )

                # ---------------------------------------------------------------------------------------------------
                # The dictionary, that we got in the variable "getDataFromDatabase" gives us the string of the dict,
                # that's white we need to convert the string into an object "dict" using the library "json"
                # ---------------------------------------------------------------------------------------------------
                dictionary = json.loads(getDataFromDatabase[0][0].replace("'", ""))

                # Remove element "text" from dict
                dictionary[mainDictionary]["custom_dictionaries"].pop(text)

                # Update the data in the local database
                update_data_in_the_database(
                    connection,
                    "dictionary = ?",
                    (
                        json.dumps(dictionary),
                        LocalDatabase.userLoginData["email"]
                    )
                )

                # Call the function to refresh the list of the custom dictionaries
                self.set_timer_to_refresh_the_list_of_the_custom_dictionaries(event=None)
                return


class WordMethods(QMainWindow):
    def __init__(self, parent_window, main_parent_widget, stacked_widget, viewing_the_words):
        super(WordMethods, self).__init__()

        # Initialize widgets
        self.parentWindow = parent_window
        self.mainParentWidget = main_parent_widget
        self.stackedWidget = stacked_widget
        self.viewingTheWords = viewing_the_words

        self.obj = None
        self.clicks = 5

    def refresh_the_list_of_the_words(self):

        """

        This function refreshes the list of the words by taking the data from the local database

        :return:
        """

        # Get the name of the custom dictionary from local database
        nameOfTheCustomDictionary = CustomDictionaries.temporaryCustomDictionaryData["customDictionaryName"]

        # Get page object by the name of the custom dictionary that has been saved in local variable
        page = self.viewingTheWords[nameOfTheCustomDictionary]["page"]

        # Get the name of the general dictionary
        nameOfTheDictionary = self.parentWindow.nameOfTheDictionary.text()

        # Get connection to the database
        connection = create_connection_to_the_database(f"database/database.db")

        # Open a host to make connection to succeed
        with connection:

            # Get data from database
            getDataFromDatabase = select_data_in_the_database(
                connection,
                "dictionary",
                LocalDatabase.userLoginData["email"]
            )

            # Check if there is data in database
            if not getDataFromDatabase[0][0]:

                # If not, do nothing
                pass

            # If there is data in database...
            else:

                # ---------------------------------------------------------------------------------------------------
                # The dictionary, that we got in the variable "getDataFromDatabase" gives us the string of the dict,
                # that's why we need to convert the string into an object "dict" using the library "json"
                # ---------------------------------------------------------------------------------------------------
                dictionary = json.loads(getDataFromDatabase[0][0].replace("'", ""))

                geometry = {
                    "QMainFrame": [231, 371],
                    "QFrameOfTheWord": [5, 5, 221, 311],
                    "QPlayTheWord": [180, 15, 31, 31],
                    "QStatusOfTheWord": [180, 50, 31, 31],
                    "QColorOfTheWord": [180, 87, 31, 31],
                    "QIconOfTheWord": [20, 22, 51, 51],
                    "QNameOfTheWord": [80, 22, 91, 22],
                    "QTranslationOfTheWord": [77, 42, 111, 71],
                    "QSeparatedLine_1": [22, 130, 191, 1],
                    "QSeparatedLine_2": [22, 180, 191, 1],
                    "QSeparatedLine_3": [22, 310, 191, 1],
                    "QTagsOfTheWord": [20, 147, 201, 22],
                    "QExamplesOfUsingTheWord": [18, 192, 201, 91],
                    "QRemoveTheWordButton": [80, 325, 31, 31],
                    "QEditTheWordButton": [120, 325, 31, 31]
                }

                # Create scroll area for the words
                scrollArea = QScrollArea(page)
                scrollArea.setGeometry(0, 170, 531, 245)
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
                scrollLayout.setContentsMargins(20, 10, 20, 10)

                framesPerLine = 2
                line_layout = None

                # Create a frame for dictionaries to be on
                frame = QFrame()

                if dictionary[self.parentWindow.nameOfTheDictionary.text()]["custom_dictionaries"][nameOfTheCustomDictionary].get("words"):

                    getCustomDictionaryWords = dictionary[nameOfTheDictionary]["custom_dictionaries"][nameOfTheCustomDictionary]["words"]

                    for keys, values in getCustomDictionaryWords.items():

                        if list(getCustomDictionaryWords).index(keys) % framesPerLine == 0:
                            line_layout = QHBoxLayout()
                            line_layout.setContentsMargins(0, 0, 0, 0)

                            scrollLayout.addLayout(line_layout)

                            # Set spacing between content inside the scrollArea widget (in our case on the layout)
                            scrollLayout.setSpacing(20)

                        # Create main frame for the word and set the specific settings to it
                        mainFrame = QFrame(
                            parent=frame
                        )
                        mainFrame.setStyleSheet(
                            """
                            background-color: rgb(255, 255, 255);
                            border-radius: 30px;
                            border: none;
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

                        # Create an icon for the word and set the specific settings to it
                        iconOfTheWord = QLabel(
                            parent=mainFrame
                        )
                        iconOfTheWord.setStyleSheet(
                            """
                            background-color: none;
                            border: none;
                            border-radius: 0px;
                            """
                        )
                        iconOfTheWord.setObjectName(f"{keys}_iconOfTheWord")
                        iconOfTheWord.setGeometry(
                            geometry["QIconOfTheWord"][0],
                            geometry["QIconOfTheWord"][1],
                            geometry["QIconOfTheWord"][2],
                            geometry["QIconOfTheWord"][3]
                        )

                        if values["photo"]:
                            iconOfTheWord.setPixmap(QPixmap(values["photo"]))
                        else:
                            iconOfTheWord.setPixmap(QPixmap("icons/programIcon.png"))

                        iconOfTheWord.setScaledContents(True)

                        # Create a title label (name of the word) and set the specific settings to it
                        titleOfTheWord = QLineEdit(
                            parent=mainFrame
                        )
                        titleOfTheWord.setReadOnly(True)

                        font = QFont("Montserrat")
                        font.setBold(True)
                        font.setPointSize(13)
                        titleOfTheWord.setFont(font)

                        titleOfTheWord.setStyleSheet(
                            """
                            background-color: none;
                            border: none;
                            border-radius: 0px;
                            """
                        )
                        titleOfTheWord.setObjectName(f"{keys}_titleOfTheWord")
                        titleOfTheWord.setText(keys)
                        titleOfTheWord.setGeometry(
                            geometry["QNameOfTheWord"][0],
                            geometry["QNameOfTheWord"][1],
                            geometry["QNameOfTheWord"][2],
                            geometry["QNameOfTheWord"][3]
                        )

                        # Create a description label for the word and set the specific settings to it
                        translationOfTheWord = QPlainTextEdit(
                            parent=mainFrame
                        )
                        font = QFont("Montserrat")
                        font.setItalic(True)
                        font.setPointSize(9)
                        translationOfTheWord.setFont(font)

                        translationOfTheWord.setPlainText(values["translation"])
                        translationOfTheWord.setStyleSheet(
                            """
                            background-color: rgba(255, 255, 255, 0);
                            border: none;
                            border-radius: 0px;
                            """
                        )
                        translationOfTheWord.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
                        translationOfTheWord.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                        translationOfTheWord.setReadOnly(True)
                        translationOfTheWord.setObjectName(f"{keys}_translationOfTheWord")
                        translationOfTheWord.setGeometry(
                            geometry["QTranslationOfTheWord"][0],
                            geometry["QTranslationOfTheWord"][1],
                            geometry["QTranslationOfTheWord"][2],
                            geometry["QTranslationOfTheWord"][3]
                        )

                        # Create a play button for the word and set the specific settings to it
                        playTheWord = QPushButton(
                            parent=mainFrame
                        )
                        playTheWord.setIcon(QIcon("icons/volumeIcon_W.png"))
                        playTheWord.setIconSize(QSize(15, 15))
                        playTheWord.setStyleSheet(
                            """QPushButton {
                                border: none;
                                background-color: rgb(0, 70, 190);
                                border-radius: 15px;
                            }"""
                        )
                        playTheWord.setObjectName(f"{keys}_playTheWord")
                        playTheWord.setCursor(Qt.CursorShape.PointingHandCursor)
                        playTheWord.setGeometry(
                            geometry["QPlayTheWord"][0],
                            geometry["QPlayTheWord"][1],
                            geometry["QPlayTheWord"][2],
                            geometry["QPlayTheWord"][3]
                        )

                        # When the button clicked, call other function to proceed
                        playTheWord.clicked.connect(self.play_the_word)

                        # Create a color button for the word and set the specific settings to it
                        colorOfTheWord = QPushButton(
                            parent=mainFrame
                        )
                        colorOfTheWord.setStyleSheet(
                            """QPushButton {
                                border: none;
                                background-color: rgb(%s);
                                border-radius: 15px;
                            }""" % (values["color"])
                        )
                        colorOfTheWord.setObjectName(f"{keys}_colorOfTheWord")
                        colorOfTheWord.setGeometry(
                            geometry["QColorOfTheWord"][0],
                            geometry["QColorOfTheWord"][1],
                            geometry["QColorOfTheWord"][2],
                            geometry["QColorOfTheWord"][3]
                        )

                        # Create an icon to show the status of the word and set the specific settings to it
                        statusOfTheWord = QPushButton(
                            parent=mainFrame
                        )
                        statusOfTheWord.setIcon(QIcon(values['status']['icon']))
                        statusOfTheWord.setIconSize(QSize(15, 15))
                        statusOfTheWord.setStyleSheet(
                            f"""
                            border: none;
                            background-color: rgb({values["status"]["color"]});
                            border-radius: 15px;
                            """
                        )
                        statusOfTheWord.setObjectName(f"{keys}_statusOfTheWord")
                        statusOfTheWord.setGeometry(
                            geometry["QStatusOfTheWord"][0],
                            geometry["QStatusOfTheWord"][1],
                            geometry["QStatusOfTheWord"][2],
                            geometry["QStatusOfTheWord"][3]
                        )

                        # Create a separated line for the word and set the specific settings to it
                        separatedLine_1 = QLabel(
                            parent=mainFrame
                        )
                        separatedLine_1.setStyleSheet(
                            """QLabel {
                                background-color: rgb(240, 240, 240);
                                border: none;
                            }"""
                        )
                        separatedLine_1.setObjectName(f"{keys}_separatedLine_1")
                        separatedLine_1.setGeometry(
                            geometry["QSeparatedLine_1"][0],
                            geometry["QSeparatedLine_1"][1],
                            geometry["QSeparatedLine_1"][2],
                            geometry["QSeparatedLine_1"][3]
                        )

                        # Create a tags line edit for the word and set the specific settings to it
                        tags = QLineEdit(
                            parent=mainFrame
                        )
                        tags.setReadOnly(True)
                        tags.setFont(QFont("Montserrat", 9))

                        tags.setStyleSheet(
                            """
                            background-color: none;
                            border: none;
                            border-radius: 0px;
                            """
                        )
                        tags.setObjectName(f"{keys}_tags")

                        if values["tags"]:
                            tags.setText(values["tags"])
                        else:
                            pass

                        tags.setGeometry(
                            geometry["QTagsOfTheWord"][0],
                            geometry["QTagsOfTheWord"][1],
                            geometry["QTagsOfTheWord"][2],
                            geometry["QTagsOfTheWord"][3]
                        )

                        # Create a separated line for the word and set the specific settings to it
                        separatedLine_2 = QLabel(
                            parent=mainFrame
                        )
                        separatedLine_2.setStyleSheet(
                            """QLabel {
                                background-color: rgb(240, 240, 240);
                                border: none;
                            }"""
                        )
                        separatedLine_2.setObjectName(f"{keys}_separatedLine_2")
                        separatedLine_2.setGeometry(
                            geometry["QSeparatedLine_2"][0],
                            geometry["QSeparatedLine_2"][1],
                            geometry["QSeparatedLine_2"][2],
                            geometry["QSeparatedLine_2"][3]
                        )

                        # Create an examples text edit for the word and set the specific settings to it
                        examplesOfUsingTheWord = QPlainTextEdit(
                            parent=mainFrame
                        )
                        examplesOfUsingTheWord.setFont(QFont("Montserrat", 9))

                        if values["examples"]:
                            examplesOfUsingTheWord.setPlainText(values["examples"])
                        else:
                            pass

                        examplesOfUsingTheWord.setStyleSheet(
                            """
                            background-color: rgba(255, 255, 255, 0);
                            border: none;
                            border-radius: 0px;
                            """
                        )
                        examplesOfUsingTheWord.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
                        examplesOfUsingTheWord.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                        examplesOfUsingTheWord.setReadOnly(True)
                        examplesOfUsingTheWord.setObjectName(f"{keys}_examplesOfUsingTheWord")
                        examplesOfUsingTheWord.setGeometry(
                            geometry["QExamplesOfUsingTheWord"][0],
                            geometry["QExamplesOfUsingTheWord"][1],
                            geometry["QExamplesOfUsingTheWord"][2],
                            geometry["QExamplesOfUsingTheWord"][3]
                        )

                        # Create a separated line for the word and set the specific settings to it
                        separatedLine_3 = QLabel(
                            parent=mainFrame
                        )
                        separatedLine_3.setStyleSheet(
                            """QLabel {
                                background-color: rgb(240, 240, 240);
                                border: none;
                            }"""
                        )
                        separatedLine_3.setObjectName(f"{keys}_separatedLine_3")
                        separatedLine_3.setGeometry(
                            geometry["QSeparatedLine_3"][0],
                            geometry["QSeparatedLine_3"][1],
                            geometry["QSeparatedLine_3"][2],
                            geometry["QSeparatedLine_3"][3]
                        )

                        # Create a button to edit a word and set the specific settings to it
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
                        editButton.setObjectName(f"{keys}_editTheWordButton")
                        editButton.setCursor(Qt.CursorShape.PointingHandCursor)
                        editButton.setGeometry(
                            geometry["QEditTheWordButton"][0],
                            geometry["QEditTheWordButton"][1],
                            geometry["QEditTheWordButton"][2],
                            geometry["QEditTheWordButton"][3]
                        )

                        # When button clicked, call other function to proceed
                        editButton.clicked.connect(self.edit_a_word)

                        # Create a remove button for the word and set the specific settings to it
                        removeButton = QPushButton(
                            parent=mainFrame
                        )
                        removeButton.setIcon(QIcon("icons/trashIcon_W.png"))
                        removeButton.setIconSize(QSize(16, 16))
                        removeButton.setStyleSheet(
                            """QPushButton {
                                border: none;
                                background-color: rgb(255, 85, 70);
                                border-radius: 7px;
                            }

                            QPushButton:hover {
                                background-color: rgba(255, 85, 70, 220);
                            }

                            QPushButton:pressed {
                                background-color: rgba(255, 85, 70, 240);
                            }"""
                        )
                        removeButton.setObjectName(f"{keys}_removeTheWordButton")
                        removeButton.setCursor(Qt.CursorShape.PointingHandCursor)
                        removeButton.setGeometry(
                            geometry["QRemoveTheWordButton"][0],
                            geometry["QRemoveTheWordButton"][1],
                            geometry["QRemoveTheWordButton"][2],
                            geometry["QRemoveTheWordButton"][3]
                        )

                        # When button clicked, call other function to proceed
                        removeButton.clicked.connect(self.open_a_choice_window_and_set_a_signal)

                        # Add a mainFrame widget to the line_layout layout
                        line_layout.addWidget(mainFrame)

                        # Set the layout to the frame that holds the content
                        frame.setLayout(scrollLayout)

                        # Set the widget to the scrollArea widget
                        scrollArea.setWidget(frame)

                        # Show the scrollArea widget
                        scrollArea.show()
                else:
                    # Set the layout to the frame that holds the content
                    frame.setLayout(scrollLayout)

                    # Set the widget to the scrollArea widget
                    scrollArea.setWidget(frame)

                    # Show the scrollArea widget
                    scrollArea.show()

                # If the removing signal in the local database equals True
                if RemoveSomething.signal:

                    # Set the removing signal to False
                    RemoveSomething.signal = False

    def play_the_word(self):

        """

        This function converts text of the word to the speech

        :return:
        """

        # Get clicked object
        sender = self.sender()

        # Get parent widget from clicked object
        parentFrameOfTheButton = sender.parentWidget()

        # Find child from parent widget
        findChild = parentFrameOfTheButton.findChildren(QLineEdit)

        # Get text from child's object
        text = findChild[0].text()

        # Create a main engine to play the word
        engine = pyttsx3.init()

        # Set rate and volume to the engine, that's going to play the word
        engine.setProperty('rate', 165)
        engine.setProperty('volume', 0.7)

        # Get available voice in the engine
        voices = engine.getProperty('voices')

        # Set the first voice in the engine voices (0 - male, 1 - female, 2 - russian female)
        engine.setProperty('voice', voices[0].id)

        # Say the text
        engine.say(text)

        # During the process, the window automatically getting frozen
        engine.runAndWait()

        # Stop the engine when it's finished
        engine.stop()

    def edit_a_word(self):

        """

        This function edits a word in the database

        :return:
        """

        # Get clicked object
        sender = self.sender()

        # Get parent widget from clicked object
        parentFrameOfTheButton = sender.parentWidget()

        # Get children objects from parent widget
        findChildren = [
            parentFrameOfTheButton.findChildren(QLineEdit),
            parentFrameOfTheButton.findChildren(QPlainTextEdit)
        ]

        # Get texts from children's objects
        texts = [
            findChildren[0][0].text(),
            findChildren[1][0].toPlainText()
        ]

        # Get current page from stacked widget
        currentPage = self.stackedWidget.currentWidget()

        # Get QLabel child from page of the stacked widget
        childrenOfThePage = currentPage.findChildren(QLabel)

        # Get name of the custom dictionary
        nameOfTheCustomDictionary = childrenOfThePage[1].text()

        # Save the data into local database
        EditAWord.dataToFillUp.update(
            {
                "name": texts[0],
                "translation": texts[1]
            }
        )

        # Save the name of the custom dictionary into local database
        EditAWord.customDictionary = nameOfTheCustomDictionary

        # Set the signal in the local database to True
        EditAWord.signal = True

        # Save the main dictionary name into local variable of database
        EditAWord.mainDictionary = self.parentWindow.nameOfTheDictionary.text()

        # Make the setting to a child's window
        window = windows.AddAWordToACustomDictionary()
        window.setParent(self)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
        window.setWindowModality(QtCore.Qt.WindowModality.WindowModal)

        window.closeEvent = self.set_timer_to_refresh_the_list_of_the_words

        # Create a blacked out widget for MainWindow
        widget = QWidget(self)
        widget.setStyleSheet(
            """QWidget {
                background-color: rgba(0, 0, 0, 50);
                border: none;
            }"""
        )
        widget.setGeometry(0, 0, 1280, 720)
        widget.setParent(self.mainParentWidget)
        widget.show()

        # Save the object of the widget in local database
        BlackedOutWidget.widget = widget

        window.show()

    def open_a_choice_window_and_set_a_signal(self):

        """

        This function open a Choice window and sets the special signal to the local variable
        of database

        :return:
        """

        # Save the clicked object into local variable
        self.obj = self.sender()

        # Make the setting to a child's window
        window = windows.ChoiceWindow()
        window.setParent(self)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
        window.setWindowModality(QtCore.Qt.WindowModality.WindowModal)

        # Set the new text in the Choice window
        window.uiChoiceWindow.explanationLabel.setText("Are you sure you want to delete this word?")

        # When window closed, call other function to proceed
        window.closeEvent = self.remove_a_word

        # Create a blacked out widget for MainWindow
        widget = QWidget(self)
        widget.setStyleSheet(
            """QWidget {
                background-color: rgba(0, 0, 0, 50);
                border: none;
            }"""
        )
        widget.setGeometry(0, 0, 1280, 720)
        widget.setParent(self.mainParentWidget)
        widget.show()

        # Save the object of the widget in local database
        BlackedOutWidget.widget = widget

        window.show()

    def set_timer_to_refresh_the_list_of_the_words(self, event):

        """

        This function sets timer to refresh the list of the words on the screen

        :param event:
        :return:
        """

        # Set the timer, after which the other function is going to start
        timer = QTimer(self)

        # Make the timer works once
        timer.setSingleShot(True)

        # Set the action that should be done after finishing the timer
        timer.timeout.connect(self.refresh_the_list_of_the_words)

        timer.start(100)

    def remove_a_word(self, event):

        """

        This function removes the word from database

        :param event: event object that comes from closeEvent
        :return:
        """

        # Check if the removing signal equals True
        if RemoveSomething.signal:

            # Get parent widget from saved clicked object
            parentFrameOfTheButton = self.obj.parentWidget()

            # Get the child object of the parent widget
            findChild = parentFrameOfTheButton.findChildren(QLineEdit)

            # Get the text from child's object
            text = findChild[0].text()

            # Get main dictionary name from parent widget
            mainDictionary = self.parentWindow.nameOfTheDictionary.text()

            # Get connection to the database
            connection = create_connection_to_the_database(f'database/database.db')

            # Open a host to make connection to succeed
            with connection:

                # Get data from database
                getDataFromDatabase = select_data_in_the_database(
                    connection,
                    "dictionary",
                    LocalDatabase.userLoginData["email"]
                )

                # ---------------------------------------------------------------------------------------------------
                # The dictionary, that we got in the variable "getDataFromDatabase" gives us the string of the dict,
                # that's why we need to convert the string into an object "dict" using the library "json"
                # ---------------------------------------------------------------------------------------------------
                dictionary = json.loads(getDataFromDatabase[0][0].replace("'", ""))

                # Remove the element "text" from dict
                dictionary[mainDictionary]["custom_dictionaries"][CustomDictionaries.temporaryCustomDictionaryData["customDictionaryName"]]["words"].pop(text)

                # Update data in the database
                update_data_in_the_database(connection, "dictionary = ?", (json.dumps(dictionary), LocalDatabase.userLoginData["email"]))

                # Call the function to refresh the list of the words
                self.set_timer_to_refresh_the_list_of_the_words(event=None)

                return

    def add_a_custom_word_to_a_custom_dictionary(self):

        """

        This function adds a custom word to a custom dictionary

        :return:
        """

        # Create an instan to the another window and set the specific settings to it
        window = windows.AddAWordToACustomDictionary()
        window.setParent(self)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowType.Window)
        window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        # Create a blacked out widget for MainWindow
        widget = QWidget(self)
        widget.setStyleSheet(
            """QWidget {
                background-color: rgba(0, 0, 0, 50);
                border: none;
            }"""
        )
        widget.setGeometry(0, 0, 1280, 720)
        widget.setParent(self.mainParentWidget)
        widget.show()

        # Save the object of the widget in local database
        BlackedOutWidget.widget = widget

        window.show()

    def randomize_the_words(self):

        """

        This function randomizes the words and then updates the list of the words

        :return:
        """

        # Get clicked object
        sender = self.sender()

        # Check if the limit of clicks less or equals to the 0
        if self.clicks <= 0:

            # Turn off the clicked object
            sender.setEnabled(False)
            return

        # Check if the limit of clicks more than 0
        else:

            # Get connection to the database
            connection = create_connection_to_the_database(f'database/database.db')

            # Open a host to make connection to succeed
            with connection:

                # Get data from database
                getDataFromDatabase = select_data_in_the_database(
                    connection,
                    "dictionary",
                    LocalDatabase.userLoginData["email"]
                )

                # ---------------------------------------------------------------------------------------------------
                # The dictionary, that we got in the variable "getDataFromDatabase" gives us the string of the dict,
                # that's why we need to convert the string into an object "dict" using the library "json"
                # ---------------------------------------------------------------------------------------------------
                dictionary = json.loads(getDataFromDatabase[0][0].replace("'", ""))

                # Get the main dictionary name from parent widget
                mainDictionary = self.parentWindow.nameOfTheDictionary.text()

                # Get the items from dict (items - (keys, values))
                items = list(dictionary[mainDictionary]["custom_dictionaries"][CustomDictionaries.temporaryCustomDictionaryData["customDictionaryName"]]["words"].items())

                # Use random method to shuffle the items in the variable
                random.shuffle(items)

                # Transform the shuffled items into dict
                shuffled = dict(items)

                # Set the new dict of the words into the dict with other items
                dictionary[mainDictionary]["custom_dictionaries"][CustomDictionaries.temporaryCustomDictionaryData["customDictionaryName"]]["words"] = shuffled

                # Update data in the database
                update_data_in_the_database(
                    connection,
                    "dictionary = ?",
                    (
                        json.dumps(dictionary),
                        LocalDatabase.userLoginData["email"]
                    )
                )

            # Call the function to refresh the list of the words
            self.set_timer_to_refresh_the_list_of_the_words(event=None)

            # Minus 1 from self.clicks variable
            self.clicks -= 1
