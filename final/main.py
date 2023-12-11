from Interface import Interface
import numpy as np
import time
import cv2
import tensorflow as tf

class Main:

	def __init__(self):
		self.interface = Interface()
		self.model = tf.keras.models.load_model('/Users/josua/Desktop/sua/1_uos/0_cs/3-2/임베/line-tracer/trained_model.h5')
		self.interface.set_left_speed(0)
		self.interface.set_right_speed(0)

		self.velocity = 0
		self.direction = 0

	def calculate_speed(self, direction):
		if direction < -1.0:
			direction = -1.0
		if direction > 1.0:
			direction = 1.0
		if direction < 0.0:
			left_speed = 1.0+direction
			right_speed = 1.0
		else:
			right_speed = 1.0-direction
			left_speed = 1.0
		
		self.interface.set_right_speed(right_speed)
		self.interface.set_left_speed(left_speed)
	
	def drive(self):
		while True:
			img = self.interface.get_image_from_camera()
			img = np.reshape(img,img.shape[0]**2)
			# 만약 qr코드 면
			# self.interface.stop_at_qr_code()
			direction = self.model.predict_direction(img)
			self.calculate_speed(direction[0][0])

			time.sleep(0.001)
			# 종료 조건 필요!
			# self.interface.finish()
			# break

Main().drive()
