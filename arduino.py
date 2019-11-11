import serial
import time

class R2D2:
	def __init__(self):
		self.r2d2 = None
		self.init()

	def init(self):
		port = self.available_ports()[0]
		if port:
			self.r2d2 = serial.Serial(port, 9600)
			self.r2d2.close()
		else:
			print('No port available')

	def get_input(self):
		# self.init()
		self.r2d2.open()
		print('Ingrese una opción:')
		opt = '0'
		while opt == '0':
			line = self.r2d2.readline()
			try:
				linedec = line.decode()
				opt = linedec[0:len(linedec)-2]
			except:
				opt = '0'
		print(opt)
		self.r2d2.close()
		return opt

	def available_ports(self):
		import sys
		from serial.tools import list_ports
		coms = []
		if sys.platform == 'win32':
			coms = [item.device for item in list_ports.comports()]
		elif sys.platform == 'linux':
			coms = [item[0] for item in list_ports.comports()]
		if len(coms) > 0:
			return coms
		return False
