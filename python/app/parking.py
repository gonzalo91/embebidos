from time import sleep

from .Config import Config


class Parking:

	maxSpaces = Config.get('Default', 'maxspaces')

	current

	ledRojo    = 0
	ledNaranja = 1
	ledVerde   = 0

	sensorEntrada = 'sensorEntrada'
	sensorSalida  = 'sensorSalida'



	def __init__(self):		
		self.run()


	def run(self):
		while(True):
			print(self.ledVerde)
			sleep(2)



	def entry(self):
		pass
		

	def freeParkingSpaces(self):
		pass

	def exit(self):
		pass


	def sayHello(self):
		print('Hola kbron')