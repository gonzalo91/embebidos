import configparser

class Config():


	@staticmethod
	def get( section, param):		
		configuracion = configparser.ConfigParser()
		configuracion.read('env.cfg')			
		return configuracion[section][param]

		

		