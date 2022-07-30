# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textToSpeech.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from gtts import gTTS
import random


class Ui_MainWindow(object):

    # Function for alert message dialog
    def alertBox(self,title,message):
        alertMessage = QtWidgets.QMessageBox()
        alertMessage.setWindowTitle(title)
        alertMessage.setText(message)
        alertMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
        alertMessage.exec_()

    # Function for text into speech converting
    def textToSpeech(self):
        # Converting text area text to string and Storing in userText variable
        userText = str(self.textArea.toPlainText())

        # Checking if user left the text area blank
        if len(userText) == 0:
            self.alertBox('Blank','Please write or paste your text into the text area.')
        else:
            # Language for audio
            language = "en"

            # Generating file name along with path
            num = random.randrange(100,999,2)
            getFiveChars = userText[0:5]

            fileName = "output/" + str(num) + "-" + getFiveChars + ".mp3"

            # Calling the gTTS class for converting text into audio
            file = gTTS(text=userText,lang= language,slow=False)
            # Saving the File
            saveFile = file.save(fileName)

            # Checking file for errors
            if saveFile != "" or saveFile !=None:
                self.alertBox('Success','Your audio file has been generated successfully. Check output folder.')
            else:
                self.alertBox('Error','Something went wrong!')



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/bg.jpg);\n"
"background-position: center bottom;\n"
"background-repeat: no-repeat;\n"
"background-attachment: fixed;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.appTitle = QtWidgets.QLabel(self.centralwidget)
        self.appTitle.setGeometry(QtCore.QRect(230, 10, 181, 51))
        self.appTitle.setStyleSheet("font-family: Calibri;\n"
"font-size: 28px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-image: url(none);")
        self.appTitle.setObjectName("appTitle")
        self.textTitle = QtWidgets.QLabel(self.centralwidget)
        self.textTitle.setGeometry(QtCore.QRect(90, 60, 221, 51))
        self.textTitle.setStyleSheet("font-family: Calibri;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: white;\n"
"background-image: url(none);")
        self.textTitle.setObjectName("textTitle")
        self.textArea = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textArea.setGeometry(QtCore.QRect(90, 120, 471, 231))
        self.textArea.setStyleSheet("font-family: Calibri;\n"
"padding: 8px;\n"
"color: orange;\n"
"font-size: 20px;\n"
"border-radius: 12px;\n"
"font-weight: bold;\n"
"border: 2px solid white; ")
        self.textArea.setObjectName("textArea")
        self.convertBtn = QtWidgets.QPushButton(self.centralwidget)
        self.convertBtn.setGeometry(QtCore.QRect(90, 380, 471, 41))
        self.convertBtn.setStyleSheet("background-image: url(none);\n"
"background-color: orange;\n"
"font-family: Calibri;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"color: white;\n"
"border-radius: 8px;")
        self.convertBtn.setObjectName("convertBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        # Connecting textToSpeech function with Convert to audio button
        self.convertBtn.clicked.connect(self.textToSpeech)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text to Speech"))
        self.appTitle.setText(_translate("MainWindow", "Text to Speech"))
        self.textTitle.setText(_translate("MainWindow", "Write or paste your text:"))
        self.convertBtn.setText(_translate("MainWindow", "Convert to audio"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
