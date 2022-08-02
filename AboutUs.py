from PyQt5 import QtCore, QtGui, QtWidgets


# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


class Ui_Form_aboutUs(object):
    def setupUi(self, Form, ratio_w, ratio_h, ratio_font):
        Form.setFixedSize(int(800 * ratio_w), int(475 * ratio_h))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file/aboutUs.png"))
        Form.setWindowIcon(icon)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(800 * ratio_w), int(475 * ratio_h)))
        self.widget.setStyleSheet("border-image : url('file/aboutUs.jpg');")

        # Label
        self.sajjad_label = QtWidgets.QLabel(Form)
        self.sajjad_label.setGeometry(QtCore.QRect(
            int(60 * ratio_w), int(20 * ratio_h), int(300 * ratio_w), int(100 * ratio_h)))
        self.sajjad_label.setFont(QtGui.QFont("Gabriola", int(40 * ratio_font)))

        self.rahmani_label = QtWidgets.QLabel(Form)
        self.rahmani_label.setGeometry(QtCore.QRect(
            int(25 * ratio_w), int(120 * ratio_h), int(300 * ratio_w), int(100 * ratio_h)))
        self.rahmani_label.setFont(QtGui.QFont("Gabriola", int(40 * ratio_font)))

        self.phone_label = QtWidgets.QLabel(Form)
        self.phone_label.setGeometry(QtCore.QRect(
            int(360 * ratio_w), int(235 * ratio_h), int(400 * ratio_w), int(80 * ratio_h)))
        self.phone_label.setFont(QtGui.QFont("Gabriola", int(28 * ratio_font)))
        self.phone_label.setText("github.com/RahmaniSajjad")
        self.phone_label.hide()

        self.insta_label = QtWidgets.QLabel(Form)
        self.insta_label.setGeometry(QtCore.QRect(
            int(360 * ratio_w), int(335 * ratio_h), int(420 * ratio_w), int(80 * ratio_h)))
        self.insta_label.setFont(QtGui.QFont("Gabriola", int(35 * ratio_font)))
        self.insta_label.setText("Twitter : @ id_Sajjad")
        self.insta_label.hide()

        self.email_label = QtWidgets.QLabel(Form)
        self.email_label.setGeometry(QtCore.QRect(
            int(360 * ratio_w), int(235 * ratio_h), int(420 * ratio_w), int(80 * ratio_h)))
        self.email_label.setFont(QtGui.QFont("Gabriola", int(25 * ratio_font)))
        self.email_label.setText("Rahmani.Sajjad.dev@gmail.com")
        self.email_label.hide()

        self.tel_label = QtWidgets.QLabel(Form)
        self.tel_label.setGeometry(QtCore.QRect(
            int(360 * ratio_w), int(235 * ratio_h), int(400 * ratio_w), int(80 * ratio_h)))
        self.tel_label.setFont(QtGui.QFont("Gabriola", int(35 * ratio_font)))
        self.tel_label.setText("Telegram : @ idSJD")
        self.tel_label.hide()

        # Push button
        self.phone_pushButton = QtWidgets.QPushButton(Form)
        self.phone_pushButton.setGeometry(QtCore.QRect(
            int(257 * ratio_w), int(239 * ratio_h), int(82 * ratio_w), int(82 * ratio_h)))
        self.phone_pushButton.setFlat(True)
        self.phone_pushButton.setToolTip("Github")
        self.phone_pushButton.clicked.connect(self.hideAll)
        self.phone_pushButton.clicked.connect(self.phone_label.show)

        self.emailpushButton = QtWidgets.QPushButton(Form)
        self.emailpushButton.setGeometry(QtCore.QRect(
            int(257 * ratio_w), int(14 * ratio_h), int(82 * ratio_w), int(82 * ratio_h)))
        self.emailpushButton.setFlat(True)
        self.emailpushButton.setToolTip("Gmail")
        self.emailpushButton.clicked.connect(self.hideAll)
        self.emailpushButton.clicked.connect(self.email_label.show)

        self.tel_insta_pushButton = QtWidgets.QPushButton(Form)
        self.tel_insta_pushButton.setGeometry(QtCore.QRect(
            int(250 * ratio_w), int(118 * ratio_h), int(96 * ratio_w), int(96 * ratio_h)))
        self.tel_insta_pushButton.setFlat(True)
        self.tel_insta_pushButton.setToolTip("Telegram & Twitter")
        self.tel_insta_pushButton.clicked.connect(self.hideAll)
        self.tel_insta_pushButton.clicked.connect(self.tel_label.show)
        self.tel_insta_pushButton.clicked.connect(self.insta_label.show)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "About us"))
        self.sajjad_label.setText(_translate("Form", "Sajjad"))
        self.rahmani_label.setText(_translate("Form", "Rahmani"))

    def hideAll(self):
        self.phone_label.hide()
        self.insta_label.hide()
        self.email_label.hide()
        self.tel_label.hide()
