from time import sleep
import RPi.GPIO as GPIO

from .Config import Config


class Parking:

    maxSpaces = int(Config.get('Default', 'maxspaces'))
    
    currentSpaces = 0   

    CNYEntrada    = 11
    servoEntrada  = 15
    CNYSalida     = 13
    servoSalida   = 7
    ledVerde      = 16
    ledAmarillo   = 12
    ledRojo       = 18



    def __init__(self): 
        self.setUp()    
        self.run()


    def setUp(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ledVerde, GPIO.OUT)
        GPIO.setup(self.ledAmarillo, GPIO.OUT)
        GPIO.setup(self.ledRojo, GPIO.OUT)
        # GPIO.setup(self.servoEntrada, GPIO.OUT)
        # GPIO.setup(self.servoSalida, GPIO.OUT)
        GPIO.setup(self.CNYEntrada, GPIO.IN)
        GPIO.setup(self.CNYSalida, GPIO.IN)
        self.turnOn(self.ledAmarillo)





    def run(self):
        while(True):
            self.entry()
            sleep(1)
            self.exit()




    def entry(self):
        if (GPIO.input(self.CNYEntrada) == False or GPIO.input(self.CNYEntrada) == 0):
            if self.thereAreAvailableSpaces():
                self.turnOn(self.ledVerde)
                self.turnOff(self.ledAmarillo)              
                # self.openServo(self.servoEntrada)
                # Peticion HTTP
                # self.sendNewentry()
                sleep(5)
                self.turnOn(self.ledAmarillo)
                self.turnOff(self.ledVerde)
                self.currentSpaces += 1
                #self.closeServo(self.servoEntrada)
            else:
                self.rejectEntry()

    def exit(self):
        if (GPIO.input(self.CNYSalida) == False or GPIO.input(self.CNYSalida) == 0):
            self.currentSpaces-=1
            #self.openServo(self.servoSalida)
            #sleep(5000)            
            #self.closeServo(self.servoSalida)
        
                



    def rejectEntry(self):
        self.turnOff(self.ledAmarillo)
        self.turnOn(self.ledRojo)
        sleep(3)
        self.turnOff(self.ledRojo)
        self.turnOn(self.ledAmarillo)





    def thereAreAvailableSpaces(self):
        return self.currentSpaces < self.maxSpaces
                

    


    def sayHello(self):
        print('Hola kbron')

    def turnOn(self, gpio):
        GPIO.output(gpio, True)


    def turnOff(self, gpio):
        GPIO.output(gpio, False)