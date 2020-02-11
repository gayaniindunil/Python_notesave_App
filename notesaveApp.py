#Program created by Gayani Chandrarathne on  3th-feb-2020
# This program contains a GUI which could save notes in a text file.
# Notes can be added into a simple text edit box and once you click the save button notes will be saved to notes.txt in the program saved folder.
# Form implementation generated from reading ui file 'notesave.ui'

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox
from PyQt5.uic import loadUi
from datetime import date

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("notesave.ui",self)

        self.textEdit.setText(self.openNotes())
        self.saveBtn.clicked.connect(self.retrieveText)
        self.closeBtn.clicked.connect(self.close_application)
        self.show()

    def retrieveText(self):
        note =self.textEdit.toPlainText()
        today = date.today()
        # note = note + "\n" + str(today) + "\n"
        with open('notes.txt', 'w') as f:
            f.write(note)

    def openNotes(self):
        with open('notes.txt', 'r') as f:
            text = f.read()
        return(text)

    def close_application(self):
        mbox = QMessageBox()
        mbox.setWindowTitle("Close Window")
        mbox.setText("Are you sure you want to close the window?, You work is not saved. You need to save notes before closing?")
        mbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        choice = mbox.exec_()
        if choice == mbox.Yes:
            self.retrieveText()
            sys.exit()
        else:
            sys.exit()

def runProgram():
    app = QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Ui = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    if  not (os.path.isfile('notes.txt')):
        with open('notes.txt','w'): pass

    runProgram()
