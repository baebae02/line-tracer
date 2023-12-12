import numpy as np
import cv2
import time
from picamera2 import Picamera2, Preview
import serial

class Interface():

    def __init__(self):
        self.cmd = ""
        self.left_speed = 0
        self.right_speed = 0
        self.ser = serial.Serial("/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_7543931373735161F152-if00", 9600)
        self.camera = Picamera2()
        camera_configure = self.camera.create_still_configuration(main={"size":(320, 320)}, 
            lores={"size": (320, 320)}, display="lores")
        self.camera.start_preview(Preview.QTGL)
        # get_image 함수로 이동해야함
        # self.camera.start()
        # time.sleep(3)

    def finish(self):
        self.cmd = ("F\n").encode('ascii')
        self.ser.write(self.cmd)
    
    def stop_at_qr_code(self):
        self.cmd = ("R0\nL0\n").encode('ascii')
        time.sleep(5)

    def set_right_speed(self, speed):
        self.cmd = ("R%d\n" %speed).encode('ascii')
        self.ser.write(self.cmd)
    
    def set_left_speed(self, speed):
        self.cmd = ("L%d\n" %speed).encode('ascii')
        self.ser.write(self.cmd)
    
    def get_image_from_camera(self):
        img = np.empty((320, 320), dtype=np.uint8)
        img = self.camera.start()

        # 여기서 qr코드인지 아닌지 체크하는 코드가 있어야 할 것 같음 추후에 추가!

        img = img[:, :, 0] # 어차피 카메라가 흑백으로 설정되어 3개의 차원 모두 같은 값을 갖고 있으므로 2개의 차원 삭제
        
        threshold = int(np.mean(img))*0.5
        ret, img2 = cv2.threshold(img.astype(np.uint8), threshold, 255, cv2.THRESH_BINARY_INV)
        img2 = cv2.resize(img2, (16, 16), interpolation=cv2.INTER_AREA)
        
        return img2