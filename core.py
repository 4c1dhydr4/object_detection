
import os
from playsound import playsound
from gtts import gTTS
from googletrans import Translator
from imageai.Detection import ObjectDetection
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class Detector:
	def __init__(self, model_path, output_path):
		self.detector = ObjectDetection()
		self.detection = None
		self.detection_items = []
		self.translator = Translator()
		self.model_path = model_path
		self.output_path = output_path
		self.out_text = ''
		self.out_audio = None
		self.language = 'es'
		self.id = 0

		self.initialize()

	def initialize(self):
		self.detector.setModelTypeAsTinyYOLOv3()
		self.detector.setModelPath(self.model_path)
		self.detector.loadModel()

	def set_detection(self, input_path):
		self.detection = self.detector.detectObjectsFromImage(
			input_image=input_path, 
			output_image_path=self.output_path)
		self.detection_items = []
		self.out_text = ''
		for item in self.detection:
			text = self.translator.translate(item["name"], dest=self.language).text
			self.detection_items.append(item)
			self.out_text = self.out_text + ' ' + text

	def speake(self):
		tts = gTTS(text=self.out_text, lang=self.language)
		audio = './mp3/' + str(self.id) + '.mp3'
		tts.save(audio)
		playsound(audio)
		self.id = self.id + 1

frames = [
	'test01.jpg',
	'megan.jfif',
	'test45.jpg',
	'fruits.png',
	'animals.jpg',
]

model_path = "./models/yolo-tiny.h5"

det = Detector(model_path, "detection.jpg")
for frame in frames:
	det.set_detection('./input/' + frame)
	det.speake() 	
