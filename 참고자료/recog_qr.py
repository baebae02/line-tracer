import time
import picamera
from PIL import Image
from pyzbar.pyzbar import decode

def read_qr_code():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        time.sleep(2)  # 카메라가 따뜻해지도록 대기

        while True:
            # 카메라에서 프레임 캡처
            stream = io.BytesIO()
            camera.capture(stream, format='jpeg')
            stream.seek(0)

            # QR 코드 디코드
            image = Image.open(stream)
            codes = decode(image)

            # 디코딩된 데이터가 있으면 출력
            if codes:
                for code in codes:
                    print("QR 코드 데이터:", code.data.decode('utf-8'))
                    return code.data.decode('utf-8')

if __name__ == "__main__":
    read_qr_code()