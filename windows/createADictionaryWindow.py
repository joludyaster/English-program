import gc
import json

from PySide6.QtCore import (Qt)
from PySide6.QtWidgets import (QMainWindow)

from uiPythonFiles.ui_CreateADictionaryForm import Ui_CreateADictionaryWindow
from database.database import (update_data_in_the_database, select_data_in_the_database, create_connection_to_the_database)
from localDatabase.local_database import (LocalDatabase, BlackedOutWidget, EditADictionary)


class CreatingAVocabularyWindow(QMainWindow):
    def __init__(self):
        super(CreatingAVocabularyWindow, self).__init__()

        # Initialize variables
        self.window = None
        self.color = ""
        self.priority = None
        self.oldNameOfDictionary = None

        self.uiCreateADictionaryWindow = Ui_CreateADictionaryWindow()
        self.uiCreateADictionaryWindow.setupUi(self)

        self.init_UI()
        self.mouse_events()

    def init_UI(self):

        """

        1. This function set the specific settings to the window
        2. Checks if the status of the signal equals True, then sets the specific data to the opened window

        :return:
        """

        # Check if the status equals True
        if EditADictionary.signal:

            # Get data from variables from local database
            name = EditADictionary.dataToFillUp["name"]
            description = EditADictionary.dataToFillUp["description"]
            color = EditADictionary.dataToFillUp["color"]
            priorityData = EditADictionary.dataToFillUp["priority"]

            # Save color, oldDictionaryName and priorityData in local variables
            self.color = color
            self.oldNameOfDictionary = name
            self.priority = priorityData

            # Set text to the line edits
            self.uiCreateADictionaryWindow.blankForTheName.setText(name)
            self.uiCreateADictionaryWindow.blankForTheDescription.setText(description)

            # Set styleSheet to the specific widget
            self.uiCreateADictionaryWindow.chosenColor.setStyleSheet(
                f"""
                background-color: rgb({color});
                border: none;
                border-radius: 5px;
                """
            )

            # Set styleSheet to the specific widget
            self.uiCreateADictionaryWindow.chosenPriority.setStyleSheet(priorityData["styleSheet"])

            # Set text to the specific widget
            self.uiCreateADictionaryWindow.chosenPriority.setText(priorityData["number"])

        # Remove the window hint
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Make the window translucent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def mouse_events(self):

        """

        This function makes mouse events and responses to them

        :return:
        """

        # Make mouse events and responses to them
        self.uiCreateADictionaryWindow.saveAndCreateADictionaryButton.clicked.connect(self.create_or_update_a_dictionary)
        self.uiCreateADictionaryWindow.cancelButton.clicked.connect(self.create_or_update_a_dictionary)

        for color in [
            self.uiCreateADictionaryWindow.color_1, self.uiCreateADictionaryWindow.color_2,
            self.uiCreateADictionaryWindow.color_3, self.uiCreateADictionaryWindow.color_4,
            self.uiCreateADictionaryWindow.color_5, self.uiCreateADictionaryWindow.color_6,
            self.uiCreateADictionaryWindow.color_7, self.uiCreateADictionaryWindow.color_8,
            self.uiCreateADictionaryWindow.color_9, self.uiCreateADictionaryWindow.color_10,
            self.uiCreateADictionaryWindow.color_11, self.uiCreateADictionaryWindow.color_12,
            self.uiCreateADictionaryWindow.color_13, self.uiCreateADictionaryWindow.color_14,
            self.uiCreateADictionaryWindow.color_15, self.uiCreateADictionaryWindow.color_16,
            self.uiCreateADictionaryWindow.color_17, self.uiCreateADictionaryWindow.color_18,
            self.uiCreateADictionaryWindow.color_19
        ]:
            color.clicked.connect(self.choose_a_color_for_a_dictionary)

        for priority in [
            self.uiCreateADictionaryWindow.firstPriority, self.uiCreateADictionaryWindow.secondPriority,
            self.uiCreateADictionaryWindow.thirdPriority, self.uiCreateADictionaryWindow.fourthPriority,
            self.uiCreateADictionaryWindow.fifthPriority
        ]:
            priority.clicked.connect(self.choose_the_priority_for_the_dictionary)

    def create_or_update_a_dictionary(self):

        """

        1. This function creates a dictionary
        2. This function updates the already existing dictionary with the new data, if the signal equals True

        :return:
        """

        # Get the clicked object
        sender = self.sender()

        # Get the name of the main dictionary
        nameOfTheDictionary = self.uiCreateADictionaryWindow.blankForTheName.text()

        # Get the description of the main dictionary
        descriptionOfTheDictionary = self.uiCreateADictionaryWindow.blankForTheDescription.text()

        # Check if the clicked object equals to the specific widget's object
        if sender == self.uiCreateADictionaryWindow.saveAndCreateADictionaryButton:

            # Check if the entered data is not empty
            if not nameOfTheDictionary and descriptionOfTheDictionary and self.color and self.priority or \
                    not nameOfTheDictionary or not descriptionOfTheDictionary or not self.color or not self.priority:

                # Do nothing if the entered data is empty
                pass

            # If entered data is not empty
            else:

                # Check if the signal to edit the dictionary equals True
                if EditADictionary.signal:

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

                        # Check if the current entered new name of the dictionary equals the old one
                        if self.uiCreateADictionaryWindow.blankForTheName.text() == self.oldNameOfDictionary:

                            # Set the name of the dictionary to the variable "name"
                            name = self.oldNameOfDictionary

                        # If the current entered new name of the dictionary is not equal the old one
                        else:

                            # Set the name of the dictionary to the variable "name"
                            name = self.uiCreateADictionaryWindow.blankForTheName.text()

                        # Replace the new name of the dictionary in the dict
                        dictionary[name] = dictionary[self.oldNameOfDictionary]

                        # Remove the old name of the dictionary from dict
                        del dictionary[self.oldNameOfDictionary]

                        # Create a temporary variable to store the data
                        priority = {
                            "color": self.priority["color"],
                            "number": self.priority["number"],
                            "styleSheet": self.priority["styleSheet"]
                        }

                        # Update the data in the dict
                        dictionary.update(
                            {
                                name: {
                                    "color": self.color,
                                    "description": descriptionOfTheDictionary,
                                    "priority": priority
                                }
                            }
                        )

                        # Update the data in the database
                        update_data_in_the_database(
                            connection,
                            "dictionary = ?",
                            (
                                json.dumps(dictionary),
                                LocalDatabase.userLoginData["email"]
                            )
                        )

                    # Remove the blacked out widget from parent window and set the styleSheet to None
                    BlackedOutWidget.widget.setParent(None)
                    BlackedOutWidget.widget.setStyleSheet(None)

                    # Set the signal to False
                    EditADictionary.signal = False

                    # Close the window
                    self.close()

                    for name in locals():
                        del name

                    gc.collect()

                    return

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

                        # If the getDataFromDatabase variable is empty
                        if not getDataFromDatabase[0][0]:

                            # Create a temporary variable to store the data
                            priority = {
                                "color": self.priority["color"],
                                "number": self.priority["number"],
                                "styleSheet": self.priority["styleSheet"]
                            }

                            # Update the data in the dict
                            dictionary = {
                                nameOfTheDictionary: {
                                    "color": self.color,
                                    "description": descriptionOfTheDictionary,
                                    "priority": priority
                                }
                            }

                        # If the getDataFromDatabase is not empty
                        else:

                            # ---------------------------------------------------------------------------------------------------
                            # The dictionary, that we got in the variable "getDataFromDatabase" gives us the string of the dict,
                            # that's why we need to convert the string into an object "dict" using the library "json"
                            # ---------------------------------------------------------------------------------------------------
                            dictionary = json.loads(getDataFromDatabase[0][0].replace("'", ""))

                            # Create a temporary variable to store the data
                            priority = {
                                "color": self.priority["color"],
                                "number": self.priority["number"],
                                "styleSheet": self.priority["styleSheet"]
                            }

                            # Update the data in the dict
                            dictionary.update(
                                {
                                    nameOfTheDictionary: {
                                        "color": self.color,
                                        "description": descriptionOfTheDictionary,
                                        "priority": priority
                                    }
                                }
                            )

                        # Update the data in the database
                        update_data_in_the_database(
                            connection,
                            "dictionary = ?",
                            (
                                json.dumps(dictionary),
                                LocalDatabase.userLoginData["email"]
                            )
                        )

                        # Remove the blacked out widget from parent window and set the styleSheet to None
                        BlackedOutWidget.widget.setParent(None)
                        BlackedOutWidget.widget.setStyleSheet(None)

                        # Close the window
                        self.close()

                        for name in locals():
                            del name

                        gc.collect()

                        return

        # If the clicked object is not equal to the specific widget's object
        else:

            # Remove the blacked out widget from parent window and set the styleSheet to None
            BlackedOutWidget.widget.setParent(None)
            BlackedOutWidget.widget.setStyleSheet(None)

            # Set the signal to False
            EditADictionary.signal = False

            # Close the window
            self.close()

            for name in locals():
                del name

            gc.collect()

            return

    def choose_a_color_for_a_dictionary(self):

        """

        This function save the chosen color of the dictionary by the user

        :return:
        """

        # Get the button that has been clicked
        button = self.sender()

        # Get the color of the clicked button
        color = button.palette().window().color()

        # Save a color to the local variable
        self.color = f"{color.red()}, {color.green()}, {color.blue()}"

        # Set styleSheet to the specific widget
        self.uiCreateADictionaryWindow.chosenColor.setStyleSheet(
            f"""
            background-color: rgb({color.red()}, {color.green()}, {color.blue()});
            border-radius: 5px;
            border: none;
            """
        )

        for name in locals():
            del name

        gc.collect()

    # def choose_a_custom_color_for_a_word(self):
    #     color_picker = QColorDialog.getColor()
    #
    #     self.uiCreateADictionaryWindow.chosenColor.setStyleSheet(
    #         f"""
    #         background-color: rgb({color_picker.red()}, {color_picker.green()}, {color_picker.blue()});
    #         border-radius: 5px;
    #         border: none;"""
    #     )
    #
    #     self.color = f"{color_picker.red()}, {color_picker.green()}, {color_picker.blue()}"

    def choose_the_priority_for_the_dictionary(self):

        """

        This function save the priority of the dictionary by the user

        :return:
        """

        # Get the clicked object
        sender = self.sender()

        # Get the color of the clicked object
        color = sender.palette().window().color()

        # Save the priority data in the local variable
        self.priority = {
            "color": f"{color.red()}, {color.green()}, {color.blue()}",
            "number": sender.text(),
            "styleSheet": sender.styleSheet(),
        }

        # Set the styleSheet to the specific widget
        self.uiCreateADictionaryWindow.chosenPriority.setStyleSheet(
            sender.styleSheet()
        )

        # Set the text to the specific widget
        self.uiCreateADictionaryWindow.chosenPriority.setText(
            sender.text()
        )

        for name in locals():
            del name

        gc.collect()
