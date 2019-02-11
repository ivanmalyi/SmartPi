class Event:
	__private_HIGH_LIGHT = 'high_light'
	__private_LOW_LIGHT = 'low_light'

	def select_status_event(self, button_name):
		if button_name == "pushButton_highLight":
			status_event = self.__private_HIGH_LIGHT
		elif button_name == "pushButton_lowLight":
			status_event = self.__private_LOW_LIGHT
		else:
			status_event = ''

		return status_event
