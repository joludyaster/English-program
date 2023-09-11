class LocalDatabase:
    temporaryData = {}
    userLoginData = {}
    temporaryDictionaryData = None


class BlackedOutWidget:
    widget = None


class CustomDictionaries:
    temporaryCustomDictionaryData = {}
    stackedWidget = None
    dashboardPage = None


class EditADictionary:
    signal = False
    dataToFillUp = {}
    object = None


class RemoveSomething:
    signal = False


class EditACustomDictionary:
    dataToFillUp = {}
    signal = False
    mainDictionary = None


class EditAWord:
    dataToFillUp = {}
    signal = False
    mainDictionary = None
    customDictionary = None


class PassParameters:
    parameters = {
        "self": None,
        "sender_obj": None,
        "main_parent_widget": None,
        "dictionary_parent": None
    }
