import serial
import time

ser = serial.Serial("/dev/cu.usbmodem143301", 9600)
speed = 0
i = 0
while(True):
    if i % 2 == 0:
        cmd = ("R%f\n"%0.3).encode('ascii')
        ser.write(cmd)
        print("turn right")
    elif i % 3 == 0:
        cmd = ("L%f\n"%0.3).encode('ascii')
        ser.write(cmd)
        print("turn left")
    else:
        cmd = ("G\n").encode('ascii')
        ser.write(cmd)
        print("go straight")
    time.sleep(1)
    read_serial=ser.readline()
    print(read_serial)
    i = i + 1
