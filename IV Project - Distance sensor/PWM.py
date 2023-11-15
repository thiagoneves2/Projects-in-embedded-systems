import RPi.GPIO as GPIO

import time

#Setando o tipo de numeração da placa
GPIO.setmode(GPIO.BCM)
#definindo o pino 20 como saída
GPIO.setup(20,GPIO.OUT)


#Definindo o pino 20 como PWM
pwm = GPIO.PWM(20,100)

#iniciando o pino 20 em 0
pwm.start(0)

#muda-se o duty cicle de 0 até 101, alterando-se assim o comprimento de onda do sinal
while True:
	for dc in range(101):
		pwm.ChangeDutyCycle(dc)
		#espera-se 0.2 segundos para continuar
		time.sleep(0.2)

