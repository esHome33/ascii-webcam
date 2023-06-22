import cv2
import cv3 as cv
import numpy as np
import os
import sys
from pynput.keyboard import *

def on_press(key):
	finish(key)

def on_release(key):
	pass

listener = Listener(on_press=on_press, on_release=on_release)

def finish(key):
	if key == Key.esc:
		listener.stop()
		os._exit(0)

def main():
	
	vc = cv.VideoCapture(0)

	if vc.isOpened():
		frame = vc.read()

		listener.start()

		while True :
			frame = vc.read()
			print(toASCII(frame))
		

	sys.exit()

def toASCII(frame, cols = 240, rows = 70):

	frame = cv.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
	height, width = frame.shape
	cell_width = width / cols
	cell_height = height / rows
	if cols > width or rows > height:
		raise ValueError('Too many cols or rows.')
	result = ""
	for i in range(rows):
		for j in range(cols):
			gray = np.mean(
				frame[int(i * cell_height):min(int((i + 1) * cell_height), height), int(j * cell_width):min(int((j + 1) * cell_width), width)]
			)
			result += grayToChar(gray)
		result += '\n'
	return result

def grayToChar(gray):
	CHAR_LIST = ".',;:clodxkO0KXNWM" # Replace by " .',;:clodxkO0KXNWM" if you want more precision  .:-=+*#%@
	num_chars = len(CHAR_LIST)
	return CHAR_LIST[
		min(
			int(gray * num_chars / 255),
			num_chars - 1
		)
	]
	
if __name__ == '__main__':
		main()
