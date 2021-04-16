# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'direction_click.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(300, 190, 141, 151))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.stop.setFont(font)
        self.stop.setObjectName("pushButton")
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(450, 190, 141, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.right.setFont(font)
        self.right.setObjectName("right")

        self.forward = QtWidgets.QPushButton(self.centralwidget)
        self.forward.setGeometry(QtCore.QRect(300, 30, 141, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.forward.setFont(font)
        self.forward.setObjectName("forward")

        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(150, 190, 141, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.left.setFont(font)
        self.left.setObjectName("left")

        self.backward = QtWidgets.QPushButton(self.centralwidget)
        self.backward.setGeometry(QtCore.QRect(300, 350, 141, 151))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.backward.setFont(font)
        self.backward.setObjectName("backward")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def stop_button_clicked(self):
        print("stop")
    def right_button_clicked(self):
        print("right")
    def forward_button_clicked(self):
        print("forward")
    def left_button_clicked(self):
        print("left")
    def backward_button_clicked(self):
        print("backward")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stop.setText(_translate("MainWindow", "stop"))
        self.right.setText(_translate("MainWindow", ">"))
        self.forward.setText(_translate("MainWindow", "＾"))
        self.left.setText(_translate("MainWindow", "<"))
        self.backward.setText(_translate("MainWindow", "巴庫"))

        # button clicked trigger
        self.stop.clicked.connect(self.stop_button_clicked)
        self.right.clicked.connect(self.right_button_clicked)
        self.forward.clicked.connect(self.forward_button_clicked)
        self.left.clicked.connect(self.left_button_clicked)
        self.backward.clicked.connect(self.backward_button_clicked)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
