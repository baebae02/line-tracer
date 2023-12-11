import numpy as np
import os
import cv2
import random
import pickle

# 저장할 디렉토리를 지정합니다.
output_directory = "[Left]training_images_without_noise(light)"
os.makedirs(output_directory, exist_ok=True)

def draw_left_without_noise(index):
    # 이미지의 크기를 설정합니다.
    image_width = 16
    image_height = 16

    # 리스트를 사용하여 픽셀 값과 레이블을 저장합니다.
    training_data = []

    # 선의 두께를 설정합니다.
    line_thickness = random.randint(1, 4)

    # 레이블을 설정합니다.
    label = -1.0

    # 커브를 생성하기 위한 매개 변수 설정
    curve_amplitude = random.uniform(1, 4)  # 커브
    curve_direction = -1  # 왼쪽으로 커브

    # 직선을 그리기 시작할 X 좌표를 설정합니다.
    start_x = image_width // 2

    # 커브를 추가한 직선을 그립니다.
    image = 255 * np.ones((image_height, image_width), dtype=np.uint8)

    for y in range(image_height):
        random_offset = random.randint(-1, 1)
        random_offset = 0
        x = start_x + curve_direction * int(curve_amplitude * (y / image_height) + random_offset)
        if 0 <= x < image_width:
            cv2.line(image, (x, y), (x, y), (128, 128, 128), line_thickness)  # 검정색 선

    image = np.flipud(image)

    # 이미지의 픽셀 값을 저장합니다.
    pixel_values = (255 - image).flatten()  # 흰색 부분을 255로, 회색 부분을 128로 변경

    # 16x16 배열로 변환합니다.
    pixel_values_16x16 = pixel_values.reshape((16, 16), order='C')  # order를 'C'로 지정하여 행 기준으로 배열
    pixel_values_16x16 = pixel_values_16x16.astype('uint8')

    # 픽셀 값과 레이블을 저장합니다.
    training_data.append((label, pixel_values_16x16))

    # 저장된 훈련 데이터를 출력합니다.
    for label, data in training_data:
        print(f"Label: {label}")
        print(f"Data:\n{data}")
        print("===")

    # 이미지를 저장합니다.
    image_filename = os.path.join(output_directory, f"line_image_left_without_noise_{index}.png")
    cv2.imwrite(image_filename, image)
    print(f"이미지가 생성되고 {image_filename}에 저장되었습니다.")
    data_set = (-1.0, 1.0, pixel_values_16x16)
    return data_set

# Load existing data if the file exists
try:
    with open('training_test.p', 'rb') as f:
        existing_data = pickle.load(f)
except FileNotFoundError:
    existing_data = []

# Append new data to the existing data
for i in range(1000):
    data_set = draw_left_without_noise(i)
    existing_data.append(data_set)

# Save the combined data back to the file
with open('training_test.p', 'wb') as f:
    pickle.dump(existing_data, f)
    print('training_test.p에 저장되었습니다.')