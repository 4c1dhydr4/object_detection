from datetime import datetime
from pygame import mixer
# from playsound import playsound
from gtts import gTTS
from googletrans import Translator

class Assistant:
	def __init__(self, name, user_name, language):
		self.name = name
		self.user_name = user_name
		self.translator = Translator()
		self.language = language
		self.mp3_id = 0
		self.mixer = mixer.init()

	def speake(self, text):
		gtts = gTTS(text=text, lang=self.language)
		audio = './mp3/' + str(self.mp3_id) + '.mp3'
		gtts.save(audio)
		mixer.music.load(audio)
		mixer.music.play()
		self.mp3_id = self.mp3_id + 1

	def say_my_name(self):
		return 'Mi nombre es {}'.format(self.name)

	def say_hi(self):
		hour = datetime.now().hour
		if hour >= 0 and hour < 12:
			return 'Buenos días {}'.format(self.user_name)
		elif hour >= 12 and hour < 18:
			return 'Buenas tardes {}'.format(self.user_name)
		elif hour >= 18 and hour <= 23:
			return 'Buenas noches {}'.format(self.user_name)
		else:
			return 'Saludos {}'.format(self.user_name)

	def say_initialize(self):
		return ''

	def main_menu(self, item=0):
		m = 'Presiona el primer botón para emergencia o comunicarte con algún amigo, el segundo botón para usar la función de asistencia mediante reconocimiento del entorno, pulsa el tercer botón para utilizar la función de amplificación de sonidos; o pulsa el cuarto botón para utilizar la función GPS'
		if item == 0:
			return m

