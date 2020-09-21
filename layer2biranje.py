# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layer3biranje.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import psycopg2



class Ui_layer2biranje(QWidget):
    def showMessageBox(self):
        print('error')
        
        
    def Button1(self):
        
        
        "provjera"
        if self.result_for_spines[0]<=self.i:
            QMessageBox().warning(self,"Error", "Unijeli ste previse", QMessageBox.Ok),
            return False
        
        "spremanje svakog pojedinog odabira u bazu podataka(spineove)"
        
        
        odabir=self.comboBox.currentText()
        if odabir == "NRU 01":
            "prvo dohvacamo vrijednost iz baze i uvecavamo za 1"
            
            naredba1=str('SELECT "NRU 01" FROM vrsta WHERE id=1;')
            cursor1 = self.conn.cursor()
            cursor1.execute(naredba1)
            before=cursor1.fetchone()
            a=before[0]+1
            
            "zatim je spremamo"
            
            naredba2=str('UPDATE vrsta SET "NRU 01" = %s WHERE id=1;'% a)
            cursor=self.conn.cursor()
            cursor.execute(naredba2)
            self.conn.commit()
        elif odabir == "NSU":
            
            naredba1=str('SELECT "NSU" FROM vrsta WHERE id=1;')
            cursor1 = self.conn.cursor()
            cursor1.execute(naredba1)
            before=cursor1.fetchone()
            b=before[0]+1
            
            naredba2=str('UPDATE vrsta SET "NSU" =%s WHERE id=1;'% b)
            cursor=self.conn.cursor()
            cursor.execute(naredba2)
            self.conn.commit()
        elif odabir == "NRU 02":
            naredba1=str('SELECT "NRU 02" FROM vrsta WHERE id=1;')
            cursor1 = self.conn.cursor()
            cursor1.execute(naredba1)
            before=cursor1.fetchone()
            c=before[0]+1
            
            
            naredba2=str('UPDATE vrsta SET "NRU 02" =%s WHERE id=1;'% c)
            cursor=self.conn.cursor()
            cursor.execute(naredba2)
            self.conn.commit()
        
        
       
        
        #if self.result_for_spines[0]==self.i+1:
           # text=str('Chose the type of the %s spine\spine cluster:' % self.x[self.i-1])
            #self.label.setText(text)
        #else:
        text=str('Chose the type of the %s spine cluster:' % self.x[self.i])
        self.label.setText(text)
        self.i=self.i+1
        
        
        
        
            	
            
        
        
        
       
       
        
            
    def Button2(self):
       
        if self.result_for_leafes[0]<=self.i2:
            QMessageBox().warning(self,"Error", "Unijeli ste previse", QMessageBox.Ok)
            return False
         
        "spremanje svakog pojedinog odabira u bazu podataka(leafove)"
        
        odabir=self.comboBox_2.currentText()
        if odabir == "NRU 01":
            "prvo dohvacamo vrijednost iz baze i uvecavamo za 1"
            
            naredba1=str('SELECT "NRU 01" FROM vrsta WHERE id=2;')
            cursor1 = self.conn.cursor()
            cursor1.execute(naredba1)
            before=cursor1.fetchone()
            a=before[0]+1
            
            "zatim je spremamo"
            
            naredba2=str('UPDATE vrsta SET "NRU 01" = %s WHERE id=2;'% a)
            cursor=self.conn.cursor()
            cursor.execute(naredba2)
            self.conn.commit()
        elif odabir == "NSU":
            
            naredba1=str('SELECT "NSU" FROM vrsta WHERE id=2;')
            cursor1 = self.conn.cursor()
            cursor1.execute(naredba1)
            before=cursor1.fetchone()
            b=before[0]+1
            
            naredba2=str('UPDATE vrsta SET "NSU" =%s WHERE id=2;'% b)
            cursor=self.conn.cursor()
            cursor.execute(naredba2)
            self.conn.commit()
        elif odabir == "NRU 02":
            naredba1=str('SELECT "NRU 02" FROM vrsta WHERE id=2;')
            cursor1 = self.conn.cursor()
            cursor1.execute(naredba1)
            before=cursor1.fetchone()
            c=before[0]+1
            
            
            naredba2=str('UPDATE vrsta SET "NRU 02" =%s WHERE id=2;'% c)
            cursor=self.conn.cursor()
            cursor.execute(naredba2)
            self.conn.commit()
        
        
        
    
        text=str('Chose the type of the %s leaf cluster:' % self.x[self.i2])
        self.label_2.setText(text)
        self.i2=self.i2+1
        
        
        
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(444, 294)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 220, 158, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 221, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 221, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 140, 91, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 50, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 140, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.retranslateUi(Dialog)
        self.label.setText("Chose the type of the 1st spine cluster:")
        self.label_2.setText("Chose the type of the 1st leaf cluster:")
        self.dialog1=QtWidgets.QDialog()
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        
        "konekcija za bazu"
        
        self.conn = psycopg2.connect(database="hds", user="postgres", password="slashh123", host="localhost", port="5432")
        
        "postavljanje vrijednosti u bazi na 0 da se nebi uzimale vrijednosti od prijasnjih puta"
        i=["NRU 01","NSU","NRU 02"]
        for j in range (0,3):
            naredba=str('UPDATE vrsta SET "%s"=0;'% i[j])
            cursor=self.conn.cursor()
            cursor.execute(naredba)
            self.conn.commit()
            
        
        
        
        "pristupanje bazi za dobivanje broja spineova"
        
        naredba1=str('SELECT "num_spine_clusters/spines" FROM layer WHERE id=1;')
        cursor1 = self.conn.cursor()
        cursor1.execute(naredba1)
        self.result_for_spines=cursor1.fetchone()
        
        "pristupanje bazi za dobivanje broja leafova"
        
        naredba2=str('SELECT num_leaf_clusters FROM layer WHERE id=1;')
        cursor2 = self.conn.cursor()
        cursor2.execute(naredba2)
        self.result_for_leafes=cursor2.fetchone()
        
        
        
        "brojaci za odabir ovo 1st 2nd,.."
        self.i=0
        self.i2=0
        self.x=["2nd","3rd","4th","5th","6th","7th","8th","9th","10th"]
        
        
        "akcije prilikon pritiska 1 i 2 botuna"
        self.pushButton_3.clicked.connect(self.Button1)
        self.pushButton_4.clicked.connect(self.Button2)
        
        
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Previous"))
        self.pushButton.setText(_translate("Dialog", "Next"))
        #self.label.setText(_translate("Dialog", "Chose the type of the 1st spine\spine cluster:"))
        self.comboBox.setItemText(0, _translate("Dialog", "NRU 01"))
        self.comboBox.setItemText(1, _translate("Dialog", "NRU 02"))
        self.comboBox.setItemText(2, _translate("Dialog", "NSU"))
        #self.label_2.setText(_translate("Dialog", "Chose the type of the 1st leaf cluster:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "NRU 01"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "NRU 02"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "NSU"))
        self.pushButton_3.setText(_translate("Dialog", "OK"))
        self.pushButton_4.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_layer2biranje()
    ui.setupUi(Dialog)
    Dialog.show()

    sys.exit(app.exec_())

