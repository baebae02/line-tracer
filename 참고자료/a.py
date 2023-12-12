import serial
import time

ser = serial.Serial("/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_7543931373735161F152-if00", 9600)
speed = 0

while(True):
    if speed % 2 == 0:
        cmd = ("R%d\n" % speed).encode('ascii')
        print("My cmd is %s" % cmd)
    else:
        cmd = ("L%d\n" % speed).encode('ascii')
        print("My cmd is %s" % cmd)
    ser.write(cmd)
    read_serial=ser.readline()
    print(read_serial)
    speed = speed + 1
