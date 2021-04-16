from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    right_velocity = 0
    left_velocity = 0

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 640)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 801, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.mode1 = QtWidgets.QWidget()
        self.mode1.setObjectName("mode1")

        self.supervisor = QtWidgets.QLabel("Ready!")
        font = QtGui.QFont()
        font.setPointSize(64)
        self.supervisor.setFont(font)
        self.supervisor.move(300, 100)
        self.supervisor.resize(400, 60)
        self.supervisor.setObjectName("supervisor")

        self.right = QtWidgets.QPushButton(self.mode1)
        self.right.setGeometry(QtCore.QRect(220, 240, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.right.setFont(font)
        self.right.setObjectName("right")

        self.left = QtWidgets.QPushButton(self.mode1)
        self.left.setGeometry(QtCore.QRect(80, 240, 131, 131))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.left.setFont(font)
        self.left.setObjectName("left")

        self.foreward = QtWidgets.QPushButton(self.mode1)
        self.foreward.setGeometry(QtCore.QRect(650, 190, 131, 121))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.foreward.setFont(font)
        self.foreward.setObjectName("foreward")

        self.backward = QtWidgets.QPushButton(self.mode1)
        self.backward.setGeometry(QtCore.QRect(650, 370, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.backward.setFont(font)
        self.backward.setObjectName("backward")

        self.stop = QtWidgets.QPushButton(self.mode1)
        self.stop.setGeometry(QtCore.QRect(540, 300, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.mode1)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(90, 10, 534, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.right_lcd = QtWidgets.QLCDNumber(self.gridLayoutWidget_2)
        self.right_lcd.setObjectName("right_lcd")
        self.gridLayout_2.addWidget(self.right_lcd, 1, 1, 1, 1)

        self.left_lcd = QtWidgets.QLCDNumber(self.gridLayoutWidget_2)
        self.left_lcd.setObjectName("left_lcd")
        self.gridLayout_2.addWidget(self.left_lcd, 1, 0, 1, 1)

        # Battery
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 2, 1, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.progressBar_2 = QtWidgets.QProgressBar(self.gridLayoutWidget_2)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_2.addWidget(self.progressBar_2, 2, 0, 1, 1)

        self.gridLayoutWidget = QtWidgets.QWidget(self.mode1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 409, 381, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.B1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B1.setObjectName("B1")
        self.gridLayout.addWidget(self.B1, 0, 0, 1, 1)  # (self.B1,row,column,1 ,1)

        self.B2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B2.setObjectName("B2")
        self.gridLayout.addWidget(self.B2, 0, 1, 1, 1)

        self.B3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B3.setObjectName("B3")
        self.gridLayout.addWidget(self.B3, 0, 2, 1, 1)

        self.B4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B4.setObjectName("B4")
        self.gridLayout.addWidget(self.B4, 1, 0, 1, 1)

        self.B5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B5.setObjectName("B5")
        self.gridLayout.addWidget(self.B5, 1, 1, 1, 1)

        self.B6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B6.setObjectName("B6")
        self.gridLayout.addWidget(self.B6, 1, 2, 1, 1)

        self.tabWidget.addTab(self.mode1, "")
        self.mode2 = QtWidgets.QWidget()
        self.mode2.setObjectName("mode2")

        self.tabWidget.addTab(self.mode2, "")
        self.mode3 = QtWidgets.QWidget()
        self.mode3.setObjectName("mode3")
        self.tabWidget.addTab(self.mode3, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow): # interface
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.supervisor.setText(_translate("MainWindow", "I'm supervisor"))
        self.right.setText(_translate("MainWindow", ">"))
        self.left.setText(_translate("MainWindow", "<"))
        self.foreward.setText(_translate("MainWindow", "^"))
        self.backward.setText(_translate("MainWindow", "倒車檔"))
        self.stop.setText(_translate("MainWindow", "stop"))
        self.label_3.setText(_translate("MainWindow", "right velocity"))
        self.label_2.setText(_translate("MainWindow", "left velocity"))

        self.B1.setText(_translate("MainWindow", "1"))
        self.B2.setText(_translate("MainWindow", "2"))
        self.B3.setText(_translate("MainWindow", "3"))
        self.B4.setText(_translate("MainWindow", "4"))
        self.B5.setText(_translate("MainWindow", "5"))
        self.B6.setText(_translate("MainWindow", "6"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mode1), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mode2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mode3), _translate("MainWindow", "Page"))