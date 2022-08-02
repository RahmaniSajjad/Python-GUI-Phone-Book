from PyQt5 import QtCore, QtGui, QtWidgets


# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


class Ui_Form_advancedShutdown(object):
    def setupUi(self, Form, ratio_w, ratio_h, ratio_font):
        Form.setFixedSize(int(460 * ratio_w), int(258 * ratio_h))
        Form.setWindowTitle("Advanced Shutdown")

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(460 * ratio_w), int(258 * ratio_h)))
        self.widget.setStyleSheet("border-image : url('file/advancedShutdown_background.png');")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file/advancedShutdown.png"))
        Form.setWindowIcon(icon)

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(
            int(145 * ratio_w), int(30 * ratio_h), int(170 * ratio_w), int(35 * ratio_h)))
        self.comboBox.setStyleSheet("color:white; background-color:black;")
        self.comboBox.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.hour_spinBox = QtWidgets.QSpinBox(Form)
        self.hour_spinBox.setGeometry(QtCore.QRect(
            int(10 * ratio_w), int(190 * ratio_h), int(140 * ratio_w), int(25 * ratio_h)))
        self.hour_spinBox.setStyleSheet("color:white; background-color:black;")
        self.hour_spinBox.setFrame(False)
        self.hour_spinBox.setFont(QtGui.QFont("Gabriola", int(14 * ratio_font)))
        self.hour_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_spinBox.setMaximum(59)
        self.hour_spinBox.setPrefix('after : ')  # پیشوند
        self.hour_spinBox.setSuffix(' hour')  # پسوند

        self.minute_spinBox = QtWidgets.QSpinBox(Form)
        self.minute_spinBox.setGeometry(QtCore.QRect(
            int(160 * ratio_w), int(190 * ratio_h), int(140 * ratio_w), int(25 * ratio_h)))
        self.minute_spinBox.setStyleSheet("color:white; background-color:black;")
        self.minute_spinBox.setFrame(False)
        self.minute_spinBox.setFont(QtGui.QFont("Gabriola", int(14 * ratio_font)))
        self.minute_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.minute_spinBox.setMaximum(59)
        self.minute_spinBox.setPrefix('and ')  # پیشوند
        self.minute_spinBox.setSuffix(' minute')  # پسوند

        self.second_spinBox = QtWidgets.QSpinBox(Form)
        self.second_spinBox.setGeometry(QtCore.QRect(
            int(310 * ratio_w), int(190 * ratio_h), int(140 * ratio_w), int(25 * ratio_h)))
        self.second_spinBox.setStyleSheet("color:white; background-color:black;")
        self.second_spinBox.setFrame(False)
        self.second_spinBox.setFont(QtGui.QFont("Gabriola", int(14 * ratio_font)))
        self.second_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.second_spinBox.setMaximum(59)
        self.second_spinBox.setPrefix('and ')  # پیشوند
        self.second_spinBox.setSuffix(' second')  # پسوند

        self.logOut_pushButton = QtWidgets.QPushButton(Form)
        self.logOut_pushButton.setGeometry(QtCore.QRect(
            int(193 * ratio_w), int(92 * ratio_h), int(74 * ratio_w), int(74 * ratio_h)))
        self.logOut_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/logOut_pushButton.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.logOut_pushButton.setFlat(True)
        self.logOut_pushButton.setToolTip("Log out now")
        self.logOut_pushButton.clicked.connect(self.logOut_action)

        self.apply_pushButton = QtWidgets.QPushButton(Form)
        self.apply_pushButton.setGeometry(QtCore.QRect(
            int(60 * ratio_w), int(105 * ratio_h), int(80 * ratio_w), int(45 * ratio_h)))
        self.apply_pushButton.setStyleSheet("color:white; background-color:black;")
        self.apply_pushButton.setFlat(True)
        self.apply_pushButton.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.apply_pushButton.clicked.connect(lambda: self.apply_action(Form))

        self.cancel_pushButton = QtWidgets.QPushButton(Form)
        self.cancel_pushButton.setGeometry(QtCore.QRect(
            int(320 * ratio_w), int(105 * ratio_h), int(80 * ratio_w), int(45 * ratio_h)))
        self.cancel_pushButton.setStyleSheet("color:white; background-color:black;")
        self.cancel_pushButton.setFlat(True)
        self.cancel_pushButton.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.cancel_pushButton.clicked.connect(Form.close)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.comboBox.setItemText(0, _translate("Form", "Select an option"))
        self.comboBox.setItemText(1, _translate("Form", "Shutdown"))
        self.comboBox.setItemText(2, _translate("Form", "Restart"))
        self.comboBox.setItemText(3, _translate("Form", "Hibernate"))
        self.apply_pushButton.setText(_translate("Form", "Apply"))
        self.cancel_pushButton.setText(_translate("Form", "Cancel"))

    def apply_action(self, Form):
        hour = self.hour_spinBox.value()
        minute = self.minute_spinBox.value()
        second = self.second_spinBox.value()

        time = hour * 3600 + minute * 60 + second

        import os

        if self.comboBox.currentIndex() == 1:
            os.system(f"shutdown /s /t {time}")
            Form.close()

        elif self.comboBox.currentIndex() == 2:
            os.system(f"shutdown /r /t {time}")
            Form.close()

        elif self.comboBox.currentIndex() == 3:
            os.system(f"shutdown /h /t {time}")
            Form.close()

    def logOut_action(self):
        import os
        os.system("shutdown /l")
