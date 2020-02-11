import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow
from datetime import date
import notesaveApp
from dayIndicatorApp  import MainPage
from notesaveApp import MainWindow

class APP():
    def __init__(self):
        pass

    def openDayindicator(self):
        self.MainWindow = QMainWindow()
        self.Ui = MainPage()

    def openNoteSave(self):
        self.window = QDialog()
        self.Ui = MainWindow()

    def Checker(self):
        with open('logs.txt', 'r') as f:
            lines = f.read().splitlines()

        if len(lines)> 1: #check app is running for the first time
            last_day = lines[-2] #check last saved record

            today =  date.today()
            if last_day == str(today): #app is opened before in the same day
                self.openNoteSave()
            else:
                self.openDayindicator() #app is open for the firsttime today
        else:
            self.openDayindicator()

    def main(self):
        app = QApplication(sys.argv)
        self.Checker()
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = APP()
    app.main()
    sys.exit(app.exec_())
