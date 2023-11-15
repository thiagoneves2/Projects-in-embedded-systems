from gpiozero import DistanceSensor, LED
from signal import pause
import time

#define-se os pinos trigger e echo
sensor = DistanceSensor(23,24)
#define-se o pino do LED
led = LED(16)

#aqui é definido que quando há um objeto no alcance o led acende
sensor.when_in_range = led.on

#quando o objeto não está no range (alcance) o led apaga
sensor.when_out_of_range = led.off
pause()
