from pyA20.gpio import gpio
from pyA20.gpio import port
from PyQt5 import QtWidgets
import random


class EventController():

	def high_light(self):
		rand = random.randint(0, 1)
		#pg7 = gpio.input(port.PG7)
		if rand == 0:#pg7 == gpio.LOW:
			#gpio.output(port.PG7, gpio.HIGH)
			print(rand)
		else:
			#gpio.output(port.PG7, gpio.LOW)
			print(rand)

		return rand#gpio.input(port.PG7)
