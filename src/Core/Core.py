from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from PyQt5 import QtWidgets
from MainFormSlot import MainFormSlot
import sys

#gpio.init()
#gpio.setcfg(port.PG7, gpio.OUTPUT)

#i = 0
#while True:
#	gpio.output(port.PG7, gpio.HIGH)
#	sleep(1)

#	gpio.output(port.PG7, gpio.LOW)
#	sleep(1)

#	if i > 10:
#		break
#	i += 1


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = MainFormSlot()

	window.show()
	app.exec_()


if __name__ == '__main__':
	main()
