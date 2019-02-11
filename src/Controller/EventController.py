from pyA20.gpio import gpio
from pyA20.gpio import port
import os


class EventController:

	__private_on = 'Включен'
	__private_off = 'Выключен'
	__private_high_light_text = ' дальний свет'
	__private_low_light_text = ', ближний свет'

	def high_light(self):

		pg7 = gpio.input(port.PG7)
		if pg7 == gpio.LOW:
			gpio.output(port.PG7, gpio.HIGH)
			gpio.output(port.PG6, gpio.LOW)
			button_text = self.__private_off+self.__private_high_light_text
			os.system("mpg321 ../../sound/on_high_light.mp3 -quiet")
		else:
			gpio.output(port.PG7, gpio.LOW)
			button_text = self.__private_on + self.__private_high_light_text
			os.system("mpg321 ../../sound/off_high_light.mp3 -quiet")

		return button_text

	def low_light(self):

		pg6 = gpio.input(port.PG6)
		if pg6 == gpio.LOW:
			gpio.output(port.PG6, gpio.HIGH)
			gpio.output(port.PG7, gpio.LOW)
			button_text = self.__private_off + self.__private_low_light_text
			os.system("mpg321 ../../sound/low_on_light.mp3 -quiet")
		else:
			gpio.output(port.PG6, gpio.LOW)
			button_text = self.__private_on + self.__private_low_light_text
			os.system("mpg321 ../../sound/off_low_light.mp3 -quiet")

		return button_text
