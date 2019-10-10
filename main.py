from core import Detector
from assistant import Assistant

frames = [
	'test01.jpg',
	'megan.jfif',
	'test45.jpg',
	'fruits.png',
	'animals.jpg',
]
LANGUAGE = 'es'

megan = Assistant(name='Megan', user_name='Luis', language=LANGUAGE)
megan.speake(megan.say_hi() + ';' + megan.say_my_name() + ';' + megan.main_menu())

det = Detector(
	"./models/yolo-tiny.h5", 
	"detection.jpg", language=LANGUAGE, 
	translator=megan.translator)
det.initialize()

for frame in frames:
	detection_text = det.get_detection('./input/' + frame)
	megan.speake(detection_text)
