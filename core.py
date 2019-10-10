
import os
from imageai.Detection import ObjectDetection

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'

class Detector:
	def __init__(self, model_path, output_path, language, translator):
		self.detector = None
		self.detection = None
		self.detection_items = []
		self.model_path = model_path
		self.output_path = output_path
		self.detection_text = ''
		self.out_audio = None
		self.id = 0
		self.language = language
		self.translator = translator

	def initialize(self):
		self.detector = ObjectDetection()
		self.detector.setModelTypeAsTinyYOLOv3()
		self.detector.setModelPath(self.model_path)
		self.detector.loadModel()

	def get_detection(self, input_path):
		self.detection = self.detector.detectObjectsFromImage(
			input_image=input_path, 
			output_image_path=self.output_path)
		self.detection_items = []
		self.detection_text = ''
		for item in self.detection:
			text = self.translator.translate(item["name"], dest=self.language).text
			self.detection_items.append(item)
			self.detection_text = self.detection_text + ' ' + text
		return self.detection_text
