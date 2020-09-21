# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dijalog1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


from layer2 import Ui_Layer2
from layer3 import Ui_Layer3
class Ui_Dialog(object):
    def opendialog(self):
        self.dialog1=QtWidgets.QDialog()
        self.ui=Ui_Layer2()
        self.ui.setupUi(self.dialog1) 
        Dialog.hide()
        self.dialog1.show()
    
    def opendialog2(self):
        self.dialog2=QtWidgets.QDialog()
        self.ui=Ui_Layer3()
        self.ui.setupUi(self.dialog2)
        Dialog.hide()
        self.dialog2.show()
     
     
    def zalayer2(self):
        self.pushButton.clicked.connect(self.opendialog)
    def zalayer3(self):
        self.pushButton.clicked.connect(self.opendialog2)
		
		
		
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(324, 264)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 50, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 100, 211, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        "odavde"
        
        self.radioButton.toggled.connect(self.zalayer2)
        self.radioButton_2.toggled.connect(self.zalayer3)
		

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose L2 or L3 Fabric:"))
        self.radioButton.setText(_translate("Dialog", "Layer 2"))
        self.radioButton_2.setText(_translate("Dialog", "Layer 3"))
        self.pushButton.setText(_translate("Dialog", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

