from PyQt5 import QtWidgets
from MainForm import Ui_Form_Main
from EventController import EventController


class MainFormSlot(QtWidgets.QMainWindow, Ui_Form_Main):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_events()

    def init_events(self):
        self.pushButton_highLight.clicked.connect(self.button_clicked)
        self.pushButton_lowLight.clicked.connect(self.button_clicked)
        self.pushButton_oven.clicked.connect(self.button_clicked)
        self.pushButton_salonLight.clicked.connect(self.button_clicked)
        self.pushButton_backLight.clicked.connect(self.button_clicked)
        self.pushButton_engineLight.clicked.connect(self.button_clicked)

    def button_clicked(self):
        sender = self.sender()
        button_name = sender.objectName()

        event_controller = EventController()
        event_text = ''

        if button_name == "pushButton_highLight":
            event_text = event_controller.high_light()

        elif button_name == "pushButton_lowLight":
            event_text = event_controller.low_light()

        elif button_name == "pushButton_oven":
            event_text = event_controller.oven()

        elif button_name == "pushButton_salonLight":
            event_text = event_controller.salon_light()

        elif button_name == "pushButton_backLight":
            event_text = event_controller.back_light()

        elif button_name == "pushButton_engineLight":
            event_text = event_controller.engine_light()

        self.label.setText(event_text)
