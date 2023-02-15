from PyQt5 import QtCore, QtGui, QtWidgets

from MainWindow import Ui_Form_MainWindow


# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


class Ui_Form(object):
    def setupUi(self, Form):
        """
        Set up the user interface for the form.

        Args:
            Form (QWidget): The form widget to set up the UI for.
        """
        global ratio_w
        global ratio_h

        # Set the size of the form based on the ratio_w and ratio_h global variables.
        Form.setFixedSize(int(410 * ratio_w), int(250 * ratio_h))

        # Set the window icon of the form.
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file/appIcon.png"))
        Form.setWindowIcon(icon)

        # Create a widget to hold the other UI elements.
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(410 * ratio_w), int(250 * ratio_h)))
        self.widget.setStyleSheet("background-color: white;")

        # Create a push button to start the application.
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(
            int(155 * ratio_w), int(215 * ratio_h), int(100 * ratio_w), int(30 * ratio_h)))
        self.pushButton1.setFont(QtGui.QFont("MV Boli", int(15 * ratio_font)))
        # self.pushButton1.setFlat(True)
        self.pushButton1.clicked.connect(self.action_pushButton1)
        self.pushButton1.setStyleSheet(
            f"""border :1px solid black;border-radius :{int(15 * (ratio_w + ratio_h) / 2)}px;""")

        # Create a label to hold a GIF animation and start the animation.
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(
            int(5 * ratio_w), int(5 * ratio_h), int(400 * ratio_w), int(202 * ratio_h)))
        self.gif = QtGui.QMovie("file/start.gif")
        self.gif.setScaledSize(QtCore.QSize(
            int(400 * ratio_w), int(202 * ratio_h)))
        self.label1.setMovie(self.gif)
        self.gif.start()

        # Set up the translations for the form.
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def action_pushButton1(self):
        """
        Define the action to perform when the pushButton1 is clicked.
        Opens a new dialog window and closes the current window.

        The new dialog window is created using the Ui_Form_MainWindow class, and is passed the
        values of the ratio_w, ratio_h, and ratio_font global variables.
        """
        global ratio_w
        global ratio_h

        # Create a new QDialog window and set up the UI using the Ui_Form_MainWindow class.
        Form_MainWindow = QtWidgets.QDialog()
        ui = Ui_Form_MainWindow()
        ui.setupUi(Form_MainWindow, ratio_w, ratio_h, ratio_font)

        # Show the new window, close the current window, and execute the new window.
        Form_MainWindow.show()
        Form.close()
        Form_MainWindow.exec_()

    def retranslateUi(self, Form):
        """
        Set the text and title for the UI elements in the Form.

        The window title and the text on the pushButton1 are set using the QtCore.QCoreApplication
        library's translate method.
        """
        _translate = QtCore.QCoreApplication.translate

        # Set the window title to "Start Contacts".
        Form.setWindowTitle(_translate("Form", "Start Contacts"))

        # Set the text on pushButton1 to "Start".
        self.pushButton1.setText(_translate("Form", "Start"))


if __name__ == "__main__":
    import sys

    # Create a QApplication object.
    app = QtWidgets.QApplication(sys.argv)

    # Calculate the ratios for window size and font size based on the user's screen resolution.
    ratio_w = app.primaryScreen().size().width() / 1920
    ratio_h = app.primaryScreen().size().height() / 1080
    ratio_font = app.fontMetrics().fontDpi() / 120

    # Create a new QWidget window and set up the UI using the Ui_Form class.
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    # Show the new window and execute the application.
    Form.show()
    sys.exit(app.exec_())
