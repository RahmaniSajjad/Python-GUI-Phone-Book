from PyQt5 import QtCore, QtGui, QtWidgets

from MainWindow import Ui_Form_MainWindow


# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


class Ui_Form(object):
    def setupUi(self, Form):
        global ratio_w
        global ratio_h

        Form.setFixedSize(int(410 * ratio_w), int(250 * ratio_h))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file/appIcon.png"))
        Form.setWindowIcon(icon)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(410 * ratio_w), int(250 * ratio_h)))
        self.widget.setStyleSheet("background-color: white;")

        # Create start pushButton
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(
            int(155 * ratio_w), int(215 * ratio_h), int(100 * ratio_w), int(30 * ratio_h)))
        self.pushButton1.setFont(QtGui.QFont("MV Boli", int(15 * ratio_font)))
        # self.pushButton1.setFlat(True)
        self.pushButton1.clicked.connect(self.action_pushButton1)
        self.pushButton1.setStyleSheet(
            f"""border :1px solid black;border-radius :{int(15 * (ratio_w + ratio_h) / 2)}px;""")
        #####################

        # Create label & add gif to it & start gif
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(
            int(5 * ratio_w), int(5 * ratio_h), int(400 * ratio_w), int(202 * ratio_h)))
        self.gif = QtGui.QMovie("file/start.gif")
        self.gif.setScaledSize(QtCore.QSize(
            int(400 * ratio_w), int(202 * ratio_h)))
        self.label1.setMovie(self.gif)
        self.gif.start()
        #####################################

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def action_pushButton1(self):
        global ratio_w
        global ratio_h

        Form_MainWindow = QtWidgets.QDialog()
        ui = Ui_Form_MainWindow()
        ui.setupUi(Form_MainWindow, ratio_w, ratio_h, ratio_font)
        Form_MainWindow.show()
        Form.close()
        Form_MainWindow.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Start Contacts"))
        self.pushButton1.setText(_translate("Form", "Start"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    ratio_w = app.primaryScreen().size().width() / 1920
    ratio_h = app.primaryScreen().size().height() / 1080
    ratio_font = app.fontMetrics().fontDpi() / 120

    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
