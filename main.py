# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import serial
from ui import Ui_MainWindow
# import HX711_plot as HX
import sys

import matplotlib
matplotlib.use("Qt5Agg")
import numpy as np
import matplotlib.pyplot as pyplot

# define connection port, baud rates
COM_PORT = '/dev/tty.usbmodem14201'    # Arduino
BAUD_RATES = 115200                     # baud rates
ser = serial.Serial(COM_PORT, BAUD_RATES, timeout=1)  # time out /s

#COM_PORT_2 = '/dev/tty.usbserial-1410'  # ESP 8266
#BAUD_RATES_2 = 9600                     # baud rates
#ser_2 = serial.Serial(COM_PORT_2, BAUD_RATES_2, timeout=1)  # time out /s

x = []
y = []
fig = pyplot.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'o-', lw=10, markersize=20)

pyplot.xlabel('X')
pyplot.ylabel('Y')
pyplot.title('Center of mass')
pyplot.axis([-2000, 2000, -2000, 2000])
pyplot.grid(axis='y')
pyplot.ion()
pyplot.show()
i = 0

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

    def stop_button_clicked(self):
        print("stop")

    def right_button_clicked(self):
        self.right_velocity = self.right_velocity + 5
        self.ui.right_lcd.display(self.right_velocity)  # lcd test
        self.ui.progressBar.setValue(self.right_velocity)  # progress test
        ser.write("a".encode())
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

    def plot_action_button_clicked(self):
        ReadLine.readdd(self, 0)
        print("gogo")

    def set_tab_groupbox(self):
        print("setting")

# 建立MainWindow的子類別ReadLine
class ReadLine(MainWindow):
    # action 是否被開啟 開啟就繼續執行
    # action 是否被開啟 沒開啟就跳掉

    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    print('hello')
    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i + 1]
            self.buf = self.buf[i + 1:]
            return r
        while True:
            i = max(1, min(2048, self.s.inWaiting()))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i + 1]
                self.buf[0:] = data[i + 1:]
                return r
            else:
                self.buf.extend(data)
    def readdd(self, i):
        try:
            while True:
                while ser.inWaiting():
                    i += 1
                    test = ReadLine(ser)
                    data = test.readline()
                    data = data.decode()
                    data = data.split(',')
                    x.append(int(data[0]))
                    y.append(int(data[1]))
                    if i > 3:
                        x.pop(0)
                        y.pop(0)
                    line1.set_data(x, y)
                    ax.autoscale_view(True, True, True)
                    fig.canvas.draw()
                    pyplot.pause(0.00001)
        except KeyboardInterrupt:
            ser.close()
            print('goodbye')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
