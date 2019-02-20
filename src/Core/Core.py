import sys
sys.path.append("../Controller")
sys.path.append("../Form/MainForm")
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from PyQt5 import QtWidgets
from MainFormSlot import MainFormSlot

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

def initialize_ports():
	gpio.init()
	gpio.setcfg(port.PG6, gpio.OUTPUT)
	gpio.setcfg(port.PG7, gpio.OUTPUT)
	gpio.setcfg(port.PG9, gpio.OUTPUT)

	gpio.setcfg(port.PD1, gpio.OUTPUT)
	gpio.output(port.PD1, gpio.HIGH)
	print("PD1/n")
	sleep(2)
	gpio.output(port.PD1, gpio.LOW)

	gpio.setcfg(port.PE1, gpio.OUTPUT)
	gpio.output(port.PE1, gpio.HIGH)
	print("PE1/n")
	sleep(2)
	gpio.output(port.PE1, gpio.LOW)

	gpio.setcfg(port.PI1, gpio.OUTPUT)
	gpio.output(port.PI1, gpio.HIGH)
	print("PI1/n")
	sleep(2)
	gpio.output(port.PI1, gpio.LOW)

if __name__ == '__main__':

	initialize_ports()

#	try:
#		main()
#	except:
#		print(Exception.__traceback__)


