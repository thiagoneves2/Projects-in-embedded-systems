import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

pino_led = 18

GPIO.setup(pino_led,GPIO.OUT)

try :
	while True:
		GPIO.output(pino_led,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(pino_led, GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
	print("Programa encerrado pelo usuário")
finally:
	GPIO.cleanup()
