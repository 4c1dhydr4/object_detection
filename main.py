import os
import time
from core import Detector
from assistant import Assistant
from pygame import mixer

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


frames = [
	'animals.jpg',
	'fruits.png',
	'test45.jpg',
	'megan.jfif',
	'test01.jpg',
]

megan = None
det = None

def get_lang():
	mixer.init()
	mixer.music.load('mp3/lang.mp3')
	mixer.music.play()

	inp = input('Ingresa la Opción: ')
	mixer.music.stop()
	if inp == '1':
		return 'es'
	elif inp == '2':
		return 'en'
	elif inp == '3':
		return 'fr'
	elif inp == '4':
		return 'de'
	else:
		return 'es'

def detection():
	stop = False
	frame = 0
	while not stop:
		megan.shut_up()
		# detection_text = det.get_detection('input/' + frames[frame])
		ok, frame = det.take_picture()
		if ok:
			detection_text = det.get_detection(frame)
			print('Detección: ', detection_text)
			if len(detection_text) == 0:
				megan.speake('No he logrado detectar objetos')
			else:
				megan.speake(detection_text)

		else:
			megan.speake("Error al obtener fotografía")
		if megan.get_input() == '1':
			stop = True
		# frame += 1
	megan.speake('Gracias por usar el asistente de reconocimiento del entorno')
	time.sleep(5)

def run(det, megan):
	megan.speake(megan.say_hi() + ';' + megan.say_my_name()) 
	det.initialize(cam_number=0)
	inp = megan.main_menu()

	if inp == '1':
		pass
	if inp == '2':
		detection()
	if inp == '3':
		pass
	if inp == '4':
		pass

if __name__ == '__main__':
	lang = get_lang()
	megan = Assistant(name='Megan', user_name='Luis', language=lang)
	det = Detector(
		"models/yolo-tiny.h5", 
		"output/", language=lang, 
		translator=megan.translator)
	run(det, megan)