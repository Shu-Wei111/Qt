# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout
import serial

from ui import Ui_MainWindow
import HX711_plot as HX

import matplotlib
matplotlib.use("Qt5Agg")  # 宣告使用Qt5

# define connection port, baud rates
COM_PORT = '/dev/tty.usbserial-1420'    # Arduino
BAUD_RATES = 115200                     # baud rates
ser = serial.Serial(COM_PORT, BAUD_RATES, timeout=1)  # time out /s

#COM_PORT_2 = '/dev/tty.usbserial-1410'  # ESP 8266
#BAUD_RATES_2 = 9600                     # baud rates
#ser_2 = serial.Serial(COM_PORT_2, BAUD_RATES_2, timeout=1)  # time out /s

class MainWindow(QtWidgets.QMainWindow):
    right_velocity = 0
    left_velocity = 0

    def __init__(self):  # 宣告時會自動執行的函式
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ProgressBar
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)  # set initial value

        # tab1 button clicked trigger
        self.ui.stop.clicked.connect(self.stop_button_clicked)
        self.ui.right.clicked.connect(self.right_button_clicked)
        self.ui.foreward.clicked.connect(self.forward_button_clicked)
        self.ui.left.clicked.connect(self.left_button_clicked)
        self.ui.backward.clicked.connect(self.backward_button_clicked)
        self.ui.stop.clicked.connect(self.stop_button_clicked)

        # tab2 button clicked trigger
        self.ui.plot_action.clicked.connect(self.plot_action_button_clicked)
        self.ui.plot_stop.clicked.connect(self.plot_stop_button_clicked)

    def stop_button_clicked(self):
        print("stop")

    def right_button_clicked(self):
        self.right_velocity = self.right_velocity + 1
        self.ui.right_lcd.display(self.right_velocity)  # lcd test
        self.ui.progressBar.setValue(self.right_velocity)  # progress test
        # ser.write("a".encode())
        print("right")

    def forward_button_clicked(self):
        print("forward")
    def left_button_clicked(self):
        self.left_velocity = self.left_velocity + 1
        self.ui.left_lcd.display(self.left_velocity)
        # ser_2.write("a".encode())
        print("left")
    def backward_button_clicked(self):
        print("backward")

    # tab 2
    def plot_action_button_clicked(self):
        HX.read_continue = True
        HX.ReadLine.getData(self, ser)

    def plot_stop_button_clicked(self):
        HX.read_continue = False
        print('Figure closed!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
