from PyQt5 import QtWidgets
from MainForm import Ui_Form_Main
from EventController import EventController
from Event import Event


class MainFormSlot(QtWidgets.QMainWindow, Ui_Form_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_events()

    def init_events(self):
        self.pushButton_highLight.clicked.connect(self.button_clicked)
        self.pushButton_lowLight.clicked.connect(self.button_clicked)

    def button_clicked(self):
        sender = self.sender()
        button_name = sender.objectName()

        event = Event()
        status_event = event.select_status_event(button_name)
        event_controller =  EventController()
        if status_event == 'high_light':
            button_text = event_controller.high_light()
            self.pushButton_highLight.setText(button_text)

        elif status_event == 'low_light':
            button_text = event_controller.low_light()
            self.pushButton_lowLight.setText(button_text)

        self.label.setText(sender.objectName())
