import sys

from PySide6.QtGui import QFontDatabase

import windows

from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication()

    widget = windows.LoginWindow()

    for font in ["fonts/Montserrat-Black.ttf", "fonts/Montserrat-BlackItalic.ttf",
                 "fonts/Montserrat-Bold.ttf", "fonts/Montserrat-BoldItalic.ttf",
                 "fonts/Montserrat-ExtraBold.ttf", "fonts/Montserrat-ExtraBoldItalic.ttf",
                 "fonts/Montserrat-ExtraLight.ttf", "fonts/Montserrat-ExtraLightItalic.ttf",
                 "fonts/Montserrat-Italic.ttf", "fonts/Montserrat-Light.ttf",
                 "fonts/Montserrat-LightItalic.ttf", "fonts/Montserrat-Medium.ttf",
                 "fonts/Montserrat-MediumItalic.ttf", "fonts/Montserrat-Regular.ttf",
                 "fonts/Montserrat-SemiBold.ttf", "fonts/Montserrat-SemiBoldItalic.ttf",
                 "fonts/Montserrat-Thin.ttf", "fonts/Montserrat-ThinItalic.ttf"]:
        customFont = QFontDatabase.addApplicationFont(font)
        if customFont < 0:
            print(f"[ERROR]: Font {font} wasn't installed...")

        families = QFontDatabase.applicationFontFamilies(customFont)

    widget.show()
    sys.exit(app.exec())
