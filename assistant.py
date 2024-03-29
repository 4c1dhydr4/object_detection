from datetime import datetime
from pygame import mixer
from gtts import gTTS
from googletrans import Translator
from arduino import R2D2
from telegram_bot import Telegram

class Assistant:
	def __init__(self, name, user_name, language):
		self.name = name
		self.user_name = user_name
		self.translator = Translator()
		self.language = language
		self.mp3_id = 0
		self.r2d2 = False
		self.telegram = None
		self.init()

	def init(self):
		self.r2d2 = R2D2()
		mixer.init()
		self.telegram = Telegram()

	def speake(self, text):
		text = self.translate(text)
		gtts = gTTS(text=text, lang=self.language)
		audio = './mp3/' + str(self.mp3_id) + '.mp3'
		gtts.save(audio)
		mixer.music.load(audio)
		mixer.music.play()
		self.mp3_id = self.mp3_id + 1
		print(text)

	def translate(self, text):
		return self.translator.translate(text, dest=self.language).text

	def shut_up(self):
		mixer.music.stop()

	def say_my_name(self):
		text = 'Mi nombre es {}, y seré tu asistente sonoro'.format(self.name)
		return self.translate(text)

	def say_hi(self):
		hour = datetime.now().hour
		text = ''
		if hour >= 0 and hour < 12:
			text = 'Buenos días {}'.format(self.user_name)
		elif hour >= 12 and hour < 18:
			text = 'Buenas tardes {}'.format(self.user_name)
		elif hour >= 18 and hour <= 23:
			text = 'Buenas noches {}'.format(self.user_name)
		else:
			text = 'Saludos {}'.format(self.user_name)
		return self.translate(text)

	def say_initialize(self):
		return ''

	def main_menu(self, item=0):
		m = 'Presiona el primer botón para emergencia \
			o comunicarte con algún amigo, el segundo botón \
			para usar la función de asistencia mediante \
			reconocimiento del entorno, pulsa el tercer botón \
			para utilizar la función de amplificación de sonidos; \
			o pulsa el cuarto botón para utilizar la función GPS'
		m = self.translate(m)
		self.speake(m)
		inp = self.get_input()
		self.shut_up()
		return inp

	def get_input(self):
		opt = '0'
		opt = self.r2d2.get_input()
		return opt


