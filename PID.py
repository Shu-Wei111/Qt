import serial

# define connection port, baud rates
COM_PORT = '/dev/tty.usbmodem14201'    # Arduino
BAUD_RATES = 115200                     # baud rates
ser = serial.Serial(COM_PORT, BAUD_RATES, timeout=1)  # time out /s

# ser.write("a".encode())
# ser.read("a".encode())

i = 0
x = []
y = []

class ReadLine:
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

try:
    while True:
        while ser.inWaiting():
            i += 1
            test = ReadLine(ser)
            data = test.readline()
            data = data.decode()
            data = data.split(',')  # 以 , 分割字串

            x.append(int(data[0]))
            y.append(int(data[0]))
            if i > 3:
                x.pop(0)
                y.pop(0)

except KeyboardInterrupt:
    ser.close()
    print('goodbye')