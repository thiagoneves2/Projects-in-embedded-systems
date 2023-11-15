from gpiozero import DistanceSensor, LED
from time import sleep

#define-se os pinos do echo e do trigger
sensor = DistanceSensor(23,24)

#é printada a distância do objeto até o sensor ultrasônico
while True:
	print('Distancia do objeto mais proximo: ',sensor.distance, 'm')
	sleep(1)
