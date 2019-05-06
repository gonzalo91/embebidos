from time import sleep
#import RPi.GPIO as GPIO

freeSlots     = [22,29,31,33,35,37]
baseSlots     = [22]
#freeSlots     = [22]
takenSlots    = []

CNYEntrada    = 11
CNYSalida     = 13

#GPIO.setup(CNYEntrada, GPIO.IN)
#GPIO.setup(CNYSalida, GPIO.IN)

#for sensor in freeSlots:
    #GPIO.setup(sensor, GPIO.IN)


#if (GPIO.input(CNYEntrada) == False or GPIO.input(CNYEntrada) == 0):
#   pass

print('+-------------------------+')
print('|   1   |    2   |    3   |')
print('|   %d  |    %d  |    %d  |' % (freeSlots[0],  freeSlots[1], freeSlots[2]))
print('<-  S (%d)           <-   |' % CNYEntrada)
print('|__________________       |')
print('|                  |      |')
print('|__________________|      |')
print('->  E (%d)           ->   |' %CNYSalida)
print('|   %d  |   %d   |   %d   |' % (freeSlots[3],  freeSlots[4], freeSlots[5]))
print('|   R   |    R   |    R   |')
print('+-------------------------+')

