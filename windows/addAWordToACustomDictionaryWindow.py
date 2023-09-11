from sqlite3 import Error

from PySide6.QtCore import (Qt, QDir, QTimer)
from PySide6.QtWidgets import (QMainWindow, QFileDialog, QColorDialog)
from PySide6.QtGui import (QPixmap)

from uiPythonFiles.ui_addAWordToACustomDictionary import Ui_WordInDictionaryMainWindow
from database.database import (update_data_in_the_database, select_data_in_the_database, create_connection_to_the_database)
from localDatabase.local_database import (LocalDatabase, BlackedOutWidget, CustomDictionaries, EditAWord)
from deep_translator import (GoogleTranslator)

import json
import os


class AddAWordToACustomDictionary(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialization widgets
        self.window = None

        # Initialization features
        self.status = None
        self.animation = None
        self.photo = None
        self.blur = None
        self.click_position = None
        self.color = None
        self.timer = None
        self.oldNameOfTheWord = None

        self.uiAddAWordToACustomDictionary = Ui_WordInDictionaryMainWindow()
        self.uiAddAWordToACustomDictionary.setupUi(self)

        self.init_UI()
        self.mouse_events()

    def init_UI(self):

        """

        This function sets the specific settings to the window and also checks the signal to edit a word, to edit a
        word eventually

        :return:
        """

        # Check if the signal to edit a word equals True
        if EditAWord.signal:

            # Create an exception block, to catch any potential errors from sql database
            try:

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

                    # Get the dict with the words from main dict "dictionary"
                    getWordsFromCustomDictionary = dictionary[EditAWord.mainDictionary]["custom_dictionaries"][EditAWord.customDictionary]["words"]

            # Catch an error
            except Error as e:

                # Print an error and close the window
                print(e)
                self.close()
                return

            # Get the specific data from local database
            titleOfTheWord = EditAWord.dataToFillUp["name"]
            translationOfTheWord = EditAWord.dataToFillUp["translation"]

            additionalTranslationOfTheWord = getWordsFromCustomDictionary[titleOfTheWord]["additionalTranslation"]
            tagsOfTheWord = getWordsFromCustomDictionary[titleOfTheWord]["tags"]

            examplesOfUsingTheWord = getWordsFromCustomDictionary[titleOfTheWord]["examples"]
            translationOfExamples = getWordsFromCustomDictionary[titleOfTheWord]["translationOfTheExamples"]

            photoOfTheWord = getWordsFromCustomDictionary[titleOfTheWord]["photo"]
            colorOfTheWord = getWordsFromCustomDictionary[titleOfTheWord]["color"]

            # Create a dict with temporary data to use it later
            statusOfTheWord = {
                "icon": getWordsFromCustomDictionary[titleOfTheWord]["status"]["icon"],
                "color": getWordsFromCustomDictionary[titleOfTheWord]["status"]["color"],
            }

            # Save an old name of the word
            self.oldNameOfTheWord = titleOfTheWord

            # Set text to the specific widgets
            self.uiAddAWordToACustomDictionary.wordLineEdit.setText(titleOfTheWord)
            self.uiAddAWordToACustomDictionary.translationLineEdit.setText(translationOfTheWord)

            # Check the conditions and set the specific data to the widgets
            if additionalTranslationOfTheWord:
                self.uiAddAWordToACustomDictionary.additionalTranslationLineEdit.setText(additionalTranslationOfTheWord)
            else:
                self.uiAddAWordToACustomDictionary.additionalTranslationLineEdit.setText("")

            if tagsOfTheWord:
                self.uiAddAWordToACustomDictionary.tagsLineEdit.setText(tagsOfTheWord)
            else:
                self.uiAddAWordToACustomDictionary.tagsLineEdit.setText("")

            if examplesOfUsingTheWord:
                self.uiAddAWordToACustomDictionary.examplesLineEdit.setText(examplesOfUsingTheWord)
            else:
                self.uiAddAWordToACustomDictionary.examplesLineEdit.setText("")

            if translationOfExamples:
                self.uiAddAWordToACustomDictionary.translationOfTheExamplesLineEdit.setText(translationOfExamples)
            else:
                self.uiAddAWordToACustomDictionary.translationOfTheExamplesLineEdit.setText("")

            if photoOfTheWord:
                if os.path.exists(photoOfTheWord):
                    self.uiAddAWordToACustomDictionary.photoOfTheWord.setPixmap(QPixmap(photoOfTheWord))
                    self.photo = photoOfTheWord
                else:
                    self.uiAddAWordToACustomDictionary.photoOfTheWord.setPixmap(QPixmap("icons/programIcon.png"))
            else:
                self.uiAddAWordToACustomDictionary.photoOfTheWord.setPixmap(QPixmap("icons/programIcon.png"))

            # Set the styleSheet to the specific widget
            self.uiAddAWordToACustomDictionary.chosenColor.setStyleSheet(
                f"""
                background-color: rgb({colorOfTheWord});
                border: none;
                border-radius: 5px;
                """
            )

            # Save the color of the word to the local variable
            self.color = colorOfTheWord

            # Create a loop to go into every button of statuses of the word
            for status in [
                self.uiAddAWordToACustomDictionary.processStatusButton,
                self.uiAddAWordToACustomDictionary.importantStatusButton,
                self.uiAddAWordToACustomDictionary.learnedStatusButton
            ]:

                # Get the color from the status word
                color = status.palette().window().color()

                # Check if the color we got equals the color of the saved color
                if f"{color.red()}, {color.green()}, {color.blue()}" == statusOfTheWord["color"]:

                    # Set the new object name to set the new styleSheet
                    status.setObjectName(status.objectName())

                    # Save the status data in the local variable
                    self.status = {
                        status: {
                            "color": f"{color.red()}, {color.green()}, {color.blue()}",
                            "icon": statusOfTheWord["icon"],
                            "styleSheet": status.styleSheet()
                        }
                    }

                    # Set the styleSheet to the status button
                    status.setStyleSheet(
                        f"""
                        background-color: rgba({color.red()}, {color.green()}, {color.blue()}, 120);
                        border: none;
                        border-radius: 7px;
                        padding: 1px;
                        color: rgb(255, 255, 255);
                        """
                    )

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
        # self.uiAddAWordToACustomDictionary.buttonToSwapWords.clicked.connect(self.swap_word_and_translation)
        self.uiAddAWordToACustomDictionary.cancelButton.clicked.connect(self.close_the_window)

        self.uiAddAWordToACustomDictionary.changePhotoOfTheWord.clicked.connect(self.choose_a_photo_for_a_word)

        for button in [
            self.uiAddAWordToACustomDictionary.color_1, self.uiAddAWordToACustomDictionary.color_2,
            self.uiAddAWordToACustomDictionary.color_3, self.uiAddAWordToACustomDictionary.color_4,
            self.uiAddAWordToACustomDictionary.color_5, self.uiAddAWordToACustomDictionary.color_6,
            self.uiAddAWordToACustomDictionary.color_7, self.uiAddAWordToACustomDictionary.color_8,
            self.uiAddAWordToACustomDictionary.color_9, self.uiAddAWordToACustomDictionary.color_10,
            self.uiAddAWordToACustomDictionary.color_11, self.uiAddAWordToACustomDictionary.color_12,
            self.uiAddAWordToACustomDictionary.color_13, self.uiAddAWordToACustomDictionary.color_14,
            self.uiAddAWordToACustomDictionary.color_15, self.uiAddAWordToACustomDictionary.color_16,
            self.uiAddAWordToACustomDictionary.color_17, self.uiAddAWordToACustomDictionary.color_18,
            self.uiAddAWordToACustomDictionary.color_19
        ]:
            button.clicked.connect(self.choose_a_color_for_a_word)

        self.uiAddAWordToACustomDictionary.changeColorButton.clicked.connect(self.choose_a_custom_color_for_a_word)
        self.uiAddAWordToACustomDictionary.wordLineEdit.textChanged[str].connect(self.start_translation)
        self.uiAddAWordToACustomDictionary.translationLineEdit.textChanged[str].connect(self.start_translation)
        self.uiAddAWordToACustomDictionary.saveAndAddAWord.clicked.connect(self.process_a_word)

        for button in [
            self.uiAddAWordToACustomDictionary.processStatusButton,
            self.uiAddAWordToACustomDictionary.learnedStatusButton,
            self.uiAddAWordToACustomDictionary.importantStatusButton
        ]:
            button.clicked.connect(self.choose_a_status_for_a_word)

    # def swap_word_and_translation(self):
    #     word_text = self.uiAddAWordToACustomDictionary.wordLineEdit.text()
    #     translation_text = self.uiAddAWordToACustomDictionary.translationLineEdit.text()
    #
    #     self.uiAddAWordToACustomDictionary.wordLineEdit.setText(translation_text)
    #     self.uiAddAWordToACustomDictionary.translationLineEdit.setText(word_text)

    def choose_a_photo_for_a_word(self):

        """

        This function saves and sets the photo that user selected

        :return:
        """

        # Create a file dialog to open the special window to select the photo
        filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')

        # If the selected photo equals ""
        if not filename:

            # Save the program icon to the temporary variable and local variable
            pixmap = QPixmap("icons/programIcon.png")
            self.photo = "icons/programIcon.png"

        # If the selected photo is not equal to the ""
        else:

            # Save the selected icon to the temporary variable and local variable
            pixmap = QPixmap(filename)
            self.photo = filename

        # Set the icon to the specific widget
        self.uiAddAWordToACustomDictionary.photoOfTheWord.setPixmap(pixmap)

    def choose_a_color_for_a_word(self):

        """

        This function saves the color and sets the new color to the specific widget

        :return:
        """

        # Get the button that has been clicked
        button = self.sender()

        # Get the color of the clicked button
        color = button.palette().window().color()

        # Save a color to the local variable
        self.color = f"{color.red()}, {color.green()}, {color.blue()}"

        # Set the styleSheet to the specific widget
        self.uiAddAWordToACustomDictionary.chosenColor.setStyleSheet(
            f"""
            background-color: rgb({color.red()}, {color.green()}, {color.blue()});
            border-radius: 5px;
            border: none;
            """
        )

    def choose_a_custom_color_for_a_word(self):

        """

        This function saves the custom color of the word and sets the new color to the specific widget

        :return:
        """

        # Open the custom color picker
        color_picker = QColorDialog.getColor()

        # Set the styleSheet to the specific widget
        self.uiAddAWordToACustomDictionary.chosenColor.setStyleSheet(
            f"""
            background-color: rgb({color_picker.red()}, {color_picker.green()}, {color_picker.blue()});
            border-radius: 5px;
            border: none;"""
        )

        # Save the new color of the word in the local varialbe
        self.color = f"{color_picker.red()}, {color_picker.green()}, {color_picker.blue()}"

    def choose_a_status_for_a_word(self):

        """

        This function saves the status data of the word and sets the specific settings to the widget

        :return:
        """

        # Check if the data of the previous status button exists
        if self.status:

            # Create a loop the goes in the items of the status button
            for key, value in self.status.items():

                # Set the styleSheet to the previous status button
                key.setStyleSheet(value["styleSheet"])

        # Get the clicked object
        sender = self.sender()

        # Get the color of the clicked object
        color = sender.palette().window().color()

        # Create a storage of the icons to use it later
        storage_of_icons = {
            "processStatusButton": "icons/processIcon_W.png",
            "importantStatusButton": "icons/importantIcon_W.png",
            "learnedStatusButton": "icons/learnedIcon_W.png"
        }

        # Save the data about status button in the local variable
        self.status = {
            sender: {
                "color": f"{color.red()}, {color.green()}, {color.blue()}",
                "icon": storage_of_icons[sender.objectName()],
                "styleSheet": sender.styleSheet()
            }
        }

        # Set the new styleSheet to the clicked object
        sender.setStyleSheet(
            f"""
            background-color: rgba({color.red()}, {color.green()}, {color.blue()}, 120);
            border: none;
            border-radius: 7px;
            padding: 1px;
            color: rgb(255, 255, 255);
            """
        )

    def start_translation(self):

        """

        This function sets the timer to start the translation of the word

        :return:
        """

        # Initialize timer object
        self.timer = QTimer()

        # Make it to succeed once
        self.timer.setSingleShot(True)

        # When the time is over, call other function to proceed
        self.timer.timeout.connect(self.translate_the_word)

        # Set the timer to 0.5 seconds
        self.timer.start(500)

    def translate_the_word(self):

        """

        This function translates the word from english to the language the user wants

        :return:
        """

        # Get the text from the line edit
        text = self.uiAddAWordToACustomDictionary.wordLineEdit.text()

        # Check if all the symbols in the string are actually chars
        check = any(char.isdigit() for char in text)

        # If all the characters in the string are actually chars
        if not check:

            # Create a translated Google object
            translated = GoogleTranslator(source="en", target="russian").translate(text=text)

            # Set the translated word to the specific widget
            self.uiAddAWordToACustomDictionary.translationLineEdit.setText(translated)

        # If all the characters in the string are not actually chars
        else:

            # Sets the empty string to the specific widget
            self.uiAddAWordToACustomDictionary.wordLineEdit.setText("")
            return

    def close_the_window(self):

        """

        This function closes the window and sets the signal to edit a word to False

        :return:
        """

        # Remove the blacked out widget from parent window and set the styleSheet to None
        BlackedOutWidget.widget.setParent(None)
        BlackedOutWidget.widget.setStyleSheet(None)

        # Check if the signal to edit a word equals True
        if EditAWord.signal:

            # Set the signal to False
            EditAWord.signal = False

        # Close the window
        self.close()

    def process_a_word(self):

        """

        This function checks the all entered data and creates the word if they meet the standards

        :return:
        """

        # Check if the required information in the line edits has been filled out
        if self.uiAddAWordToACustomDictionary.wordLineEdit.text() and self.uiAddAWordToACustomDictionary.translationLineEdit.text() and \
                self.color and self.status:

            # Check if the signal to edit a word equals True
            if EditAWord.signal:

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

                    # Check if the new name of the word equals the old one
                    if self.uiAddAWordToACustomDictionary.wordLineEdit.text() == self.oldNameOfTheWord:

                        # Set the new name of the word to the temporary variable "name"
                        name = self.oldNameOfTheWord

                    # Check if the new name of the word is not equal to the old one
                    else:

                        # Set the new name of the word to the temporary variable "name"
                        name = self.uiAddAWordToACustomDictionary.wordLineEdit.text()

                    # Replace the old name of the word by the new one
                    dictionary[CustomDictionaries.temporaryCustomDictionaryData["mainDictionaryName"]][
                        "custom_dictionaries"][CustomDictionaries.temporaryCustomDictionaryData["customDictionaryName"]]["words"][name] = dictionary[CustomDictionaries.temporaryCustomDictionaryData["mainDictionaryName"]][
                        "custom_dictionaries"][CustomDictionaries.temporaryCustomDictionaryData["customDictionaryName"]]["words"][self.oldNameOfTheWord]

                    # Remove the old name of the word from dict
                    del dictionary[CustomDictionaries.temporaryCustomDictionaryData["mainDictionaryName"]][
                        "custom_dictionaries"][CustomDictionaries.temporaryCustomDictionaryData["customDictionaryName"]]["words"][self.oldNameOfTheWord]

                    # Update the data in the dict
                    dictionary[CustomDictionaries.temporaryCustomDictionaryData["mainDictionaryName"]][
                        "custom_dictionaries"][CustomDictionaries.temporaryCustomDictionaryData["customDictionaryName"]]["words"].update(
                        {
                            self.uiAddAWordToACustomDictionary.wordLineEdit.text():
                                {
                                    "translation": self.uiAddAWordToACustomDictionary.translationLineEdit.text(),
                                    "additionalTranslation": self.uiAddAWordToACustomDictionary.additionalTranslationLineEdit.text(),
                                    "tags": self.uiAddAWordToACustomDictionary.tagsLineEdit.text(),
                                    "examples": self.uiAddAWordToACustomDictionary.examplesLineEdit.text(),
                                    "translationOfTheExamples": self.uiAddAWordToACustomDictionary.translationOfTheExamplesLineEdit.text(),
                                    "photo": self.photo,
                                    "color": self.color,
                                    "status": {
                                        "icon": list(self.status.values())[0]["icon"],
                                        "color": list(self.status.values())[0]["color"]
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

                    # Remove the blacked out widget from parent window and set the styleSheet to none
                    BlackedOutWidget.widget.setParent(None)
                    BlackedOutWidget.widget.setStyleSheet(None)

                    # Set the signal to False
                    EditAWord.signal = False

                    # Close the window
                    self.close()

            # Check if the signal to edit a word equals False
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

                    # Update the data in the dict
                    dictionary[CustomDictionaries.temporaryCustomDictionaryData["mainDictionaryName"]][
                        "custom_dictionaries"][CustomDictionaries.temporaryCustomDictionaryData["customDictionaryName"]]["words"].update(
                        {
                            self.uiAddAWordToACustomDictionary.wordLineEdit.text():
                                {
                                    "translation": self.uiAddAWordToACustomDictionary.translationLineEdit.text(),
                                    "additionalTranslation": self.uiAddAWordToACustomDictionary.additionalTranslationLineEdit.text(),
                                    "tags": self.uiAddAWordToACustomDictionary.tagsLineEdit.text(),
                                    "examples": self.uiAddAWordToACustomDictionary.examplesLineEdit.text(),
                                    "translationOfTheExamples": self.uiAddAWordToACustomDictionary.translationOfTheExamplesLineEdit.text(),
                                    "photo": self.photo,
                                    "color": self.color,
                                    "status": {
                                        "icon": list(self.status.values())[0]["icon"],
                                        "color": list(self.status.values())[0]["color"]
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
        else:
            pass
