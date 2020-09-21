# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layer2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from layer2biranje import Ui_layer2biranje
import psycopg2

class Ui_Layer2(object):
    def layer2biranje(self):
        "za spremanje vrijednosti combo boxa"
        conn = psycopg2.connect(database="hds", user="postgres", password="slashh123", host="localhost", port="5432")
        a=int(self.comboBox.currentText())
        naredba=str('UPDATE layer SET num_spine_leaf=%s WHERE id=1;' % a)
        cursor = conn.cursor()
        cursor.execute(naredba)
        conn.commit()
        
        "za prelazak na iduci dialog prilikom pritiska next buttona"
        
        self.dialog1=QtWidgets.QDialog()
        self.ui=Ui_layer2biranje()
        
        self.ui.setupUi(self.dialog1)
        
     
        self.dialog1.show()
    def spinBox1(self):
        conn = psycopg2.connect(database="hds", user="postgres", password="slashh123", host="localhost", port="5432")
        d=self.spinBox.value()
        naredba=str('UPDATE layer SET "num_spine_clusters/spines"=%s WHERE id=1;' % d)
        cursor = conn.cursor()
        cursor.execute(naredba)
        conn.commit()
    def spinBox2(self):
        conn = psycopg2.connect(database="hds", user="postgres", password="slashh123", host="localhost", port="5432")
        d=self.spinBox_2.value()
        naredba=str('UPDATE layer SET num_leaf_clusters=%s WHERE id=1;' % d)
        cursor = conn.cursor()
        cursor.execute(naredba)
        conn.commit()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(444, 294)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(33, 103, 339, 74))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 3, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 2, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(210, 230, 158, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.layoutWidget_2.setFont(font)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        self.pushButton.clicked.connect(self.layer2biranje)
        self.x=self.comboBox.currentText()
        self.spinBox.valueChanged.connect(self.spinBox1)
        self.spinBox_2.valueChanged.connect(self.spinBox2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose number of Spine CLusters:"))
        self.label_2.setText(_translate("Dialog", "Choose number of Leaf CLusters:"))
        self.label_3.setText(_translate("Dialog", "Choose number of Spine-Leaf interconnects :"))
        self.comboBox.setItemText(0, _translate("Dialog", "1"))
        self.comboBox.setItemText(1, _translate("Dialog", "2"))
        self.comboBox.setItemText(2, _translate("Dialog", "3"))
        self.pushButton_2.setText(_translate("Dialog", "Previous"))
        self.pushButton.setText(_translate("Dialog", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Layer2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

