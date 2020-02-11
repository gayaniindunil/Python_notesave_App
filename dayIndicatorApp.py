import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow
from PyQt5.uic import loadUi
from datetime import date
from notesaveApp import MainWindow

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage,self).__init__()
        loadUi("dayIndicator.ui",self)

        self.closeBtn.clicked.connect(self.record_data)
        self.show()

    def openNotes(self):
        self.dialog = QDialog()
        self.nsui = MainWindow()
        # Ui.hide()
        self.nsui.show()
        sys.exit(self.nsui.exec_())

    def record_data(self):
        state = self.horizontalSlider.value()
        today = date.today()
        note = str(today) + "\n" + "todays feeling: " + str(state) + "\n"
        with open('logs.txt', 'a') as f:
            f.write(note)
        self.openNotes()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    Ui = MainPage()
    sys.exit(app.exec_())
