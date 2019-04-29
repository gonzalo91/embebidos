from time import sleep
import RPi.GPIO as GPIO
import requests


from .Config import Config


class Parking:

    maxSpaces = int(Config.get('Default', 'maxspaces'))

    url       = Config.get('Default', 'apiSave')
    
    currentSpaces = 0   

    CNYEntrada    = 11
    servoEntrada  = 15
    CNYSalida     = 13
    servoSalida   = 7
    ledVerdeIn    = 16
    ledAmarillo   = 12
    ledRojo       = 18
    ledVerdeOut   = 32
    #freeSlots    = [22,29,31,33,35,37]
    baseSlots     = [22]
    freeSlots     = [22]
    takenSlots    = []
    



    def __init__(self): 
        self.setUp()    
        self.run()


    def setUp(self):
        GPIO.setmode(GPIO.BOARD)

        #Led's
        GPIO.setup(self.ledVerdeOut, GPIO.OUT)        
        GPIO.setup(self.ledVerdeIn, GPIO.OUT)
        GPIO.setup(self.ledAmarillo, GPIO.OUT)
        GPIO.setup(self.ledRojo, GPIO.OUT)        
    
        
        #Sensores Entrada y salida
        GPIO.setup(self.CNYEntrada, GPIO.IN)
        GPIO.setup(self.CNYSalida, GPIO.IN)




        #Servo de entrada
        GPIO.setup(self.servoEntrada, GPIO.OUT)
        self.servoEntrada = GPIO.PWM(self.servoEntrada,50)
        self.servoEntrada.start(0.1)
        sleep(0.5)
        self.servoEntrada.ChangeDutyCycle((0.7*200)/20)

        #Servo de salida
        # GPIO.setup(self.servoSalida, GPIO.OUT)
        # self.servoSalida = GPIO.PWM(self.servoSalida,50)
        # self.servoSalida.start(0.1)
        # sleep(0.5)
        # self.servoSalida.ChangeDutyCycle((0.7*200)/20)


        #Sensores de pariking
        for sensor in self.freeSlots:
            GPIO.setup(sensor, GPIO.IN)



        self.turnOn(self.ledAmarillo)





    def run(self):
        while(True):
            self.entry()
            sleep(1)
            self.exit()




    def entry(self):
        if (GPIO.input(self.CNYEntrada) == False or GPIO.input(self.CNYEntrada) == 0):
            if self.thereAreAvailableSpaces():
                self.turnOn(self.ledVerdeIn)
                self.turnOff(self.ledAmarillo)              
                self.openServo(self.servoEntrada)
                # Peticion HTTP
                # self.sendNewentry()
                sleep(5)
                self.turnOn(self.ledAmarillo)
                self.turnOff(self.ledVerdeIn)
                self.currentSpaces += 1
                self.closeServo(self.servoEntrada)
            else:
                self.rejectEntry()

    def exit(self):
        if (GPIO.input(self.CNYSalida) == False or GPIO.input(self.CNYSalida) == 0):
            self.currentSpaces-=1
            self.turnOn(self.ledVerdeOut)
            #self.openServo(self.servoSalida)
            sleep(3)
            #self.sendNewOutput()            
            self.turnOff(self.ledVerdeOut)            
            #self.closeServo(self.servoSalida)
        
    def getSensor(self, port):
        return self.baseSlots.index(port) + 1 


    def sendNewOutPut(self):
        finded = False
        attempts = 0

        while (attempts < 3 and not finded):
            for i,sensor in enumerate(self.takenSlots ):
                if( GPIO.input(sensor) and (sensor not in self.freeSlots)):
                    taken = self.takenSlots.pop(i)
                    self.freeSlots.append(taken)
                    finded = True
                    break #OMG
            attempts += 1

        if not finded: 
            taken = self.takenSlots.pop()
            self.freeSlots.append(taken)
            
        sensor = self.getSensor(taken)
            
        req = requests.post('http://gacr.com.mx/update-data', data = {'sensor': sensor, 'estatus' : 0}, timeout=5)



    def sendNewEntry(self):
        finded = False
        attempts = 0

        while (attempts < 3 and not finded):
            for i,sensor in enumerate(self.freeSlots ):
                if( not GPIO.input(sensor) and (sensor not in self.takenSlots)):
                    taken = self.freeSlots.pop(i)
                    self.takenSlots.append(taken)
                    finded = True
                    break #OMG
            attempts += 1

        if not finded: 
            taken = self.freeSlots.pop()
            self.takenSlots.append(taken)
            
        sensor = self.getSensor(taken)
            
        req = requests.post('http://gacr.com.mx/update-data', data = {'sensor': sensor, 'estatus' : 1}, timeout=5)



    def rejectEntry(self):
        self.turnOff(self.ledAmarillo)
        self.turnOn(self.ledRojo)
        sleep(3)
        self.turnOff(self.ledRojo)
        self.turnOn(self.ledAmarillo)





    def thereAreAvailableSpaces(self):
        return self.currentSpaces < self.maxSpaces

    def openServo(self, servo):
    	Nms = 115*0.0105+0.6
        dc=(Nms*100)/20
        servo.ChangeDutyCycle(dc)

    def closeServo(self, servo):
    	Nms = 10*0.01+0.6
        dc=(Nms*100)/20
        servo.ChangeDutyCycle(dc)



                

    


    def sayHello(self):
        print('Hola kbron')

    def turnOn(self, gpio):
        GPIO.output(gpio, True)


    def turnOff(self, gpio):
        GPIO.output(gpio, False)