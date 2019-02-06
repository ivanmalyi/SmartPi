# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Main(object):
    def setupUi(self, Form_Main):
        Form_Main.setObjectName("Form_Main")
        Form_Main.resize(400, 300)
        Form_Main.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.pushButton_highLight = QtWidgets.QPushButton(Form_Main)
        self.pushButton_highLight.setGeometry(QtCore.QRect(30, 60, 111, 27))
        self.pushButton_highLight.setAutoFillBackground(False)
        self.pushButton_highLight.setObjectName("pushButton_highLight")
        self.pushButton_lowLight = QtWidgets.QPushButton(Form_Main)
        self.pushButton_lowLight.setGeometry(QtCore.QRect(230, 60, 111, 27))
        self.pushButton_lowLight.setObjectName("pushButton_lowLight")
        self.progressBar_brightnesLight = QtWidgets.QProgressBar(Form_Main)
        self.progressBar_brightnesLight.setGeometry(QtCore.QRect(140, 210, 118, 23))
        self.progressBar_brightnesLight.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar_brightnesLight.setMaximum(104)
        self.progressBar_brightnesLight.setProperty("value", 80)
        self.progressBar_brightnesLight.setObjectName("progressBar_brightnesLight")
        self.label = QtWidgets.QLabel(Form_Main)
        self.label.setGeometry(QtCore.QRect(110, 130, 161, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")


        self.retranslateUi(Form_Main)
        QtCore.QMetaObject.connectSlotsByName(Form_Main)

    def retranslateUi(self, Form_Main):
        _translate = QtCore.QCoreApplication.translate
        Form_Main.setWindowTitle(_translate("Form_Main", "SmartPi"))
        self.pushButton_highLight.setText(_translate("Form_Main", "Дальний свет"))
        self.pushButton_lowLight.setText(_translate("Form_Main", "Ближний свет"))
        self.label.setText(_translate("Form_Main", "Off"))

