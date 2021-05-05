import matplotlib.pyplot as pyplot

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

class ReadLine:
    # action 是否被開啟 開啟就繼續執行
    # action 是否被開啟 沒開啟就跳掉

    read_break = False

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

    def getData(self, i, ser, read_break=False):
        while not read_break:
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
                ser.close()  # close serial
                pyplot.close(fig)  # close figure
                print('goodbye')

        ser.close()  # close serial
        pyplot.close(fig)  # close figure
        print('goodbye')


    def plot_close(self, ser):
        ser.close()  # close serial
        pyplot.close('all')  # close figure