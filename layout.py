# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 254)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 581, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.kebebSpin = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.kebebSpin.setObjectName("kebebSpin")
        self.gridLayout.addWidget(self.kebebSpin, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setStyleSheet("font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.kremowkaSpin = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.kremowkaSpin.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kremowkaSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.kremowkaSpin.setObjectName("kremowkaSpin")
        self.gridLayout.addWidget(self.kremowkaSpin, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setStyleSheet("font-weight: bold;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.kremowkaSum = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.kremowkaSum.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kremowkaSum.setObjectName("kremowkaSum")
        self.gridLayout.addWidget(self.kremowkaSum, 0, 3, 1, 1)
        self.kebebPrice = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.kebebPrice.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kebebPrice.setObjectName("kebebPrice")
        self.gridLayout.addWidget(self.kebebPrice, 1, 2, 1, 1)
        self.kremowkaPrice = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.kremowkaPrice.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kremowkaPrice.setObjectName("kremowkaPrice")
        self.gridLayout.addWidget(self.kremowkaPrice, 0, 2, 1, 1)
        self.kebebSum = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.kebebSum.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kebebSum.setObjectName("kebebSum")
        self.gridLayout.addWidget(self.kebebSum, 1, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Kula mocy"))
        self.label.setText(_translate("Dialog", "Kremówki"))
        self.kremowkaSum.setPlaceholderText(_translate("Dialog", "razem"))
        self.kebebPrice.setPlaceholderText(_translate("Dialog", "cena za kilogram"))
        self.kremowkaPrice.setPlaceholderText(_translate("Dialog", "podaj cenę za sztukę"))
        self.kebebSum.setPlaceholderText(_translate("Dialog", "razem"))