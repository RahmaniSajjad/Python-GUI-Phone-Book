from PyQt5 import QtCore, QtGui, QtWidgets


# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


class Ui_Form_Calendar(object):
    def setupUi(self, Form, ratio_w, ratio_h, ratio_font):
        Form.setFixedSize(int(700 * ratio_w), int(400 * ratio_h))
        Form.setWindowTitle("Calendar")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file/CalendarIcon.png"))
        Form.setWindowIcon(icon)

        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(
            int(0 * ratio_w), int(0 * ratio_h), int(700 * ratio_w), int(400 * ratio_h)))
        self.calendarWidget.setFont(QtGui.QFont("Calibri", int(11 * ratio_font)))
        self.calendarWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.calendarWidget.showToday()
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setGridVisible(True)
