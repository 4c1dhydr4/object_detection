import os
import time
from core import Detector
from assistant import Assistant
from pygame import mixer
from telegram_bot import Telegram
from arduino import R2D2

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'

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

	inp = R2D2().get_input()
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
			if len(detection_text) == 0:
				megan.speake('No he logrado detectar objetos')
			else:
				megan.speake(detection_text)
		else:
			megan.speake("Error al obtener fotografía")
		opt = megan.get_input()
		if opt == '4':
			stop = True
		# frame += 1
	megan.speake('Gracias por usar el asistente de reconocimiento del entorno')
	time.sleep(5)

def emergency(detector, lang):
	megan.speake('Enviando mensaje de emergencia a contactos enlazados')
	telegram = Telegram()
	emergency_text = 'Me encuentro en una emergencia, por favor necesito ayuda. Te envío mi ubicación.'
	text = detector.translator.translate(emergency_text, dest=lang).text
	time.sleep(5)
	megan.speake(telegram.send_text(text))
	time.sleep(2)
	megan.speake('Capturando y enviando fotografías. Preciona 4 para cancelar y cualquier botón para capturar imágen y enviarla')
	time.sleep(7)
	stop = False
	while not stop:
		ok, frame = det.take_picture()
		if ok:
			megan.speake(telegram.send_picture(frame))
		else:
			megan.speake("Error al capturar fotografía")
		opt = megan.get_input()
		if opt == '4':
			stop = True
	megan.speake("Gracias por usar el servicio de emergencia")


def gps():
	megan.speake('Bienvenido a la función de Navegación GPS')

def run(det, megan):
	megan.speake(megan.say_hi() + ';' + megan.say_my_name()) 
	det.initialize(cam_number=0)
	inp = megan.main_menu()
	if inp == '1':
		emergency(det, megan.language)
	if inp == '2':
		detection()
	if inp == '3':
		pass
	if inp == '4':
		gps()

if __name__ == '__main__':
	lang = get_lang()
	megan = Assistant(name='Megan', user_name='Luis', language=lang)
	det = Detector(
		"models/yolo-tiny.h5", 
		"output/", language=lang, 
		translator=megan.translator)
	run(det, megan)