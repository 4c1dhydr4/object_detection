import telegram
import logging

# TOKEN = '792970316:AAHzgtxfn-nyQYhNnraUSM0Uz7GEFrFRQJ0'
TOKEN = '990774114:AAG86TJPyeX8X8SQIF2miirkS8joRbT-Pmk'
chat_id = 771607185

class Telegram:
	def __init__(self):
		self.bot = self.set_telepy()

	def set_telepy(self):
		logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
		logger = logging.getLogger(__name__)
		return telegram.Bot(TOKEN)

	def send_text(self, text):
		try:
			self.bot.send_message(chat_id=chat_id, text=text)
			return 'Mensaje de emergencia enviado'
		except:
			return 'Error al enviar mensaje de emergencia'

	def send_picture(self, image_path):
		try:
			self.bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
			return 'Fotografía enviada'
		except:
			return 'Error al enviar la fotografía'