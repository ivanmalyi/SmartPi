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
        Form_Main.resize(1280, 818)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_Main.sizePolicy().hasHeightForWidth())
        Form_Main.setSizePolicy(sizePolicy)
        Form_Main.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.pushButton_highLight = QtWidgets.QPushButton(Form_Main)
        self.pushButton_highLight.setGeometry(QtCore.QRect(170, 80, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_highLight.setFont(font)
        self.pushButton_highLight.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../files/img/lightbulb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_highLight.setIcon(icon)
        self.pushButton_highLight.setCheckable(True)
        self.pushButton_highLight.setAutoExclusive(False)
        self.pushButton_highLight.setObjectName("pushButton_highLight")
        self.pushButton_lowLight = QtWidgets.QPushButton(Form_Main)
        self.pushButton_lowLight.setGeometry(QtCore.QRect(540, 80, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_lowLight.setFont(font)
        self.pushButton_lowLight.setObjectName("pushButton_lowLight")
        self.label = QtWidgets.QLabel(Form_Main)
        self.label.setGeometry(QtCore.QRect(220, 10, 741, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_oven = QtWidgets.QPushButton(Form_Main)
        self.pushButton_oven.setGeometry(QtCore.QRect(900, 80, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_oven.setFont(font)
        self.pushButton_oven.setObjectName("pushButton_oven")
        self.pushButton_saloneLight = QtWidgets.QPushButton(Form_Main)
        self.pushButton_saloneLight.setGeometry(QtCore.QRect(160, 230, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_saloneLight.setFont(font)
        self.pushButton_saloneLight.setObjectName("pushButton_saloneLight")
        self.pushButton_backLight = QtWidgets.QPushButton(Form_Main)
        self.pushButton_backLight.setGeometry(QtCore.QRect(540, 230, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_backLight.setFont(font)
        self.pushButton_backLight.setObjectName("pushButton_backLight")
        self.pushButton_engineLight = QtWidgets.QPushButton(Form_Main)
        self.pushButton_engineLight.setGeometry(QtCore.QRect(900, 230, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_engineLight.setFont(font)
        self.pushButton_engineLight.setObjectName("pushButton_engineLight")

        self.retranslateUi(Form_Main)
        QtCore.QMetaObject.connectSlotsByName(Form_Main)

    def retranslateUi(self, Form_Main):
        _translate = QtCore.QCoreApplication.translate
        Form_Main.setWindowTitle(_translate("Form_Main", "SmartPi"))
        self.pushButton_highLight.setText(_translate("Form_Main", "дальний свет"))
        self.pushButton_lowLight.setText(_translate("Form_Main", "ближний свет"))
        self.label.setText(_translate("Form_Main", "Off"))
        self.pushButton_oven.setText(_translate("Form_Main", "обогреватель"))
        self.pushButton_saloneLight.setText(_translate("Form_Main", "свет в салоне"))
        self.pushButton_backLight.setText(_translate("Form_Main", "свет в багажнике"))
        self.pushButton_engineLight.setText(_translate("Form_Main", "свет под капотом"))

