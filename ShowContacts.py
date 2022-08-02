from PyQt5 import QtCore, QtGui, QtWidgets
from gtts import gTTS
from playsound import playsound
import os


# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


class Ui_Form_ShowContacts(object):
    def setupUi(self, Form, w, h, f):
        global ratio_w
        global ratio_h
        global ratio_font
        ratio_w = w
        ratio_h = h
        ratio_font = f

        Form.setFixedSize(int(1380 * ratio_w), int(917 * ratio_h))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file/showContact.ico"))
        Form.setWindowIcon(icon)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(1380 * ratio_w), int(917 * ratio_h)))
        self.widget.setStyleSheet("border-image : url('file/showContact_background.jpg');")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(
            int(40 * ratio_w), int(40 * ratio_h), int(661 * ratio_w), int(837 * ratio_h)))
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
        self.tableWidget.setColumnCount(5)

        item = QtWidgets.QTableWidgetItem()
        item.setFont(QtGui.QFont("Gabriola", int(18 * ratio_font)))
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setFont(QtGui.QFont("Gabriola", int(18 * ratio_font)))
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setFont(QtGui.QFont("Gabriola", int(18 * ratio_font)))
        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        item.setFont(QtGui.QFont("Gabriola", int(18 * ratio_font)))
        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        item.setFont(QtGui.QFont("Gabriola", int(18 * ratio_font)))
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(int(120 * ratio_w))
        self.tableWidget.verticalHeader().setDefaultSectionSize(int(50 * ratio_h))

        # LCD
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(
            int(970 * ratio_w), int(205 * ratio_h), int(120 * ratio_w), int(120 * ratio_h)))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setStyleSheet("color:white")

        # Label
        self.Contacts_number_label = QtWidgets.QLabel(Form)
        self.Contacts_number_label.setGeometry(QtCore.QRect(
            int(720 * ratio_w), int(190 * ratio_h), int(320 * ratio_w), int(60 * ratio_h)))
        self.Contacts_number_label.setFont(QtGui.QFont("Gabriola", int(30 * ratio_font)))
        self.Contacts_number_label.setStyleSheet("color:white")
        self.Contacts_number_label.setText("Number of contacts :")

        # read contacts
        self.read_contacts()

        # Push buttons
        self.refresh_pushButton = QtWidgets.QPushButton(Form)
        self.refresh_pushButton.setGeometry(QtCore.QRect(
            int(705 * ratio_w), int(45 * ratio_h), int(32 * ratio_w), int(32 * ratio_h)))
        self.refresh_pushButton.setFlat(True)
        self.refresh_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/refresh.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.refresh_pushButton.setToolTip("Refresh contacts list")
        self.refresh_pushButton.clicked.connect(lambda: self.refresh_action(Form))

        # ComboBox
        self.change_sort_comboBox = QtWidgets.QComboBox(Form)
        self.change_sort_comboBox.setGeometry(QtCore.QRect(
            int(730 * ratio_w), int(407 * ratio_h), int(200 * ratio_w), int(40 * ratio_h)))
        self.change_sort_comboBox.setFont(QtGui.QFont("Gabriola", int(13 * ratio_font)))
        self.change_sort_comboBox.setStyleSheet(
            f"border :1px solid black;border-radius :{int(15 * (ratio_w + ratio_h) / 2)}px;")
        self.change_sort_comboBox.setFrame(False)
        self.change_sort_comboBox.setEditable(False)
        self.change_sort_comboBox.setCurrentIndex(0)
        # Add item
        self.change_sort_comboBox.addItem("")
        self.change_sort_comboBox.addItem("")
        self.change_sort_comboBox.addItem("")
        self.change_sort_comboBox.addItem("")
        self.change_sort_comboBox.addItem("")
        self.change_sort_comboBox.addItem("")
        self.change_sort_comboBox.addItem("")
        self.change_sort_comboBox.addItem("")
        self.change_sort_comboBox.addItem("")
        self.change_sort_comboBox.addItem("")
        # Change sort action
        with open("file/sort_contact_currentIndex.txt", "rt") as file:
            self.change_sort_comboBox.setCurrentIndex(int(file.read()))
        self.change_sort_action()
        self.change_sort_comboBox.activated.connect(self.change_sort_action)

        self.retranslateUi(Form)
        self.tableWidget.setSortingEnabled(True)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Show Contacts"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Number"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Email"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Address"))
        self.change_sort_comboBox.setItemText(0, _translate("Form", "   Name - Ascending"))
        self.change_sort_comboBox.setItemText(1, _translate("Form", "   Name - Descending"))
        self.change_sort_comboBox.setItemText(2, _translate("Form", "   Last name - Ascending"))
        self.change_sort_comboBox.setItemText(3, _translate("Form", "   Last name - Descending"))
        self.change_sort_comboBox.setItemText(4, _translate("Form", "   Number - Ascending"))
        self.change_sort_comboBox.setItemText(5, _translate("Form", "   Number - Descending"))
        self.change_sort_comboBox.setItemText(6, _translate("Form", "   Email - Ascending"))
        self.change_sort_comboBox.setItemText(7, _translate("Form", "   Email - Descending"))
        self.change_sort_comboBox.setItemText(8, _translate("Form", "   Address - Ascending"))
        self.change_sort_comboBox.setItemText(9, _translate("Form", "   Address - Descending"))

    def read_contacts(self):
        Row = 0
        self.tableWidget.setRowCount(Row)
        with open("file/Contacts.txt", "rt") as file:
            for i in file:
                line = i[0:-1].split("---")

                self.tableWidget.setRowCount(Row + 1)

                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(Row, 0, item)
                item.setText(line[0][1:-1])

                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(Row, 1, item)
                item.setText(line[1][1:-1])

                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(Row, 2, item)
                item.setText(line[2][1:-1])

                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(Row, 3, item)
                item.setText(line[3][1:-1])

                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(Row, 4, item)
                item.setText(line[4][1:-1])

                Row += 1

        self.lcdNumber.display(self.tableWidget.rowCount())

    def refresh_action(self, Form):
        global ratio_w
        global ratio_h

        sort_status = self.change_sort_comboBox.currentIndex()  # *
        Form.close()
        Form_ShowContacts = QtWidgets.QDialog()
        ui = Ui_Form_ShowContacts()
        ui.setupUi(Form_ShowContacts, ratio_w, ratio_h, ratio_font)
        ui.change_sort_comboBox.setCurrentIndex(sort_status)  # *
        ui.change_sort_action()  # *
        Form_ShowContacts.show()
        Form_ShowContacts.exec_()

    def change_sort_action(self):
        index = self.change_sort_comboBox.currentIndex()
        with open("file/sort_contact_currentIndex.txt", "wt") as file:
            file.write(str(index))
        if index == 0:
            self.tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)

        if index == 1:
            self.tableWidget.sortItems(0, QtCore.Qt.DescendingOrder)

        if index == 2:
            self.tableWidget.sortItems(1, QtCore.Qt.AscendingOrder)

        if index == 3:
            self.tableWidget.sortItems(1, QtCore.Qt.DescendingOrder)

        if index == 4:
            self.tableWidget.sortItems(2, QtCore.Qt.AscendingOrder)

        if index == 5:
            self.tableWidget.sortItems(2, QtCore.Qt.DescendingOrder)

        if index == 6:
            self.tableWidget.sortItems(3, QtCore.Qt.AscendingOrder)

        if index == 7:
            self.tableWidget.sortItems(3, QtCore.Qt.DescendingOrder)

        if index == 8:
            self.tableWidget.sortItems(4, QtCore.Qt.AscendingOrder)

        if index == 9:
            self.tableWidget.sortItems(4, QtCore.Qt.DescendingOrder)

    def tableWidget_action_calculate(self, row):
        self.name_selected = self.tableWidget.item(row, 0).text()
        self.last_name_selected = self.tableWidget.item(row, 1).text()
        self.number_selected = self.tableWidget.item(row, 2).text()
        self.email_selected = self.tableWidget.item(row, 3).text()
        self.address_selected = self.tableWidget.item(row, 4).text()

    def tableWidget_action_show(self, Form):
        global ratio_w
        global ratio_h

        self.single_contact_widget = QtWidgets.QWidget(Form)
        self.single_contact_widget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(1380 * ratio_w), int(917 * ratio_h)))

        self.widget = QtWidgets.QWidget(self.single_contact_widget)
        self.widget.setGeometry(QtCore.QRect(
            int(120 * ratio_w), int(128 * ratio_h), int(500 * ratio_w), int(660 * ratio_h)))
        self.widget.setStyleSheet("border-image : url('file/showSingleContact_background.png');")

        # Label
        self.no_net_label = QtWidgets.QLabel(self.single_contact_widget)
        self.no_net_label.setGeometry(QtCore.QRect(
            int(245 * ratio_w), int(220 * ratio_h), int(100 * ratio_w), int(15 * ratio_h)))
        self.no_net_label.setFont(QtGui.QFont("Gabriola", int(10 * ratio_font)))
        self.no_net_label.setStyleSheet("color:red")
        self.no_net_label.setText("No internet !")
        self.no_net_label.hide()

        self.top_label = QtWidgets.QLabel(self.single_contact_widget)
        self.top_label.setGeometry(QtCore.QRect(
            int(270 * ratio_w), int(250 * ratio_h), int(200 * ratio_w), int(30 * ratio_h)))
        self.top_label.setFont(QtGui.QFont("Gabriola", int(30 * ratio_font)))
        self.top_label.setText("Edit Contact")

        self.name_label = QtWidgets.QLabel(self.single_contact_widget)
        self.name_label.setGeometry(QtCore.QRect(
            int(210 * ratio_w), int(320 * ratio_h), int(80 * ratio_w), int(30 * ratio_h)))
        self.name_label.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.name_label.setText("Name :")

        self.last_name_label = QtWidgets.QLabel(self.single_contact_widget)
        self.last_name_label.setGeometry(QtCore.QRect(
            int(210 * ratio_w), int(390 * ratio_h), int(150 * ratio_w), int(30 * ratio_h)))
        self.last_name_label.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.last_name_label.setText("Last name :")

        self.number_label = QtWidgets.QLabel(self.single_contact_widget)
        self.number_label.setGeometry(QtCore.QRect(
            int(210 * ratio_w), int(460 * ratio_h), int(120 * ratio_w), int(30 * ratio_h)))
        self.number_label.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.number_label.setText("Number :")

        self.email_label = QtWidgets.QLabel(self.single_contact_widget)
        self.email_label.setGeometry(QtCore.QRect(
            int(210 * ratio_w), int(530 * ratio_h), int(100 * ratio_w), int(30 * ratio_h)))
        self.email_label.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.email_label.setText("Email :")

        self.address_label = QtWidgets.QLabel(self.single_contact_widget)
        self.address_label.setGeometry(QtCore.QRect(
            int(210 * ratio_w), int(600 * ratio_h), int(120 * ratio_w), int(30 * ratio_h)))
        self.address_label.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.address_label.setText("Address :")

        # three statuses of saving label
        self.invalid_label = QtWidgets.QLabel(self.single_contact_widget)
        self.invalid_label.setGeometry(QtCore.QRect(
            int(1150 * ratio_w), int(850 * ratio_h), int(220 * ratio_w), int(50 * ratio_h)))
        self.invalid_label.setFont(QtGui.QFont("Gabriola", int(25 * ratio_font)))
        self.invalid_label.setStyleSheet("color:white")
        self.invalid_label.setText("Invalid !")
        self.invalid_label.hide()

        self.exist_label = QtWidgets.QLabel(self.single_contact_widget)
        self.exist_label.setGeometry(QtCore.QRect(
            int(1100 * ratio_w), int(850 * ratio_h), int(220 * ratio_w), int(50 * ratio_h)))
        self.exist_label.setFont(QtGui.QFont("Gabriola", int(25 * ratio_font)))
        self.exist_label.setStyleSheet("color:white")
        self.exist_label.setText("Already exist !")
        self.exist_label.hide()

        self.not_changed_label = QtWidgets.QLabel(self.single_contact_widget)
        self.not_changed_label.setGeometry(QtCore.QRect(
            int(1100 * ratio_w), int(850 * ratio_h), int(250 * ratio_w), int(50 * ratio_h)))
        self.not_changed_label.setFont(QtGui.QFont("Gabriola", int(25 * ratio_font)))
        self.not_changed_label.setStyleSheet("color:white")
        self.not_changed_label.setText("No change found !")
        self.not_changed_label.hide()

        # Copied to clipboard label
        self.copy_to_clipboard_label = QtWidgets.QLabel(self.single_contact_widget)
        self.copy_to_clipboard_label.setGeometry(QtCore.QRect(
            int(1050 * ratio_w), int(850 * ratio_h), int(280 * ratio_w), int(50 * ratio_h)))
        self.copy_to_clipboard_label.setFont(QtGui.QFont("Gabriola", int(25 * ratio_font)))
        self.copy_to_clipboard_label.setStyleSheet("color:white")
        self.copy_to_clipboard_label.setText("Copied to clipboard !")
        self.copy_to_clipboard_label.hide()

        # Added to favorite label
        self.added_to_favorite_label = QtWidgets.QLabel(self.single_contact_widget)
        self.added_to_favorite_label.setGeometry(QtCore.QRect(
            int(1000 * ratio_w), int(850 * ratio_h), int(360 * ratio_w), int(50 * ratio_h)))
        self.added_to_favorite_label.setFont(QtGui.QFont("Gabriola", int(25 * ratio_font)))
        self.added_to_favorite_label.setStyleSheet("color:white")
        self.added_to_favorite_label.setText("Added to favorite contacts !")
        self.added_to_favorite_label.hide()

        # Line Edit
        self.name_lineEdit = QtWidgets.QLineEdit(self.single_contact_widget)
        self.name_lineEdit.setGeometry(QtCore.QRect(
            int(340 * ratio_w), int(325 * ratio_h), int(200 * ratio_w), int(25 * ratio_h)))
        self.name_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.name_lineEdit.setFrame(False)
        self.name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.name_lineEdit.setText(self.name_selected)
        self.name_lineEdit.setPlaceholderText("Enter name here")
        self.name_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)
        self.name_lineEdit.setReadOnly(True)

        self.last_name_lineEdit = QtWidgets.QLineEdit(self.single_contact_widget)
        self.last_name_lineEdit.setGeometry(QtCore.QRect(
            int(340 * ratio_w), int(395 * ratio_h), int(200 * ratio_w), int(25 * ratio_h)))
        self.last_name_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.last_name_lineEdit.setFrame(False)
        self.last_name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.last_name_lineEdit.setText(self.last_name_selected)
        self.last_name_lineEdit.setPlaceholderText("Enter last name here")
        self.last_name_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)
        self.last_name_lineEdit.setReadOnly(True)

        self.number_lineEdit = QtWidgets.QLineEdit(self.single_contact_widget)
        self.number_lineEdit.setGeometry(QtCore.QRect(
            int(340 * ratio_w), int(465 * ratio_h), int(200 * ratio_w), int(25 * ratio_h)))
        self.number_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.number_lineEdit.setFrame(False)
        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.number_lineEdit.setText(self.number_selected)
        self.number_lineEdit.setPlaceholderText("Enter number here")
        rx_number_lineEdit = QtCore.QRegExp("[0-9 | + | -]*")
        val_number_lineEdit = QtGui.QRegExpValidator(rx_number_lineEdit)
        self.number_lineEdit.setValidator(val_number_lineEdit)
        self.number_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)
        self.number_lineEdit.setReadOnly(True)

        self.email_lineEdit = QtWidgets.QLineEdit(self.single_contact_widget)
        self.email_lineEdit.setGeometry(QtCore.QRect(
            int(340 * ratio_w), int(535 * ratio_h), int(200 * ratio_w), int(25 * ratio_h)))
        self.email_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.email_lineEdit.setFrame(False)
        self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.email_lineEdit.setText(self.email_selected)
        self.email_lineEdit.setPlaceholderText("Enter email here")
        self.email_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)
        rx_email_lineEdit = QtCore.QRegExp("[a-z | A-Z | 0-9 | @ | \.]*")
        val_email_lineEdit = QtGui.QRegExpValidator(rx_email_lineEdit)
        self.email_lineEdit.setValidator(val_email_lineEdit)
        self.email_lineEdit.setReadOnly(True)

        self.address_lineEdit = QtWidgets.QLineEdit(self.single_contact_widget)
        self.address_lineEdit.setGeometry(QtCore.QRect(
            int(340 * ratio_w), int(605 * ratio_h), int(200 * ratio_w), int(25 * ratio_h)))
        self.address_lineEdit.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.address_lineEdit.setFrame(False)
        self.address_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.address_lineEdit.setText(self.address_selected)
        self.address_lineEdit.setPlaceholderText("Enter address here (Optional)")
        self.address_lineEdit.setAlignment(QtCore.Qt.AlignHCenter)
        self.address_lineEdit.setReadOnly(True)

        # Push button
        self.close_pushButton = QtWidgets.QPushButton(self.single_contact_widget)
        self.close_pushButton.setGeometry(QtCore.QRect(
            int(520 * ratio_w), int(170 * ratio_h), int(32 * ratio_w), int(32 * ratio_h)))
        self.close_pushButton.setFlat(True)
        self.close_pushButton.setStyleSheet("border-image : url('file/SingleContact_close.png');")
        self.close_pushButton.clicked.connect(self.single_contact_widget.hide)

        self.edit_pushButton = QtWidgets.QPushButton(self.single_contact_widget)
        self.edit_pushButton.setGeometry(QtCore.QRect(
            int(475 * ratio_w), int(253 * ratio_h), int(34 * ratio_w), int(33 * ratio_h)))
        self.edit_pushButton.setFlat(True)
        self.edit_pushButton.setStyleSheet("border-image : url('file/SingleContact_edit.png');")
        self.edit_pushButton.clicked.connect(self.edit_action)

        self.sound_pushButton = QtWidgets.QPushButton(self.single_contact_widget)
        self.sound_pushButton.setGeometry(QtCore.QRect(
            int(200 * ratio_w), int(200 * ratio_h), int(34 * ratio_w), int(36 * ratio_h)))
        self.sound_pushButton.setFlat(True)
        self.sound_pushButton.setStyleSheet("border-image : url('file/SingleContact_sound.png');")
        self.sound_pushButton.clicked.connect(self.sound_action)

        self.clear_pushButton = QtWidgets.QPushButton(self.single_contact_widget)
        self.clear_pushButton.setGeometry(QtCore.QRect(
            int(200 * ratio_w), int(660 * ratio_h), int(90 * ratio_w), int(30 * ratio_h)))
        self.clear_pushButton.setFlat(True)
        self.clear_pushButton.setStyleSheet(
            f"border :1px solid black;border-radius :{int(15 * (ratio_w + ratio_h) / 2)}px;" + "color:#550000;")
        self.clear_pushButton.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.clear_pushButton.setText("Clear")
        self.clear_pushButton.clicked.connect(self.clear_action)

        self.copy_to_clipboard_pushButton = QtWidgets.QPushButton(self.single_contact_widget)
        self.copy_to_clipboard_pushButton.setGeometry(QtCore.QRect(
            int(175 * ratio_w), int(700 * ratio_h), int(200 * ratio_w), int(35 * ratio_h)))
        self.copy_to_clipboard_pushButton.setFlat(True)
        self.copy_to_clipboard_pushButton.setStyleSheet(
            f"border :1px solid black;border-radius :{int(15 * (ratio_w + ratio_h) / 2)}px;" + "color:#550000;")
        self.copy_to_clipboard_pushButton.setFont(QtGui.QFont("Gabriola", int(18 * ratio_font)))
        self.copy_to_clipboard_pushButton.setText("Copy to clipboard")
        self.copy_to_clipboard_pushButton.clicked.connect(self.copy_to_clipboard_action)

        self.delete_pushButton = QtWidgets.QPushButton(self.single_contact_widget)
        self.delete_pushButton.setGeometry(QtCore.QRect(
            int(315 * ratio_w), int(660 * ratio_h), int(90 * ratio_w), int(30 * ratio_h)))
        self.delete_pushButton.setFlat(True)
        self.delete_pushButton.setStyleSheet(
            f"border :1px solid black;border-radius :{int(15 * (ratio_w + ratio_h) / 2)}px;" + "color:#550000;")
        self.delete_pushButton.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.delete_pushButton.setText("Delete")
        self.delete_pushButton.clicked.connect(lambda: self.delete_action(self.single_contact_widget, Form))

        self.save_pushButton = QtWidgets.QPushButton(self.single_contact_widget)
        self.save_pushButton.setGeometry(QtCore.QRect(
            int(430 * ratio_w), int(660 * ratio_h), int(90 * ratio_w), int(30 * ratio_h)))
        self.save_pushButton.setFlat(True)
        self.save_pushButton.setStyleSheet(
            f"border :1px solid black;border-radius :{int(15 * (ratio_w + ratio_h) / 2)}px;" + "color:#550000;")
        self.save_pushButton.setFont(QtGui.QFont("Gabriola", int(20 * ratio_font)))
        self.save_pushButton.setText("Save")
        self.save_pushButton.clicked.connect(lambda: self.save_action(self.single_contact_widget, Form))

        self.add_to_favorite_pushButton = QtWidgets.QPushButton(self.single_contact_widget)
        self.add_to_favorite_pushButton.setGeometry(QtCore.QRect(
            int(390 * ratio_w), int(700 * ratio_h), int(160 * ratio_w), int(35 * ratio_h)))
        self.add_to_favorite_pushButton.setFlat(True)
        self.add_to_favorite_pushButton.setStyleSheet(
            f"border :1px solid black;border-radius :{int(15 * (ratio_w + ratio_h) / 2)}px;" + "color:#550000;")
        self.add_to_favorite_pushButton.setFont(QtGui.QFont("Gabriola", int(18 * ratio_font)))
        self.add_to_favorite_pushButton.setText("Add to favorite")
        self.add_to_favorite_pushButton.clicked.connect(
            lambda: self.add_to_favorite_action(self.single_contact_widget))

        self.single_contact_widget.show()

    def clear_action(self):
        self.name_lineEdit.setText("")
        self.last_name_lineEdit.setText("")
        self.number_lineEdit.setText("")
        self.email_lineEdit.setText("")
        self.address_lineEdit.setText("")

        self.invalid_label.hide()
        self.exist_label.hide()
        self.copy_to_clipboard_label.hide()
        self.added_to_favorite_label.hide()
        self.not_changed_label.hide()
        self.no_net_label.hide()

        self.name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.last_name_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
        self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")

    def copy_to_clipboard_action(self):
        name = self.name_lineEdit.text()
        last_name = self.last_name_lineEdit.text()
        number = self.number_lineEdit.text()
        email = self.email_lineEdit.text()
        address = self.address_lineEdit.text()

        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(f"-> Name : {name} | Last name : {last_name} | Number : {number} | Email : {email} | "
                          f"Address : {address} <-")

        self.invalid_label.hide()
        self.exist_label.hide()
        self.added_to_favorite_label.hide()
        self.not_changed_label.hide()
        self.no_net_label.hide()
        self.copy_to_clipboard_label.show()

    def delete_action(self, single_contact_widget, Form):
        selected_line = f"'{self.name_selected}'---'{self.last_name_selected}'---'{self.number_selected}'---" \
                        f"'{self.email_selected}'---'{self.address_selected}'"

        with open("file/Contacts.txt", "rt") as file:
            lines = file.readlines()
        with open("file/Contacts.txt", "wt") as file:
            for line in lines:
                if line.strip("\n") != selected_line:
                    file.write(line)

        MessageBox = QtWidgets.QMessageBox()
        MessageBox.information(
            single_contact_widget, 'Result', 'Contact successfully deleted.', MessageBox.Ok)
        self.refresh_action(Form)
        self.single_contact_widget.hide()

    def save_action(self, single_contact_widget, Form):
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
                    if f"'{number}'" == line[2] and number != self.number_selected:
                        self.number_lineEdit.setStyleSheet("background-color:#ffa0a0;")
                        status = 2
                        break
                    elif f"'{email}'" == line[3] and email != self.email_selected:
                        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                        self.email_lineEdit.setStyleSheet("background-color:#ffa0a0;")
                        status = 2
                        break
                    else:
                        self.number_lineEdit.setStyleSheet("background-color:#e10e10e10;")
                        self.email_lineEdit.setStyleSheet("background-color:#e10e10e10;")

        # check for changed or not
        if status == 0:
            if name == self.name_selected:
                if last_name == self.last_name_selected:
                    if number == self.number_selected:
                        if email == self.email_selected:
                            if address == self.address_selected:
                                status = 3

        #################################################

        if status == 0:
            selected_line = f"'{self.name_selected}'---'{self.last_name_selected}'---'{self.number_selected}'---" \
                            f"'{self.email_selected}'---'{self.address_selected}'"

            with open("file/Contacts.txt", "rt") as file:
                lines = file.readlines()
            with open("file/Contacts.txt", "wt") as file:
                for line in lines:
                    if line.strip("\n") != selected_line:
                        file.write(line)

                    else:
                        file.write(f"'{name}'---'{last_name}'---'{number}'---'{email}'---'{address}'\n")

            MessageBox = QtWidgets.QMessageBox()
            MessageBox.information(
                single_contact_widget, 'Result', 'Contact changes saved.', MessageBox.Ok)
            self.refresh_action(Form)
            self.single_contact_widget.hide()

        elif status == 1:
            self.exist_label.hide()
            self.copy_to_clipboard_label.hide()
            self.added_to_favorite_label.hide()
            self.not_changed_label.hide()
            self.no_net_label.hide()
            self.invalid_label.show()

        elif status == 2:
            self.invalid_label.hide()
            self.copy_to_clipboard_label.hide()
            self.added_to_favorite_label.hide()
            self.not_changed_label.hide()
            self.no_net_label.hide()
            self.exist_label.show()

        elif status == 3:
            self.invalid_label.hide()
            self.copy_to_clipboard_label.hide()
            self.added_to_favorite_label.hide()
            self.exist_label.hide()
            self.no_net_label.hide()
            self.not_changed_label.show()

    def add_to_favorite_action(self, single_contact_widget):
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
            with open("file/FavoriteContacts.txt", "rt") as file:
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
            with open("file/FavoriteContacts.txt", "at") as file:
                file.write(f"'{name}'---'{last_name}'---'{number}'---'{email}'---'{address}'\n")

            self.invalid_label.hide()
            self.exist_label.hide()
            self.copy_to_clipboard_label.hide()
            self.not_changed_label.hide()
            self.no_net_label.hide()
            self.added_to_favorite_label.show()

        elif status == 1:
            self.exist_label.hide()
            self.copy_to_clipboard_label.hide()
            self.added_to_favorite_label.hide()
            self.not_changed_label.hide()
            self.no_net_label.hide()
            self.invalid_label.show()

        elif status == 2:
            self.invalid_label.hide()
            self.copy_to_clipboard_label.hide()
            self.added_to_favorite_label.hide()
            self.not_changed_label.hide()
            self.no_net_label.hide()
            self.exist_label.show()

    def edit_action(self):
        self.name_lineEdit.setReadOnly(False)
        self.last_name_lineEdit.setReadOnly(False)
        self.number_lineEdit.setReadOnly(False)
        self.email_lineEdit.setReadOnly(False)
        self.address_lineEdit.setReadOnly(False)

    def sound_action(self):
        text = f"""
        hi.
        Your contact's fullname is {self.name_lineEdit.text()} {self.last_name_lineEdit.text()}.
        and the number is {self.number_lineEdit.text()}.
        you can send the email by {self.email_lineEdit.text()}.
        and lives in {self.address_lineEdit.text()}.
        Have a good time.
        """
        try:
            self.no_net_label.hide()
            sound = gTTS(text)
            sound.save("sound.mp3")
            playsound("sound.mp3")
            os.remove("sound.mp3")

        except:
            self.no_net_label.show()


ratio_w = 1
ratio_h = 1
ratio_font = 1
