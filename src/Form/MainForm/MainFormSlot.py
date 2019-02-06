from PyQt5 import QtWidgets
from MainForm import Ui_Form_Main


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
        self.label.setText(sender.text())
