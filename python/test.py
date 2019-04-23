import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
servo = GPIO.PWM(15,50)

servo.start(0.1)
time.sleep(0.5)
servo.ChangeDutyCycle((0.7*200)/20)

try:
    while True:
        grados = float(input("Introduzca grados entre 0 y 180 "))
        
        if grados <= 90:
            Nms = grados*0.01+0.6
            dc=(Nms*100)/20
            servo.ChangeDutyCycle(dc)
        elif grados <= 180:
            Nms = grados*0.0105+0.6
            dc=(Nms*100)/20
            servo.ChangeDutyCycle(dc)
        else:
            print('escribe bien puto')
                                               
except KeyboardInterrupt:
    servo.stop()
finally:
    GPIO.cleanup()
