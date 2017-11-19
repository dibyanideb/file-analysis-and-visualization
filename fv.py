# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os,time
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(555, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 160, 531, 131))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 90, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.DROPB = QtWidgets.QComboBox(self.centralwidget)
        self.DROPB.setGeometry(QtCore.QRect(20, 20, 511, 51))
        self.DROPB.setObjectName("DROPB")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(17, 320, 531, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setProperty("visible",False)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 555, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(320, 90, 101, 41))
        self.pushButton1.setObjectName("pushButton")
        os.chdir('C:\\Users\\lenovo')
        x = "You are in " + os.getcwd() + " folder"
        x = x + "\nEnter the folder you wish to see the usage....."
        self.label.setText(x)
        self.DROPB.clear();
        l = os.listdir();
        self.DROPB.addItems(l);
        self.pushButton.clicked.connect(self.pb)
        self.pushButton1.clicked.connect(self.gr)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ENTER"))
        self.pushButton1.setText(_translate("MainWindow", "Gen Graph"))

    def pb(self):
        self.progressBar.setProperty("visible", True);
        for i in range(100):
            time.sleep(0.02);
            self.progressBar.setProperty("value", i + 1);
        self.progressBar.setProperty("visible", False);
        p = self.DROPB.currentText();
        k=os.getcwd();
        g=k+"\\"+p;
        if (os.path.isdir(g)):
            os.chdir(p);
        self.label.setText("You are in " + os.getcwd() + " folder");
        l = os.listdir();
        self.DROPB.clear();
        self.DROPB.addItems(l);
        if (os.path.isfile(g)):
            self.label.setText("\nFile created on : "+time.ctime(os.path.getctime(g))+"\nFile Last Accessed On :"+time.ctime(os.path.getatime(g))+"\nFile Last Modified On :"+time.ctime(os.path.getmtime(g)));
    def gr(self):
        sz = [];
        nm = [];
        er = os.getcwd()
        ui = os.listdir();
        ts=0;
        for item in ui:
            if (os.path.isfile(er + "\\" + item)):
                nm.append(item);
                sz.append(os.path.getsize(item));
                ts=ts+(os.path.getsize(item));
        import matplotlib.pyplot as plt
        plt.pie(sz, labels=nm, autopct='%1.1i%%')
        plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

