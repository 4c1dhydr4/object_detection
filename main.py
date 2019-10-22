import time
from core import Detector
from assistant import Assistant
from pygame import mixer

frames = [
	'animals.jpg',
	'fruits.png',
	'test45.jpg',
	'megan.jfif',
	'test01.jpg',
]

langs = [
	'mp3/lang_es.mp3',
	'mp3/lang_en.mp3',
	'mp3/lang_fr.mp3',
	'mp3/lang_de.mp3',
]

megan = None
det = None

def get_lang():
	mixer.init()
	mixer.music.load(langs[0])
	mixer.music.queue(langs[1])
	mixer.music.play()

	inp = input('Ingresa la Opción: ')
	if inp == '1':
		mixer.music.stop()
		return 'es'
	elif inp == '2':
		mixer.music.stop()
		return 'en'
	elif inp == '3':
		mixer.music.stop()
		return 'fr'
	elif inp == '4':
		mixer.music.stop()
		return 'de'
	else:
		mixer.music.stop()
		return 'es'


def detection():
	stop = False
	frame = 0
	while not stop:
		megan.shut_up()
		# frame = det.take_picture()
		detection_text = det.get_detection('input/' + frames[frame])
		print('Detección: ', detection_text)
		megan.speake(detection_text)
		if megan.get_input() == '1':
			stop = True
		frame += 1
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