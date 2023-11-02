import cv2
import numpy as np
import os
import random

# 저장할 디렉토리를 지정합니다.
output_directory = "line_tracer_training_images"
os.makedirs(output_directory, exist_ok=True)

# 이미지의 크기를 설정합니다.
image_width = 256
image_height = 256

# 생성할 이미지의 수를 지정합니다.
num_images = 20

# 선의 두께를 설정합니다.
line_thickness = 30  # 원하는 두께로 설정하세요

for i in range(num_images):
    # 흰 배경 이미지를 생성합니다.
    image = 255 * np.ones((image_height, image_width, 3), dtype=np.uint8)

    # 커브를 생성하기 위한 매개 변수 설정
    curve_amplitude = 50  # 커브 진폭을 증가시켜보세요
    curve_frequency = 3  # 곡선의 주기 (2배수로 설정하면 더 뚜렷한 곡선이 생성됩니다)
    
    # 직선을 그리기 시작할 X 좌표를 설정합니다.
    start_x = image_width // 3

    # 커브를 추가한 직선을 그립니다.
    for y in range(image_height):
        x = start_x + int(curve_amplitude * np.sin(curve_frequency * (y / image_height) * np.pi))
        if 0 <= x < image_width:
            cv2.line(image, (x, y), (x+line_thickness, y), (0, 0, 0), line_thickness)  # 검은색 선
    # 이미지를 저장합니다.
    image_filename = os.path.join(output_directory, f"line_image_{i + 1}.png")
    cv2.imwrite(image_filename, image)

print(f"{num_images}개의 이미지가 생성되고 {output_directory}에 저장되었습니다.")

