import pytesseract as pytxt
from PIL import Image
import cv2

#for x in range(1,54):
#print(pytxt.image_to_string(Image.open('/home/pi/object_detection/pictures/{}.png'.format('01'))))
def get_pic():
	video_capture = cv2.VideoCapture(0)
	if not video_capture.isOpened():
		print('not video')
	ret, frame = video_capture.read()
	video_capture.release()
	im = Image.fromarray(frame[:,:,::-1])
	x = pytxt.image_to_string(im)
	print(x)

while True:
	get_pic()
