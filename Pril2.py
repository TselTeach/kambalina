

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox

import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(300, 330, 200, 23))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 330, 100, 23))
        self.pushButton.setObjectName("pushButton")
        self.btn_otvet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_otvet.setGeometry(QtCore.QRect(500, 330, 100, 23))
        self.btn_otvet.setObjectName("btn_otvet")
        self.otvet = QtWidgets.QTextEdit(self.centralwidget)
        self.otvet.setGeometry(QtCore.QRect(270, 100, 181, 101))
        self.otvet.setObjectName("otvet")
        MainWindow.setCentralWidget(self.centralwidget)
        self.i=0
        self.j=0
        self.kol_vo_prav = 0
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 191, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("IMG_5163.JPG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.results2(self.j,self.i))
        self.pushButton2.clicked.connect(lambda: self.sled(self.i,self.j))
        self.btn_otvet.clicked.connect(lambda: self.otvet2(self.i))
    def results2(self, j, i):
        b = ["IMG_5067.PNG","IMG_5073.JPG","IMG_5060.JPG", "IMG_5075", "IMG_5077", "IMG_5079", "IMG_5082", "IMG_5118", "IMG_5120", "IMG_5122", "IMG_5125", 'IMG_5218', "IMG_5130", "IMG_5132", "IMG_5137", "IMG_5138", "IMG_5140", "IMG_5142", "IMG_5144", "IMG_5144", "IMG_5147"]
        if self.j == self.i:
            self.label_3.setGeometry(QtCore.QRect(30, 40, 191, 261))
            self.label_3.setText("")
            self.label_3.setPixmap(QtGui.QPixmap(b[j]))
            self.label_3.setScaledContents(True)
            self.label_3.setObjectName("label_3")
            self.j=self.j+1
            print(self.j, self.i)
        elif self.j < self.i:
            print(self.j, self.i)
            self.j = self.i
            self.label_3.setGeometry(QtCore.QRect(30, 40, 191, 261))
            self.label_3.setText("")
            self.label_3.setPixmap(QtGui.QPixmap(b[self.j]))
            self.label_3.setScaledContents(True)
            self.label_3.setObjectName("label_3")
            self.j=self.j+1
            print(self.j, self.i)
    def otvet2 (self,i):
        c = ["Hat", "Table", "Dog", "Ceiling", "Carrot", "Puddle", "Coat", "Eagle", "Aunt", "Whistle", "Raspberry", "Fair","Bridge", "Blanket", "Pot", "Bug", "Fork", "Belly", "Finger", "Ski"]
        if self.otvet.toPlainText() == c[i]:
            verno = QMessageBox()
            verno.setText ("Молодец, верно!")
            verno.setDefaultButton(QMessageBox.Ok)
            verno.buttonClicked.connect(self.popup_action)
            self.kol_vo_prav = self.kol_vo_prav + 1
            verno.exec()
        else:
            neverno = QMessageBox()
            neverno.setText ("Неправильно, попробуй ещё раз!")
            neverno.setDefaultButton(QMessageBox.Ok)
            neverno.exec()
    def popup_action(self,btn):
        if btn.text() == "OK":
            self.otvet.setText("Введите ответ")
            self.sled(self.i,self.j)

    def sled(self, i,j):
        a = ["IMG_5164.JPG","IMG_5182.JPG","IMG_5165","IMG_5166", "IMG_5167","IMG_5168", "IMG_5169", "IMG_5170", "IMG_5171", "IMG_5172", "IMG_5173", "IMG_5174", "IMG_5175", "IMG_5177", "IMG_5176", "IMG_5178", "IMG_5179", "IMG_5180", "IMG_5181"]
        if (len(a))==self.i:
            verno = QMessageBox()
            verno.setText ("Ты ответил правильно на "+ str(self.kol_vo_prav))
            verno.setDefaultButton(QMessageBox.Ok)
            verno.exec()
        self.label_3.setGeometry(QtCore.QRect(30, 40, 191, 261))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(a[i]))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.i=self.i+1


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton2.setText(_translate("MainWindow", "Следующий вопрос"))
        self.pushButton.setText(_translate("MainWindow", "Показать ответ"))
        self.btn_otvet.setText(_translate("MainWindow", "Ответить"))
        self.otvet.setText(_translate("MainWindow", "Введи ответ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
