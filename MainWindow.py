from PyQt5 import QtCore, QtGui, QtWidgets
from os import path, getcwd, remove
import getpass
from playsound import playsound
from Calendar import Ui_Form_Calendar
from AddContact import Ui_Form_addContact
from AdvancedShutdown import Ui_Form_advancedShutdown
from ShowContacts import Ui_Form_ShowContacts
from ShowFavoriteContacts import Ui_Form_ShowFavoriteContacts
from SearchContacts import Ui_Form_SearchContacts
from AboutUs import Ui_Form_aboutUs



# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


class Ui_Form_MainWindow(object):
    def setupUi(self, Form, w, h, f):
        global ratio_w
        global ratio_h
        global ratio_font
        ratio_w = w
        ratio_h = h
        ratio_font = f

        Form.setFixedSize(int(1133 * ratio_w), int(850 * ratio_h))
        Form.setWindowTitle("Contacts")

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(1133 * ratio_w), int(850 * ratio_h)))
        self.widget.setStyleSheet("border-image : url('file/background0.jpg');")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file/appIcon.png"))
        Form.setWindowIcon(icon)

        # PushButtons
        self.addContact_pushButton = QtWidgets.QPushButton(Form)
        self.addContact_pushButton.setGeometry(QtCore.QRect(
            int(20 * ratio_w), int(30 * ratio_h), int(128 * ratio_w), int(128 * ratio_h)))
        self.addContact_pushButton.setFlat(True)
        self.addContact_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/addContact.ico')}
            QToolTip {background-color: white;color: black};
            """)
        self.addContact_pushButton.setToolTip("Add a contact")
        self.addContact_pushButton.clicked.connect(self.addContact_action)

        self.showContact_pushButton = QtWidgets.QPushButton(Form)
        self.showContact_pushButton.setGeometry(QtCore.QRect(
            int(20 * ratio_w), int(178 * ratio_h), int(128 * ratio_w), int(128 * ratio_h)))
        self.showContact_pushButton.setFlat(True)
        self.showContact_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/showContact.ico')}
            QToolTip {background-color: white;color: black};
            """)
        self.showContact_pushButton.setToolTip("Show contacts")
        self.showContact_pushButton.clicked.connect(self.showContact_action)

        self.showFavoriteContact_pushButton = QtWidgets.QPushButton(Form)
        self.showFavoriteContact_pushButton.setGeometry(QtCore.QRect(
            int(168 * ratio_w), int(178 * ratio_h), int(128 * ratio_w), int(128 * ratio_h)))
        self.showFavoriteContact_pushButton.setFlat(True)
        self.showFavoriteContact_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/showFavoriteContact.ico')}
            QToolTip {background-color: white;color: black};
            """)
        self.showFavoriteContact_pushButton.setToolTip("Show favorite contacts")
        self.showFavoriteContact_pushButton.clicked.connect(self.showFavoriteContact_action)

        self.searchContact_pushButton = QtWidgets.QPushButton(Form)
        self.searchContact_pushButton.setGeometry(QtCore.QRect(
            int(200 * ratio_w), int(62 * ratio_h), int(66 * ratio_w), int(66 * ratio_h)))
        self.searchContact_pushButton.setFlat(True)
        self.searchContact_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/searchContact.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.searchContact_pushButton.setToolTip("Search from contacts")
        self.searchContact_pushButton.clicked.connect(self.SearchContacts_action)

        self.restore_pushButton = QtWidgets.QPushButton(Form)
        self.restore_pushButton.setGeometry(QtCore.QRect(
            int(52 * ratio_w), int(338 * ratio_h), int(64 * ratio_w), int(64 * ratio_h)))
        self.restore_pushButton.setFlat(True)
        self.restore_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/restore.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.restore_pushButton.setToolTip("Restore contacts")
        self.restore_pushButton.clicked.connect(self.restore_action)

        self.backup_pushButton = QtWidgets.QPushButton(Form)
        self.backup_pushButton.setGeometry(QtCore.QRect(
            int(204 * ratio_w), int(341 * ratio_h), int(60 * ratio_w), int(60 * ratio_h)))
        self.backup_pushButton.setFlat(True)
        self.backup_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/backup.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.backup_pushButton.setToolTip("Backup contacts")
        self.backup_pushButton.clicked.connect(self.backup_action)

        self.clearData_pushButton = QtWidgets.QPushButton(Form)
        self.clearData_pushButton.setGeometry(QtCore.QRect(
            int(200 * ratio_w), int(464 * ratio_h), int(66 * ratio_w), int(66 * ratio_h)))
        self.clearData_pushButton.setFlat(True)
        self.clearData_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/clearData.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.clearData_pushButton.setToolTip("Clear data")
        self.clearData_pushButton.clicked.connect(lambda: self.clearData_action(Form))

        self.advancedShutdown_pushButton = QtWidgets.QPushButton(Form)
        self.advancedShutdown_pushButton.setGeometry(QtCore.QRect(
            int(52 * ratio_w), int(464 * ratio_h), int(64 * ratio_w), int(64 * ratio_h)))
        self.advancedShutdown_pushButton.setFlat(True)
        self.advancedShutdown_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/advancedShutdown.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.advancedShutdown_pushButton.setToolTip("Advanced windows shutdown")
        self.advancedShutdown_pushButton.clicked.connect(self.advancedShutdown_action)

        self.aboutUs_pushButton = QtWidgets.QPushButton(Form)
        self.aboutUs_pushButton.setGeometry(QtCore.QRect(
            int(200 * ratio_w), int(594 * ratio_h), int(66 * ratio_w), int(66 * ratio_h)))
        self.aboutUs_pushButton.setFlat(True)
        self.aboutUs_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/aboutUs.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.aboutUs_pushButton.setToolTip("About us")
        self.aboutUs_pushButton.clicked.connect(self.aboutUs_action)

        self.wizard_pushButton = QtWidgets.QPushButton(Form)
        self.wizard_pushButton.setGeometry(QtCore.QRect(
            int(52 * ratio_w), int(594 * ratio_h), int(66 * ratio_w), int(66 * ratio_h)))
        self.wizard_pushButton.setFlat(True)
        self.wizard_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/wizard.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.wizard_pushButton.setToolTip("Guide book")
        self.wizard_pushButton.clicked.connect(self.wizard_action)

        self.exit_pushButton = QtWidgets.QPushButton(Form)
        self.exit_pushButton.setGeometry(QtCore.QRect(
            int(56 * ratio_w), int(724 * ratio_h), int(66 * ratio_w), int(66 * ratio_h)))
        self.exit_pushButton.setFlat(True)
        self.exit_pushButton.setStyleSheet(
            """
            QPushButton {border-image: url('file/exit.png')}
            QToolTip {background-color: white;color: black};
            """)
        self.exit_pushButton.setToolTip("Exit")
        self.exit_pushButton.clicked.connect(self.exit_action)

        self.calendar_pushButton = QtWidgets.QPushButton(Form)
        self.calendar_pushButton.setGeometry(QtCore.QRect(
            int(890 * ratio_w), int(10 * ratio_h), int(235 * ratio_w), int(40 * ratio_h)))
        self.calendar_pushButton.setText(QtCore.QDate.currentDate().toString("dddd  |  dd  MMMM  yyyy"))
        self.calendar_pushButton.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))
        self.calendar_pushButton.setStyleSheet(
            """
            QPushButton {color:#00aaff}
            QToolTip {background-color: white;color: black};
            """)
        self.calendar_pushButton.setFlat(True)
        self.calendar_pushButton.setToolTip("Open calendar")
        self.calendar_pushButton.clicked.connect(self.calendar_action)

        self.change_background_pushButton = QtWidgets.QPushButton(Form)
        self.change_background_pushButton.setGeometry(QtCore.QRect(
            int(970 * ratio_w), int(800 * ratio_h), int(150 * ratio_w), int(40 * ratio_h)))
        self.change_background_pushButton.setText("Next background")
        self.change_background_pushButton.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))
        self.change_background_pushButton.setStyleSheet(
            """
            QPushButton {color:#00aaff}
            QToolTip {background-color: white;color: black};
            """)
        self.change_background_pushButton.setFlat(True)
        self.change_background_pushButton.setToolTip("Show next background")
        self.num = 1
        self.change_background_pushButton.clicked.connect(self.change_background_action)

        # Check Box
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(
            int(950 * ratio_w), int(60 * ratio_h), int(150 * ratio_w), int(20 * ratio_h)))
        self.checkBox.setText('Run on startup')
        self.checkBox.setFont(QtGui.QFont("Gabriola", int(15 * ratio_font)))
        self.checkBox.setStyleSheet("color:white;")

        if path.exists(f"C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start "
                       f"Menu/Programs/Startup/app_startup.bat"):
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

        self.checkBox.toggled.connect(self.checkBox_action)

        ##################

        # ساخت لیبل خروج
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(1133 * ratio_w), int(850 * ratio_h)))
        self.label1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.gif = QtGui.QMovie("file/exit.gif")
        self.gif.setScaledSize(QtCore.QSize(
            int(500 * ratio_w), int(212 * ratio_h)))
        self.label1.setMovie(self.gif)
        self.label1.hide()

        self.confirmExit_pushButton = QtWidgets.QPushButton(self.label1)
        self.confirmExit_pushButton.setGeometry(QtCore.QRect(
            int(350 * ratio_w), int(560 * ratio_h), int(310 * ratio_w), int(50 * ratio_h)))
        self.confirmExit_pushButton.setStyleSheet("color: white;")
        self.confirmExit_pushButton.setFont(QtGui.QFont("MV Boli", int(16 * ratio_font)))
        self.confirmExit_pushButton.setText("Are you sure to exit ?")
        self.confirmExit_pushButton.setFlat(True)

        self.confirmExit_Yes_pushButton = QtWidgets.QPushButton(self.label1)
        self.confirmExit_Yes_pushButton.setGeometry(QtCore.QRect(
            int(670 * ratio_w), int(540 * ratio_h), int(100 * ratio_w), int(50 * ratio_h)))
        self.confirmExit_Yes_pushButton.setStyleSheet("color: red;")
        self.confirmExit_Yes_pushButton.setFont(QtGui.QFont("MV Boli", int(15 * ratio_font)))
        self.confirmExit_Yes_pushButton.setText("Yes :(")
        self.confirmExit_Yes_pushButton.setFlat(True)
        self.confirmExit_Yes_pushButton.clicked.connect(lambda: playsound("./file/exit.mp3"))
        self.confirmExit_Yes_pushButton.clicked.connect(Form.close)

        self.confirmExit_No_pushButton = QtWidgets.QPushButton(self.label1)
        self.confirmExit_No_pushButton.setGeometry(QtCore.QRect(
            int(670 * ratio_w), int(590 * ratio_h), int(100 * ratio_w), int(50 * ratio_h)))
        self.confirmExit_No_pushButton.setStyleSheet("color: green;")
        self.confirmExit_No_pushButton.setFont(QtGui.QFont("MV Boli", int(15 * ratio_font)))
        self.confirmExit_No_pushButton.setText("No :)")
        self.confirmExit_No_pushButton.setFlat(True)
        self.confirmExit_No_pushButton.clicked.connect(self.label1.hide)
        #####################################

        # Menu
        mainM = QtWidgets.QMenuBar(Form)
        mainM.setGeometry(QtCore.QRect(
            int(376 * ratio_w), int(10 * ratio_h), int(380 * ratio_w), int(28 * ratio_h)))
        mainM.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        ###
        contactsM = mainM.addMenu('Contacts')

        addContactZM = QtWidgets.QAction('Add contact', Form)
        addContactZM.triggered.connect(self.addContact_action)
        addContactZM.setShortcut("Ctrl+N")
        contactsM.addAction(addContactZM)

        contactListZM = QtWidgets.QAction('Contact list', Form)
        contactListZM.triggered.connect(self.showContact_action)
        contactListZM.setShortcut("Ctrl+C")
        contactsM.addAction(contactListZM)

        favoriteContactListZM = QtWidgets.QAction('Favorite Contact list', Form)
        favoriteContactListZM.triggered.connect(self.showFavoriteContact_action)
        favoriteContactListZM.setShortcut("Ctrl+F")
        contactsM.addAction(favoriteContactListZM)

        searchContactsZM = QtWidgets.QAction('Search from contacts', Form)
        searchContactsZM.triggered.connect(self.SearchContacts_action)
        searchContactsZM.setShortcut("Ctrl+S")
        contactsM.addAction(searchContactsZM)

        ###
        advancedM = mainM.addMenu('Advanced')

        advancedShutdownZM = QtWidgets.QAction('Advanced shutdown', Form)
        advancedShutdownZM.triggered.connect(self.advancedShutdown_action)
        advancedShutdownZM.setShortcut("Shift+S")
        advancedM.addAction(advancedShutdownZM)

        clearDataZM = QtWidgets.QAction('Clear data', Form)
        clearDataZM.triggered.connect(lambda: self.clearData_action(Form))
        clearDataZM.setShortcut("Ctrl+D")
        advancedM.addAction(clearDataZM)

        ###
        backupRestoreM = mainM.addMenu('Backup and Restore')

        backupZM = QtWidgets.QAction('Backup', Form)
        backupZM.triggered.connect(self.backup_action)
        backupZM.setShortcut("Ctrl+B")
        backupRestoreM.addAction(backupZM)

        restoreZM = QtWidgets.QAction('Restore', Form)
        restoreZM.triggered.connect(self.restore_action)
        restoreZM.setShortcut("Ctrl+R")
        backupRestoreM.addAction(restoreZM)

        ###
        helpM = mainM.addMenu('Help')

        helpZM = QtWidgets.QAction('Help', Form)
        helpZM.triggered.connect(self.wizard_action)
        helpZM.setShortcut("Ctrl+H")
        helpM.addAction(helpZM)

        aboutUsZM = QtWidgets.QAction('About us', Form)
        aboutUsZM.triggered.connect(self.aboutUs_action)
        aboutUsZM.setShortcut("Ctrl+A")
        helpM.addAction(aboutUsZM)

        exitZM = QtWidgets.QAction('Exit', Form)
        exitZM.triggered.connect(self.exit_action)
        exitZM.setShortcut("Ctrl+E")
        helpM.addAction(exitZM)

        # Wizard page
        self.wizard = QtWidgets.QWizard(Form)
        self.wizard.setGeometry(QtCore.QRect(
            int(710 * ratio_w), int(400 * ratio_h), int(500 * ratio_w), int(280 * ratio_h)))

        self.wizard_sound_pushButton = QtWidgets.QPushButton(self.wizard)
        self.wizard_sound_pushButton.setGeometry(QtCore.QRect(
            int(20 * ratio_w), int(240 * ratio_h), int(140 * ratio_w), int(30 * ratio_h)))
        self.wizard_sound_pushButton.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.wizard_sound_pushButton.setText("Play voice instead")
        self.wizard_sound_pushButton.clicked.connect(self.wizard_sound_action)

        self.wizard_page1 = QtWidgets.QWizardPage()
        self.wizard_page1.setTitle("Add a new contact")
        self.wizard_page1.setSubTitle("""you can add your new contact or create a random contact.""")
        self.wizard.setPage(1, self.wizard_page1)

        self.wizard_page2 = QtWidgets.QWizardPage()
        self.wizard_page2.setTitle("Search contacts")
        self.wizard_page2.setSubTitle("""you can search your contacts.
use # for numbers and @ for Name & Lastname.""")
        self.wizard.setPage(2, self.wizard_page2)

        self.wizard_page3 = QtWidgets.QWizardPage()
        self.wizard_page3.setTitle("Contacts list")
        self.wizard_page3.setSubTitle(
            """you can see, edit, delete, your contacts or add them to favorite or copy them to clipboard.""")
        self.wizard.setPage(3, self.wizard_page3)

        self.wizard_page4 = QtWidgets.QWizardPage()
        self.wizard_page4.setTitle("Favorite contacts list")
        self.wizard_page4.setSubTitle(
            """you can see, edit, delete from favorite contacts or copy them to clipboard.""")
        self.wizard.setPage(4, self.wizard_page4)

        self.wizard_page5 = QtWidgets.QWizardPage()
        self.wizard_page5.setTitle("Backup contacts")
        self.wizard_page5.setSubTitle(
            """you can backup your contacts if you want to use them in future.""")
        self.wizard.setPage(5, self.wizard_page5)

        self.wizard_page6 = QtWidgets.QWizardPage()
        self.wizard_page6.setTitle("Restore contacts")
        self.wizard_page6.setSubTitle(
            """you can restore your contacts if you want to use past data.""")
        self.wizard.setPage(6, self.wizard_page6)

        self.wizard_page6 = QtWidgets.QWizardPage()
        self.wizard_page6.setTitle("Restore contacts")
        self.wizard_page6.setSubTitle(
            """you can restore your contacts if you want to use past data.""")
        self.wizard.setPage(6, self.wizard_page6)

        self.wizard_page7 = QtWidgets.QWizardPage()
        self.wizard_page7.setTitle("Advanced shutdown")
        self.wizard_page7.setSubTitle(
            """you can shutdown, restart, hibernate or log out your system with advanced options.""")
        self.wizard.setPage(7, self.wizard_page7)

        self.wizard_page8 = QtWidgets.QWizardPage()
        self.wizard_page8.setTitle("Clear data")
        self.wizard_page8.setSubTitle(
            """you can clear all your contacts and your favorite contacts quickly.""")
        self.wizard.setPage(8, self.wizard_page8)

        playsound("./file/startup.mp3")

    def calendar_action(self):
        global ratio_w
        global ratio_h

        Form_Calendar = QtWidgets.QDialog()
        ui = Ui_Form_Calendar()
        ui.setupUi(Form_Calendar, ratio_h, ratio_w, ratio_font)
        Form_Calendar.show()
        Form_Calendar.exec_()

    def exit_action(self):
        self.label1.show()
        self.gif.start()

    def addContact_action(self):
        global ratio_w
        global ratio_h

        Form_addContact = QtWidgets.QDialog()
        ui = Ui_Form_addContact()
        ui.setupUi(Form_addContact, ratio_w, ratio_h, ratio_font)
        Form_addContact.show()
        Form_addContact.exec_()

    def clearData_action(self, Form):
        MessageBox = QtWidgets.QMessageBox()
        MessageBox_answer = MessageBox.critical(
            Form, 'Clear data', 'You will lose all your contacts.\nAre you sure?', MessageBox.Yes | MessageBox.No)

        if MessageBox_answer == MessageBox.Yes:
            with open("file/FavoriteContacts.txt", "rt") as favorite_contacts_file, open("file/Contacts.txt",
                                                                                         "rt") as contacts_file:
                if len(contacts_file.read()) == 0 and len(favorite_contacts_file.read()) == 0:
                    empty = True
                else:
                    empty = False

            if empty:
                MessageBox.information(
                    Form, 'Result', 'Your contacts and favorite contacts is empty !', MessageBox.Ok)
            else:
                contacts_file = open("file/Contacts.txt", "wt")
                contacts_file.close()
                favorite_contacts_file = open("file/FavoriteContacts.txt", "wt")
                favorite_contacts_file.close()

                MessageBox.information(
                    Form, 'Result', 'All your contacts have been deleted.', MessageBox.Ok)

    def advancedShutdown_action(self):
        global ratio_w
        global ratio_h

        Form_advancedShutdown = QtWidgets.QDialog()
        ui = Ui_Form_advancedShutdown()
        ui.setupUi(Form_advancedShutdown, ratio_w, ratio_h, ratio_font)
        Form_advancedShutdown.show()
        Form_advancedShutdown.exec_()

    def showContact_action(self):
        global ratio_w
        global ratio_h

        Form_ShowContacts = QtWidgets.QDialog()
        ui = Ui_Form_ShowContacts()
        ui.setupUi(Form_ShowContacts, ratio_w, ratio_h, ratio_font)
        Form_ShowContacts.show()
        Form_ShowContacts.exec_()

    def showFavoriteContact_action(self):
        global ratio_w
        global ratio_h

        Form_ShowFavoriteContacts = QtWidgets.QDialog()
        ui = Ui_Form_ShowFavoriteContacts()
        ui.setupUi(Form_ShowFavoriteContacts, ratio_w, ratio_h, ratio_font)
        Form_ShowFavoriteContacts.show()
        Form_ShowFavoriteContacts.exec_()

    def SearchContacts_action(self):
        global ratio_w
        global ratio_h

        Form_SearchContacts = QtWidgets.QDialog()
        ui = Ui_Form_SearchContacts()
        ui.setupUi(Form_SearchContacts, ratio_w, ratio_h, ratio_font)
        Form_SearchContacts.show()
        Form_SearchContacts.exec_()

    def checkBox_action(self):
        if self.checkBox.isChecked():
            a = open(
                f"C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start "
                f"Menu/Programs/Startup/app_startup.bat",
                "w")
            a.write(f"""{getcwd()[0]}:
            cd {getcwd()}
            StartWindow.py""")
            a.close()

        else:
            remove(f"C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start "
                   f"Menu/Programs/Startup/app_startup.bat")

    def restore_action(self):
        File_restore = QtWidgets.QFileDialog()
        File_restore.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        file_name = File_restore.getOpenFileName(None, "Select your backup file", "", "Backup files (*.bak)")

        if len(file_name[0]) != 0:
            with open(file_name[0], "rt") as file:
                text = file.read()

            if file_name[0][0:-4].endswith("_favorite"):
                with open("file/FavoriteContacts.txt", "wt") as file:
                    file.write(text)

            else:
                with open("file/Contacts.txt", "wt") as file:
                    file.write(text)

    def backup_action(self):
        File_backup = QtWidgets.QFileDialog()
        File_backup.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        file_name = File_backup.getSaveFileName()

        if len(file_name[0]) != 0:
            with open("file/Contacts.txt", "rt") as file:
                contacts = file.read()

            with open("file/FavoriteContacts.txt", "rt") as file:
                favoriteContacts = file.read()

            with open(f"{file_name[0]}.bak", "wt") as file:
                file.write(contacts)

            with open(f"{file_name[0]}_favorite.bak", "wt") as file:
                file.write(favoriteContacts)

    def aboutUs_action(self):
        global ratio_w
        global ratio_h

        Form_aboutUs = QtWidgets.QDialog()
        ui = Ui_Form_aboutUs()
        ui.setupUi(Form_aboutUs, ratio_w, ratio_h, ratio_font)
        Form_aboutUs.show()
        Form_aboutUs.exec_()

    def wizard_action(self):
        self.wizard.open()
        self.wizard.restart()

    def wizard_sound_action(self):
        playsound(f"file/page{self.wizard.currentId()}.mp3")
        self.wizard.next()

    def change_background_action(self):
        self.widget.setStyleSheet(f"border-image : url('file/background{self.num}.jpg');")
        if self.num >= 10:
            self.num = 0
        else:
            self.num += 1


ratio_w = 1
ratio_h = 1
ratio_font = 1
