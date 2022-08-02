from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import re


# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


class Ui_Form_addContact(object):
    def setupUi(self, Form, ratio_w, ratio_h, ratio_font):
        Form.setFixedSize(int(900 * ratio_w), int(600 * ratio_h))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file/addContact.ico"))
        Form.setWindowIcon(icon)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(900 * ratio_w), int(600 * ratio_h)))
        self.widget.setStyleSheet("border-image : url('file/addContact_background.jpg');")

        # Label
        self.top_label = QtWidgets.QLabel(Form)
        self.top_label.setGeometry(QtCore.QRect(
            int(480 * ratio_w), int(90 * ratio_h), int(220 * ratio_w), int(30 * ratio_h)))
        self.top_label.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))

        self.name_label = QtWidgets.QLabel(Form)
        self.name_label.setGeometry(QtCore.QRect(
            int(440 * ratio_w), int(180 * ratio_h), int(70 * ratio_w), int(20 * ratio_h)))
        self.name_label.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))

        self.last_name_label = QtWidgets.QLabel(Form)
        self.last_name_label.setGeometry(QtCore.QRect(
            int(440 * ratio_w), int(240 * ratio_h), int(90 * ratio_w), int(20 * ratio_h)))
        self.last_name_label.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))

        self.number_label = QtWidgets.QLabel(Form)
        self.number_label.setGeometry(QtCore.QRect(
            int(440 * ratio_w), int(300 * ratio_h), int(80 * ratio_w), int(20 * ratio_h)))
        self.number_label.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))

        self.email_label = QtWidgets.QLabel(Form)
        self.email_label.setGeometry(QtCore.QRect(
            int(440 * ratio_w), int(360 * ratio_h), int(70 * ratio_w), int(20 * ratio_h)))
        self.email_label.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))

        self.address_label = QtWidgets.QLabel(Form)
        self.address_label.setGeometry(QtCore.QRect(
            int(440 * ratio_w), int(420 * ratio_h), int(70 * ratio_w), int(20 * ratio_h)))
        self.address_label.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))

        # three statuses of saving label
        self.saved_label = QtWidgets.QLabel(Form)
        self.saved_label.setGeometry(QtCore.QRect(
            int(260 * ratio_w), int(310 * ratio_h), int(70 * ratio_w), int(25 * ratio_h)))
        self.saved_label.setFont(QtGui.QFont("Gabriola", int(17 * ratio_font)))
        self.saved_label.setStyleSheet("color:white")
        self.saved_label.setText("Saved !")
        self.saved_label.hide()

        self.invalid_label = QtWidgets.QLabel(Form)
        self.invalid_label.setGeometry(QtCore.QRect(
            int(255 * ratio_w), int(310 * ratio_h), int(70 * ratio_w), int(25 * ratio_h)))
        self.invalid_label.setFont(QtGui.QFont("Gabriola", int(17 * ratio_font)))
        self.invalid_label.setStyleSheet("color:white")
        self.invalid_label.setText("Invalid !")
        self.invalid_label.hide()

        self.exist_label = QtWidgets.QLabel(Form)
        self.exist_label.setGeometry(QtCore.QRect(
            int(227 * ratio_w), int(310 * ratio_h), int(140 * ratio_w), int(25 * ratio_h)))
        self.exist_label.setFont(QtGui.QFont("Gabriola", int(17 * ratio_font)))
        self.exist_label.setStyleSheet("color:white")
        self.exist_label.setText("Already exist !")
        self.exist_label.hide()

        # label for random contact
        self.no_internet_label = QtWidgets.QLabel(Form)
        self.no_internet_label.setGeometry(QtCore.QRect(
            int(235 * ratio_w), int(310 * ratio_h), int(120 * ratio_w), int(25 * ratio_h)))
        self.no_internet_label.setFont(QtGui.QFont("Gabriola", int(17 * ratio_font)))
        self.no_internet_label.setStyleSheet("color:white")
        self.no_internet_label.setText("No internet !")
        self.no_internet_label.hide()

        self.Error_label = QtWidgets.QLabel(Form)
        self.Error_label.setGeometry(QtCore.QRect(
            int(260 * ratio_w), int(310 * ratio_h), int(70 * ratio_w), int(25 * ratio_h)))
        self.Error_label.setFont(QtGui.QFont("Gabriola", int(17 * ratio_font)))
        self.Error_label.setStyleSheet("color:white")
        self.Error_label.setText("Error !")
        self.Error_label.hide()

        # Line Edit
        self.name_lineEdit = QtWidgets.QLineEdit(Form)
        self.name_lineEdit.setGeometry(QtCore.QRect(
            int(540 * ratio_w), int(180 * ratio_h), int(200 * ratio_w), int(25 * ratio_h)))
        self.name_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.name_lineEdit.setFrame(False)
        self.name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.name_lineEdit.setPlaceholderText("Enter name here")
        self.name_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)

        self.last_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.last_name_lineEdit.setGeometry(QtCore.QRect(
            int(540 * ratio_w), int(240 * ratio_h), int(200 * ratio_w), int(25 * ratio_h)))
        self.last_name_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.last_name_lineEdit.setFrame(False)
        self.last_name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.last_name_lineEdit.setPlaceholderText("Enter last name here")
        self.last_name_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)

        self.number_lineEdit = QtWidgets.QLineEdit(Form)
        self.number_lineEdit.setGeometry(QtCore.QRect(
            int(540 * ratio_w), int(300 * ratio_h), int(200 * ratio_w), int(25 * ratio_h)))
        self.number_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.number_lineEdit.setFrame(False)
        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.number_lineEdit.setPlaceholderText("Enter number here")
        rx_number_lineEdit = QtCore.QRegExp("[0-9|+|-]*")
        val_number_lineEdit = QtGui.QRegExpValidator(rx_number_lineEdit)
        self.number_lineEdit.setValidator(val_number_lineEdit)
        self.number_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)

        self.email_lineEdit = QtWidgets.QLineEdit(Form)
        self.email_lineEdit.setGeometry(QtCore.QRect(
            int(540 * ratio_w), int(360 * ratio_h), int(200 * ratio_w), int(25 * ratio_h)))
        self.email_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.email_lineEdit.setFrame(False)
        self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.email_lineEdit.setPlaceholderText("Enter email here")
        rx_email_lineEdit = QtCore.QRegExp(
            "[a-z|A-Z|0-9]{1}[a-z|A-Z|0-9|\.]{5,29}@[a-z|A-Z]+\.[a-z|A-Z]+"
        )
        val_email_lineEdit = QtGui.QRegExpValidator(rx_email_lineEdit)
        self.email_lineEdit.setValidator(val_email_lineEdit)
        self.email_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)

        self.address_lineEdit = QtWidgets.QLineEdit(Form)
        self.address_lineEdit.setGeometry(QtCore.QRect(
            int(540 * ratio_w), int(420 * ratio_h), int(200 * ratio_w), int(25 * ratio_h)))
        self.address_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.address_lineEdit.setFrame(False)
        self.address_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.address_lineEdit.setPlaceholderText("Enter address here (Optional)")
        self.address_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)

        # Push button
        self.save_pushButton = QtWidgets.QPushButton(Form)
        self.save_pushButton.setGeometry(QtCore.QRect(
            int(305 * ratio_w), int(480 * ratio_h), int(60 * ratio_w), int(30 * ratio_h)))
        self.save_pushButton.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.save_pushButton.setFlat(True)
        self.save_pushButton.clicked.connect(self.save_action)

        self.cancel_pushButton = QtWidgets.QPushButton(Form)
        self.cancel_pushButton.setGeometry(QtCore.QRect(
            int(295 * ratio_w), int(530 * ratio_h), int(80 * ratio_w), int(30 * ratio_h)))
        self.cancel_pushButton.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.cancel_pushButton.setFlat(True)
        self.cancel_pushButton.clicked.connect(Form.close)

        self.clear_pushButton = QtWidgets.QPushButton(Form)
        self.clear_pushButton.setGeometry(QtCore.QRect(
            int(300 * ratio_w), int(430 * ratio_h), int(70 * ratio_w), int(30 * ratio_h)))
        self.clear_pushButton.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.clear_pushButton.setFlat(True)
        self.clear_pushButton.clicked.connect(self.clear_action)

        self.random_contact_pushButton = QtWidgets.QPushButton(Form)
        self.random_contact_pushButton.setGeometry(QtCore.QRect(
            int(447 * ratio_w), int(500 * ratio_h), int(280 * ratio_w), int(35 * ratio_h)))
        self.random_contact_pushButton.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.random_contact_pushButton.setFlat(True)
        self.random_contact_pushButton.setStyleSheet(
            f"border :1px solid black;border-radius :{int(15 * (ratio_w + ratio_h) / 2)}px;" + "color:#550000;")
        self.random_contact_pushButton.clicked.connect(self.random_contact_action)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add contact"))
        self.top_label.setText(_translate("Form", "Create a new contact"))
        self.name_label.setText(_translate("Form", "Name :"))
        self.last_name_label.setText(_translate("Form", "Last name :"))
        self.number_label.setText(_translate("Form", "Number :"))
        self.email_label.setText(_translate("Form", "Email :"))
        self.address_label.setText(_translate("Form", "Address :"))
        self.save_pushButton.setText(_translate("Form", "Save"))
        self.cancel_pushButton.setText(_translate("Form", "Cancel"))
        self.clear_pushButton.setText(_translate("Form", "Clear"))
        self.random_contact_pushButton.setText(_translate("Form", "Create a random contact"))

    def clear_action(self):
        self.name_lineEdit.setText("")
        self.last_name_lineEdit.setText("")
        self.number_lineEdit.setText("")
        self.email_lineEdit.setText("")
        self.address_lineEdit.setText("")

        self.invalid_label.hide()
        self.exist_label.hide()
        self.saved_label.hide()
        self.no_internet_label.hide()
        self.Error_label.hide()

        self.name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.last_name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")

    def save_action(self):
        name = self.name_lineEdit.text()
        last_name = self.last_name_lineEdit.text()
        number = self.number_lineEdit.text()
        email = self.email_lineEdit.text()
        address = self.address_lineEdit.text()
        status = 0

        # Verify inputs
        def email_verify(input_email):
            import re
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]+\b'

            if re.match(regex, input_email):
                return True

            else:
                return False

        # set default all line edit
        self.name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.last_name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")

        if len(name) < 2:
            self.name_lineEdit.setStyleSheet("background-color:#ffa0a0;")
            status = 1

        else:
            # set default all line edit
            self.name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
            self.last_name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
            self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
            self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")

            if len(last_name) < 2:
                self.last_name_lineEdit.setStyleSheet("background-color:#ffa0a0;")
                status = 1

            else:
                # set default all line edit
                self.name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                self.last_name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")

                if len(number) < 7:
                    self.number_lineEdit.setStyleSheet("background-color:#ffa0a0;")
                    status = 1

                else:
                    # set default all line edit
                    self.name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                    self.last_name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                    self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                    self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")

                    if not (email_verify(email)):
                        self.email_lineEdit.setStyleSheet("background-color:#ffa0a0;")
                        status = 1
                    else:
                        # set default all line edit
                        self.name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                        self.last_name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                        self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")

        #####################

        # check is it exist
        if status == 0:
            with open("file/Contacts.txt", "rt") as file:
                for i in file:
                    line = i[0:-1].split("---")
                    if f"'{number}'" == line[2]:
                        self.number_lineEdit.setStyleSheet("background-color:#ffa0a0;")
                        status = 2
                        break
                    elif f"'{email}'" == line[3]:
                        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                        self.email_lineEdit.setStyleSheet("background-color:#ffa0a0;")
                        status = 2
                        break
                    else:
                        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                        self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")

        #################################################

        if status == 0:
            # add contact
            with open("file/Contacts.txt", "at") as file:
                file.write(f"'{name}'---'{last_name}'---'{number}'---'{email}'---'{address}'\n")

            self.clear_action()

            self.invalid_label.hide()
            self.exist_label.hide()
            self.no_internet_label.hide()
            self.Error_label.hide()
            self.saved_label.show()

        elif status == 1:
            self.exist_label.hide()
            self.saved_label.hide()
            self.no_internet_label.hide()
            self.Error_label.hide()
            self.invalid_label.show()

        elif status == 2:
            self.invalid_label.hide()
            self.saved_label.hide()
            self.no_internet_label.hide()
            self.Error_label.hide()
            self.exist_label.show()

    def random_contact_action(self):
        self.clear_action()
        url = 'http://fakenamegenerator.com'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        try:
            result = requests.get(url, headers=headers)
            page = result.content.decode()

            regex = """<h3>(.*)</h3>"""
            fullname = re.findall(regex, page)
            name = fullname[0].split(" ", 1)[0]
            last_name = fullname[0].split(" ", 1)[1]
            last_name = "".join([i for i in last_name if i != " "])

            regex = """        <dt>Phone</dt>
        <dd>(.*)</dd>"""
            number = re.findall(regex, page)
            number = "+1" + "".join([i for i in number[0] if i.isdigit()])

            regex = """        <dt>Email Address</dt>

                    <dd>(.*)            <div"""
            email = re.findall(regex, page)
            email = email[0]

            regex = """<div class="adr">
                                        (.*)<br />(.*)                                        </div>"""
            address = re.findall(regex, page)
            address = address[0][0] + " - " + address[0][1]

            self.name_lineEdit.setText(name)
            self.last_name_lineEdit.setText(last_name)
            self.number_lineEdit.setText(number)
            self.email_lineEdit.setText(email)
            self.address_lineEdit.setText(address)

            self.invalid_label.hide()
            self.exist_label.hide()
            self.no_internet_label.hide()
            self.Error_label.hide()
            self.saved_label.hide()

        except requests.exceptions.ConnectionError:
            self.invalid_label.hide()
            self.exist_label.hide()
            self.saved_label.hide()
            self.Error_label.hide()
            self.no_internet_label.show()

        except:
            self.invalid_label.hide()
            self.exist_label.hide()
            self.saved_label.hide()
            self.no_internet_label.hide()
            self.Error_label.show()
