from googletrans import Translator
from gtts import gTTS

t = Translator()

text = t.translate('Precione el primer botón para recibir asistencia en Español', dest='es').text
tts = gTTS(text=text, lang='es')
tts.save('./mp3/lang_es.mp3')

text = t.translate('Precione el primer botón para recibir asistencia en Inglés', dest='en').text
tts = gTTS(text=text, lang='en')
tts.save('./mp3/lang_en.mp3')

text = t.translate('Precione el primer botón para recibir asistencia en Francés', dest='fr').text
tts = gTTS(text=text, lang='fr')
tts.save('./mp3/lang_fr.mp3')

text = t.translate('Precione el primer botón para recibir asistencia en Alemán', dest='de').text
tts = gTTS(text=text, lang='de')
tts.save('./mp3/lang_de.mp3')