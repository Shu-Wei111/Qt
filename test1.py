import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
from next import Ui_MainWindow

# define connection port, baud rates
COM_PORT = '/dev/tty.usbserial-1410'
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # button clicked trigger
        self.stop.clicked.connect(self.stop_button_clicked)
        self.right.clicked.connect(self.right_button_clicked)
        self.foreward.clicked.connect(self.forward_button_clicked)
        self.left.clicked.connect(self.left_button_clicked)
        self.backward.clicked.connect(self.backward_button_clicked)

    def stop_button_clicked(self):
        print("stop")
    def right_button_clicked(self):
        self.right_velocity = self.right_velocity + 1
        self.right_lcd.display(self.right_velocity)
        ser.write("a".encode())
        print("right")
    def forward_button_clicked(self):
        print("forward")
    def left_button_clicked(self):
        self.left_velocity = self.left_velocity + 1
        self.left_lcd.display(self.left_velocity)
        ser.write("b".encode())
        print("left")
    def backward_button_clicked(self):
        print("backward")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
