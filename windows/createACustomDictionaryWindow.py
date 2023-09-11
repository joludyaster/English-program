import json

from PySide6.QtCore import (Qt)
from PySide6.QtWidgets import (QMainWindow)

from uiPythonFiles.ui_CreateACustomDictionaryForm import Ui_CreateACustomDictionaryWindow
from database.database import update_data_in_the_database, select_data_in_the_database, create_connection_to_the_database
from localDatabase.local_database import LocalDatabase, BlackedOutWidget, EditACustomDictionary


class CustomDictionaryArea(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialization widgets
        self.window = None

        # Initialization features
        self.status = None
        self.animation = None
        self.blur = None
        self.clickPosition = None
        self.oldNameOfDictionary = None

        self.uiCustomDictionaryAreaWindow = Ui_CreateACustomDictionaryWindow()
        self.uiCustomDictionaryAreaWindow.setupUi(self)

        self.init_UI()
        self.mouse_events()

    def init_UI(self):

        """

        This function sets the specific settings to the window and also checks the signal in the local database
        to edit a custom dictionary

        :return:
        """

        # Check if the signal to edit a custom dictionary equals True
        if EditACustomDictionary.signal:

            # Get the data from dict in the local variable in the local database
            name = EditACustomDictionary.dataToFillUp["name"]
            description = EditACustomDictionary.dataToFillUp["description"]

            # Save the old name of the custom dictionary
            self.oldNameOfDictionary = name

            # Set text to the specific widgets
            self.uiCustomDictionaryAreaWindow.blankForTheNameOfDictionary.setText(name)
            self.uiCustomDictionaryAreaWindow.blankForTheDescription.setPlainText(description)

        # Hide the window hint
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Make window translucent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def mouse_events(self):

        """

        This function makes mouse events and responses to them

        :return:
        """

        # Make mouse events and responses to them
        self.uiCustomDictionaryAreaWindow.cancelButton.clicked.connect(self.close_the_window_or_process_a_custom_dictionary)
        self.uiCustomDictionaryAreaWindow.saveAndCreateADictionaryButton.clicked.connect(self.close_the_window_or_process_a_custom_dictionary)

    def close_the_window_or_process_a_custom_dictionary(self):

        """

        This function creates a custom dictionary or edit the existing one

        :return:
        """

        # Get clicked object
        sender = self.sender()

        # Get texts from specific widgets
        nameOfTheCustomDictionary = self.uiCustomDictionaryAreaWindow.blankForTheNameOfDictionary.text()
        descriptionOfTheCustomDictionary = self.uiCustomDictionaryAreaWindow.blankForTheDescription.toPlainText()

        # Check if the clicked object equals the specific button in the window
        if sender == self.uiCustomDictionaryAreaWindow.cancelButton:

            # Remove the blacked out widget from parent window and set the styleSheet to None
            BlackedOutWidget.widget.setParent(None)
            BlackedOutWidget.widget.setStyleSheet(None)

            # Check if the signal to edit a custom dictionary equals True
            if EditACustomDictionary.signal:

                # Set the signal to False
                EditACustomDictionary.signal = False

            # Close the window
            self.close()

        # If the clicked object is not equal to the specific button in the window
        else:

            # Check if the signal to edit a custom dictionary equals True
            if EditACustomDictionary.signal:

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

                    # Get the main dictionary name from local database
                    mainDictionary = EditACustomDictionary.mainDictionary

                    # Get the "words" dict from main dict
                    words = dictionary[mainDictionary]["custom_dictionaries"][self.oldNameOfDictionary]["words"]

                    # Check if entered by user new name of the custom dictionary equals the old one
                    if self.uiCustomDictionaryAreaWindow.blankForTheNameOfDictionary.text() == self.oldNameOfDictionary:

                        # Save the new name of the custom dictionary to the variable "name"
                        name = self.oldNameOfDictionary

                    # If entered by user new name of the custom dictionary is not equal to the old one
                    else:

                        # Save the new name of the custom dictionary to the variable "name"
                        name = self.uiCustomDictionaryAreaWindow.blankForTheNameOfDictionary.text()

                    # Replace the old name of the custom dictionary by the new one
                    dictionary[mainDictionary]["custom_dictionaries"][name] = dictionary[mainDictionary]["custom_dictionaries"][self.oldNameOfDictionary]

                    # Remove the old name of the custom dictionary in the dict
                    del dictionary[mainDictionary]["custom_dictionaries"][self.oldNameOfDictionary]

                    # Update the data in the dict
                    dictionary[mainDictionary]["custom_dictionaries"].update(
                        {
                            name: {
                                "description": descriptionOfTheCustomDictionary,
                                "words": words
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

                # Set the signal to edit a custom dictionary to False
                EditACustomDictionary.signal = False

                # Close the window
                self.close()

            # If the signal to edit a custom dictionary equals False
            else:

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

                    # ---------------------------------------------------------------------------------------------------
                    # The dictionary, that we got in the variable "getDataFromDatabase" gives us the string of the dict,
                    # that's why we need to convert the string into an object "dict" using the library "json"
                    # ---------------------------------------------------------------------------------------------------
                    dictionary = json.loads(getDataFromDatabase[0][0].replace("'", ""))

                    # Check if the name of the custom dictionary has been entered by user
                    if nameOfTheCustomDictionary:

                        # Check if there are custom dictionaries in the dict
                        if dictionary[LocalDatabase.temporaryDictionaryData["name"]].get("custom_dictionaries"):

                            # Update the data in the dict
                            dictionary[LocalDatabase.temporaryDictionaryData["name"]]["custom_dictionaries"].update(
                                {
                                    nameOfTheCustomDictionary: {
                                        "description": descriptionOfTheCustomDictionary,
                                        "words": {}
                                    }
                                }
                            )

                        # Check if there are custom dictionaries in the dict
                        else:

                            # Update the data in the dict
                            dictionary[LocalDatabase.temporaryDictionaryData["name"]].update(
                                {
                                    "custom_dictionaries": {
                                        nameOfTheCustomDictionary: {
                                            "description": descriptionOfTheCustomDictionary,
                                            "words": {}
                                        }
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

                    # If the name of the custom dictionary has not been entered by user
                    else:

                        # Do nothing
                        pass



