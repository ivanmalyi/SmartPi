from pyA20.gpio import gpio
from pyA20.gpio import port
import os


class EventController:

	__private_on = 'Включен'
	__private_off = 'Выключен'
	__private_high_light_text = ' дальний свет'
	__private_low_light_text = ', ближний свет'
	__private_oven = ' обогреватель'
	__private_salon_light = ' свет в салоне'
	__private_back_light = ' свет в багажнике'
	__private_engine_light = ' свет под капотом'

	def high_light(self):
		pg9 = gpio.input(port.PG9)

		if pg9 == gpio.LOW:
			gpio.output(port.PG9, gpio.HIGH)
			gpio.output(port.PG7, gpio.LOW)
			button_text = self.__private_off+self.__private_high_light_text
			os.system("mpg327 ../../files/sound/on_high_light.mp3 -quiet")
		else:
			gpio.output(port.PG9, gpio.LOW)
			button_text = self.__private_on + self.__private_high_light_text
			os.system("mpg327 ../../files/sound/off_high_light.mp3 -quiet")

		return button_text

	def low_light(self):
		pg7 = gpio.input(port.PG7)

		if pg7 == gpio.LOW:
			gpio.output(port.PG7, gpio.HIGH)
			gpio.output(port.PG9, gpio.LOW)
			button_text = self.__private_off + self.__private_low_light_text
			os.system("mpg327 ../../files/sound/low_on_light.mp3 -quiet")
		else:
			gpio.output(port.PG7, gpio.LOW)
			button_text = self.__private_on + self.__private_low_light_text
			os.system("mpg327 ../../files/sound/off_low_light.mp3 -quiet")

		return button_text

	def oven(self):
		pg6 = gpio.input(port.PG6)

		if pg6 == gpio.LOW:
			gpio.output(port.PG6, gpio.HIGH)
			button_text = self.__private_on + self.__private_oven
			os.system("mpg327 ../../files/sound/ -quiet")
		else:
			gpio.output(port.PG6, gpio.LOW)
			button_text = self.__private_off + self.__private_oven
			os.system("mpg327 ../../files/sound/ -quiet")

		return button_text

	def salon_light(self):
		pg3 = gpio.input(port.PG3)

		if pg3 == gpio.LOW:
			gpio.output(port.PG3, gpio.HIGH)
			button_text = self.__private_on + self.__private_salon_light
			os.system("mpg327 ../../files/sound/ -quiet")
		else:
			gpio.output(port.PG3, gpio.LOW)
			button_text = self.__private_off + self.__private_salon_light
			os.system("mpg327 ../../files/sound/ -quiet")

		return button_text

	def back_light(self):
		pg4 = gpio.input(port.PG4)

		if pg4 == gpio.LOW:
			gpio.output(port.PG4, gpio.HIGH)
			button_text = self.__private_on + self.__private_back_light
			os.system("mpg327 ../../files/sound/ -quiet")
		else:
			gpio.output(port.PG4, gpio.LOW)
			button_text = self.__private_off + self.__private_back_light
			os.system("mpg327 ../../files/sound/ -quiet")

		return button_text

	def engine_light(self):
		pg5 = gpio.input(port.PG5)

		if pg5 == gpio.LOW:
			gpio.output(port.PG5, gpio.HIGH)
			button_text = self.__private_on + self.__private_back_light
			os.system("mpg327 ../../files/sound/ -quiet")
		else:
			gpio.output(port.PG5, gpio.LOW)
			button_text = self.__private_off + self.__private_back_light
			os.system("mpg327 ../../files/sound/ -quiet")

		return button_text
