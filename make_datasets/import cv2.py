import cv2
import numpy as np
import os
import random

# 저장할 디렉토리를 지정합니다.
output_directory = "line_tracer_training_images"
os.makedirs(output_directory, exist_ok=True)

# 이미지의 크기를 설정합니다.
image_width = 128
image_height = 128

# 생성할 이미지의 수를 지정합니다.
num_images = 20

# 선의 두께를 설정합니다.
line_thickness = 6  # 원하는 두께로 설정하세요

for i in range(num_images):
    # 흰 배경 이미지를 생성합니다.
    image = 255 * np.ones((image_height, image_width, 3), dtype=np.uint8)

    # 커브를 생성하기 위한 매개 변수 설정
    curve_amplitude = 20  # 커브 진폭 (20도 정도)
    curve_direction = 1  # 오른쪽으로 커브

    # 직선을 그리기 시작할 X 좌표를 설정합니다.
    start_x = image_width // 2

    # 커브를 추가한 직선을 그립니다.
    for y in range(image_height):
        x = start_x + curve_direction * int(curve_amplitude * np.sin((y / image_height) * np.pi))
        if 0 <= x < image_width:
            cv2.line(image, (x, 0), (x, image_height), (0, 0, 0), line_thickness)  # 검은색 선

    # 이미지를 저장합니다.
    image_filename = os.path.join(output_directory, f"line_image_{i + 1}.png")
    cv2.imwrite(image_filename, image)

print(f"{num_images}개의 이미지가 생성되고 {output_directory}에 저장되었습니다.")
