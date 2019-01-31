from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from datetime import datetime
# Импортируем класс интерфейса из созданного конвертером модуля
from test_ui import Ui_Form


# Создаём собственный класс, наследуясь от автоматически сгенерированного
class MainWindowSlots(Ui_Form):

	# Определяем пользовательский слот
	def set_time(self):
		# Получаем текущую метку времени в формате 'Ч:М:С'
		str_time = datetime.now().strftime('%H:%M:%S')
		# Присваиваем надписи на кнопке метку времени
		self.pushButton.setText(str_time)
		return None


gpio.init()
gpio.setcfg(port.PG7, gpio.OUTPUT)

i = 0
while True:
	gpio.output(port.PG7, gpio.HIGH)
	sleep(1)

	gpio.output(port.PG7, gpio.LOW)
	sleep(1)

	if i > 10:
		break
	i += 1
