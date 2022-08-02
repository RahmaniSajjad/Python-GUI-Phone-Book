from PyQt5 import QtCore, QtGui, QtWidgets


# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


class Ui_Form_SearchContacts(object):
    def setupUi(self, Form, w, h, f):
        global ratio_w
        global ratio_h
        global ratio_font
        ratio_w = w
        ratio_h = h
        ratio_font = f

        Form.setFixedSize(int(1200 * ratio_w), int(680 * ratio_h))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file/searchContact.png"))
        Form.setWindowIcon(icon)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(1200 * ratio_w), int(680 * ratio_h)))
        self.widget.setStyleSheet("border-image : url('file/SearchContacts_background.jpg');")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(
            int(20 * ratio_w), int(40 * ratio_h), int(661 * ratio_w), int(500 * ratio_h)))
        self.tableWidget.setFont(QtGui.QFont("Calibri", int(12 * ratio_font)))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.cellDoubleClicked['int', 'int'].connect(self.tableWidget_action_calculate)
        self.tableWidget.cellDoubleClicked.connect(lambda: self.tableWidget_action_show(Form))

        # HorizontalHeader (tableWidget)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)

        item = QtWidgets.QTableWidgetItem()
        item.setFont(QtGui.QFont("Gabriola", int(18 * ratio_font)))
        self.tableWidget.setHorizontalHeaderItem(0, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(int(620 * ratio_w))
        self.tableWidget.verticalHeader().setDefaultSectionSize(int(60 * ratio_h))

        # Completer
        completer_options = []
        with open("file/Contacts.txt", "rt") as file:
            for i in file:
                line = i[0:-1].split("---")

                completer_options.append("@" + line[0][1:-1] + line[1][1:-1])
                completer_options.append("#" + line[2][2:-1])

        self.completer = QtWidgets.QCompleter(completer_options)
        self.completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

        # Line Edit
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(
            int(800 * ratio_w), int(30 * ratio_h), int(350 * ratio_w), int(30 * ratio_h)))
        self.lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.lineEdit.setStyleSheet("QLineEdit:hover{background-color: #e10e10e10;}")
        self.lineEdit.setPlaceholderText("Enter your text here for advanced search")
        self.lineEdit.setCompleter(self.completer)

        # Text Edit
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(
            int(800 * ratio_w), int(80 * ratio_h), int(350 * ratio_w), int(380 * ratio_h)))
        self.textEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.textEdit.setStyleSheet("QTextEdit:hover{background-color: #e10e10e10;}")
        self.textEdit.setPlaceholderText("Enter your text here")

        # Push Button
        self.search_pushButton = QtWidgets.QPushButton(Form)
        self.search_pushButton.setGeometry(QtCore.QRect(
            int(940 * ratio_w), int(505 * ratio_h), int(100 * ratio_w), int(100 * ratio_h)))
        self.search_pushButton.setFlat(True)
        self.search_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/SearchPushbutton.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.search_pushButton.setToolTip("Click to search from contacts")
        self.search_pushButton.clicked.connect(self.regex_action)

        # LCD
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(
            int(430 * ratio_w), int(520 * ratio_h), int(120 * ratio_w), int(120 * ratio_h)))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setStyleSheet("color:white")

        # Label
        self.Contacts_number_label = QtWidgets.QLabel(Form)
        self.Contacts_number_label.setGeometry(QtCore.QRect(
            int(30 * ratio_w), int(550 * ratio_h), int(420 * ratio_w), int(60 * ratio_h)))
        self.Contacts_number_label.setFont(QtGui.QFont("Gabriola", int(30 * ratio_font)))
        self.Contacts_number_label.setStyleSheet("color:white")
        self.Contacts_number_label.setText("Number of contacts found :")

        self.retranslateUi(Form)
        self.tableWidget.setSortingEnabled(True)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def regex_action(self):
        text = self.lineEdit.text()
        if len(text) == 0:
            text = self.textEdit.toPlainText()

        import re
        name_lastName_list = re.findall(r'@([\w.]+)', text)
        number_list = re.findall(r'#(\d+)', text)

        names = []
        last_names = []
        numbers = []
        emails = []
        addresses = []

        with open("file/Contacts.txt", "rt") as file:
            lines = file.readlines()

        for nameLastName in name_lastName_list:
            for i in lines:
                line = i[0:-1].split("---")

                if line[0][1:-1] + line[1][1:-1] == nameLastName:
                    names.append(line[0])
                    last_names.append(line[1])
                    numbers.append(line[2])
                    emails.append(line[3])
                    addresses.append(line[4])

        for num in number_list:
            for i in lines:
                line = i[0:-1].split("---")

                if (line[2][2:-1] == num) and (line[2] not in numbers):
                    names.append(line[0])
                    last_names.append(line[1])
                    numbers.append(line[2])
                    emails.append(line[3])
                    addresses.append(line[4])

        self.contact_list = list(zip(names, last_names, numbers, emails, addresses))
        self.show_contacts()

    def show_contacts(self):
        Row = 0
        self.tableWidget.setRowCount(Row)
        for contact in self.contact_list:
            self.tableWidget.setRowCount(Row + 1)

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(Row, 0, item)
            text = f" ---> Name : {contact[0][1:-1]} | Last name : {contact[1][1:-1]} | " \
                   f"Number : {contact[2][1:-1]} <--- "
            item.setText(text)

            Row += 1

        self.lcdNumber.display(Row)

    def tableWidget_action_calculate(self, row):
        self.name_selected = self.contact_list[row][0][1:-1]
        self.last_name_selected = self.contact_list[row][1][1:-1]
        self.number_selected = self.contact_list[row][2][1:-1]
        self.email_selected = self.contact_list[row][3][1:-1]
        self.address_selected = self.contact_list[row][4][1:-1]

    def tableWidget_action_show(self, Form):
        global ratio_w
        global ratio_h

        self.single_contact_widget = QtWidgets.QWidget(Form)
        self.single_contact_widget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(1200 * ratio_w), int(680 * ratio_h)))

        self.widget = QtWidgets.QWidget(self.single_contact_widget)
        self.widget.setGeometry(QtCore.QRect(
            int(180 * ratio_w), int(65 * ratio_h), int(341 * ratio_w), int(450 * ratio_h)))
        self.widget.setStyleSheet("border-image : url('file/showSearchedContact_background.png');")

        # Label
        self.top_label = QtWidgets.QLabel(self.single_contact_widget)
        self.top_label.setGeometry(QtCore.QRect(
            int(280 * ratio_w), int(160 * ratio_h), int(150 * ratio_w), int(30 * ratio_h)))
        self.top_label.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.top_label.setText("Show Contact")

        self.name_label = QtWidgets.QLabel(self.single_contact_widget)
        self.name_label.setGeometry(QtCore.QRect(
            int(240 * ratio_w), int(220 * ratio_h), int(80 * ratio_w), int(30 * ratio_h)))
        self.name_label.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))
        self.name_label.setText("Name :")

        self.last_name_label = QtWidgets.QLabel(self.single_contact_widget)
        self.last_name_label.setGeometry(QtCore.QRect(
            int(240 * ratio_w), int(270 * ratio_h), int(150 * ratio_w), int(30 * ratio_h)))
        self.last_name_label.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))
        self.last_name_label.setText("Last name :")

        self.number_label = QtWidgets.QLabel(self.single_contact_widget)
        self.number_label.setGeometry(QtCore.QRect(
            int(240 * ratio_w), int(320 * ratio_h), int(120 * ratio_w), int(30 * ratio_h)))
        self.number_label.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))
        self.number_label.setText("Number :")

        self.email_label = QtWidgets.QLabel(self.single_contact_widget)
        self.email_label.setGeometry(QtCore.QRect(
            int(240 * ratio_w), int(370 * ratio_h), int(100 * ratio_w), int(30 * ratio_h)))
        self.email_label.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))
        self.email_label.setText("Email :")

        self.address_label = QtWidgets.QLabel(self.single_contact_widget)
        self.address_label.setGeometry(QtCore.QRect(
            int(240 * ratio_w), int(420 * ratio_h), int(120 * ratio_w), int(30 * ratio_h)))
        self.address_label.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))
        self.address_label.setText("Address :")

        # Line Edit
        self.name_lineEdit = QtWidgets.QLineEdit(self.single_contact_widget)
        self.name_lineEdit.setGeometry(QtCore.QRect(
            int(340 * ratio_w), int(225 * ratio_h), int(130 * ratio_w), int(25 * ratio_h)))
        self.name_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.name_lineEdit.setFrame(False)
        self.name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.name_lineEdit.setText(self.name_selected)
        self.name_lineEdit.setReadOnly(True)
        self.name_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)

        self.last_name_lineEdit = QtWidgets.QLineEdit(self.single_contact_widget)
        self.last_name_lineEdit.setGeometry(QtCore.QRect(
            int(340 * ratio_w), int(275 * ratio_h), int(130 * ratio_w), int(25 * ratio_h)))
        self.last_name_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.last_name_lineEdit.setFrame(False)
        self.last_name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.last_name_lineEdit.setText(self.last_name_selected)
        self.last_name_lineEdit.setReadOnly(True)
        self.last_name_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)

        self.number_lineEdit = QtWidgets.QLineEdit(self.single_contact_widget)
        self.number_lineEdit.setGeometry(QtCore.QRect(
            int(340 * ratio_w), int(325 * ratio_h), int(130 * ratio_w), int(25 * ratio_h)))
        self.number_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.number_lineEdit.setFrame(False)
        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.number_lineEdit.setText(self.number_selected)
        self.number_lineEdit.setReadOnly(True)
        self.number_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)

        self.email_lineEdit = QtWidgets.QLineEdit(self.single_contact_widget)
        self.email_lineEdit.setGeometry(QtCore.QRect(
            int(340 * ratio_w), int(375 * ratio_h), int(130 * ratio_w), int(25 * ratio_h)))
        self.email_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.email_lineEdit.setFrame(False)
        self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.email_lineEdit.setText(self.email_selected)
        self.email_lineEdit.setReadOnly(True)
        self.email_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)

        self.address_lineEdit = QtWidgets.QLineEdit(self.single_contact_widget)
        self.address_lineEdit.setGeometry(QtCore.QRect(
            int(340 * ratio_w), int(425 * ratio_h), int(130 * ratio_w), int(25 * ratio_h)))
        self.address_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.address_lineEdit.setFrame(False)
        self.address_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.address_lineEdit.setText(self.address_selected)
        self.address_lineEdit.setReadOnly(True)
        self.address_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)

        # Push button
        self.close_pushButton = QtWidgets.QPushButton(self.single_contact_widget)
        self.close_pushButton.setGeometry(QtCore.QRect(
            int(445 * ratio_w), int(100 * ratio_h), int(32 * ratio_w), int(32 * ratio_h)))
        self.close_pushButton.setFlat(True)
        self.close_pushButton.setStyleSheet("border-image : url('file/SingleContact_close.png');")
        self.close_pushButton.clicked.connect(self.single_contact_widget.hide)

        self.single_contact_widget.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Search Contacts"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Contacts List"))


ratio_w = 1
ratio_h = 1
ratio_font = 1
