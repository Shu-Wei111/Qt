import matplotlib.pyplot as pyplot
from PyQt5 import QtGui, QtWidgets
from matplotlib.backends.backend_template import FigureCanvas

from ui import Ui_MainWindow

read_continue = True
i = 0

class ReadLine:
    # action 是否被開啟 開啟就繼續執行
    # action 是否被開啟 沒開啟就跳掉

    def __init__(self, s):
        self.ui = Ui_MainWindow()
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

    def getData(self,  ser):

        x = []
        y = []

        # fig = pyplot.figure(figsize=(5, 3))
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
        pyplot.tight_layout()

        # ## Tab_2 ## #
        self.ui.HX711_plot = QtWidgets.QWidget()
        self.ui.HX711_plot.setObjectName("HX711_plot")

        # objects in tab2
        self.figure = fig
        self.canvas = FigureCanvas(self.figure)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.plot()

        self.tabWidget.addTab(self.HX711_plot, "")

        j = 0

        try:
            while read_continue:
                print("wait")
                while ser.inWaiting():
                    j += 1
                    test = ReadLine(ser)
                    data = test.readline()
                    data = data.decode()
                    data = data.split(',')
                    x.append(int(data[0]))
                    y.append(int(data[1]))
                    if j > 3:
                        x.pop(0)
                        y.pop(0)
                    line1.set_data(x, y)
                    ax.autoscale_view(True, True, True)
                    fig.canvas.draw()
                    pyplot.pause(0.00001)

            # ser.close()  # close serial
            pyplot.close(fig)  # close figure
            print('goodbye')

        except KeyboardInterrupt:
            pyplot.close(fig)  # close figure
            print('goodbye')
