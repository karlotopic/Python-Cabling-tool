# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layer3biranje.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import psycopg2



class Ui_layer3biranje(QWidget):
    
    
		
    def showMessageBox(self):
        print('error')
    def btnNext(self):
        #spremamo u bazu odabire korisnika
		
        Nru_Nru=self.d
        Nsu_Nsu=self.e
        Nru02_Nru02=self.f
        
        Nru_Nru02=0
        Nru_Nsu=0
        Nru02_Nsu=0
        
        
      
        
        
        cursor=self.conn.cursor()
        
        "spremanje u bazu "
        naredba1=str('UPDATE vrsta SET "NRU 01" = %s,"NSU"=%s,"NRU 02"=%s WHERE id=1;'% (self.a,self.b, self.c))
        cursor.execute(naredba1)
        self.conn.commit()
        
        naredba2=str('UPDATE vrsta SET "NRU 01" = %s,"NSU"=%s,"NRU 02"=%s WHERE id=2;'% (self.d,self.e, self.f))
        cursor.execute(naredba2)
        self.conn.commit()
        #pomocu odabranih komponenata izracunavamo potrebnu kablažu
        
        "clusteri leafova(tj za izracunavanje kabela potrebnih za spajanje clustera u leafovima"
        Nru_Nru=self.d*2
        Nsu_Nsu=self.e*2
        Nru02_Nru02=self.f*2
        
        d=self.d
        e=self.e
        f=self.f
        
        
        "interconnections"
        if(self.a>0):
            for i in range(self.a):
           
                if(d>0):
                    for j in range(d):
                    
                        Nru_Nru=Nru_Nru+self.interconnects[0]*2
                    
                    
                    
            
                if(e>0):
                    for j in range(e):
                        Nru_Nsu=Nru_Nsu+self.interconnects[0]*2
                    
              
                
            
                if(f>0):
                    for j in range(f):
                        Nru_Nru02=Nru_Nru02+self.interconnects[0]*2
                    
                    
        if(self.b>0):
            for i in range(self.b):
                if(d>0):
                    for j in range(d):
                        Nru_Nsu=Nru_Nsu+self.interconnects[0]*2
                    
                    
                    
            
                if(e>0):
                    for j in range(e):
                        Nsu_Nsu=Nsu_Nsu+self.interconnects[0]*2
                    
              
                
            
                if(f>0):
                    for j in range(f):
                        Nru02_Nsu=Nru02_Nsu+self.interconnects[0]*2
           
            
        
        if(self.c>0):
            for i in range(self.c):
           
                if(d>0):
                    for j in range(d):
                        Nru_Nru02=Nru_Nru02+self.interconnects[0]*2
                    
                    
                    
            
                if(e>0):
                    for j in range(e):
                        Nru02_Nsu=Nru02_Nsu+self.interconnects[0]*2
                    
              
                
            
                if(f>0):
                    for j in range(f):
                        Nru02_Nru02=Nru02_Nru02+self.interconnects[0]*2        
            
        print(Nru_Nru,Nsu_Nsu,Nru02_Nru02,Nru_Nru02,Nru_Nsu,Nru02_Nsu)
            
    def Button1(self):
        
        
        "provjera"
        if self.result_for_spines[0]<=self.i:
            QMessageBox().warning(self,"Error", "Unijeli ste previse", QMessageBox.Ok),
            return False
        
        odabir=self.comboBox.currentText()
        if odabir == "NRU 01":
            self.a=self.a+1
            
        elif odabir == "NSU":
            self.b=self.b+1
            
        elif odabir == "NRU 02":
            self.c=self.c+1
            
        text=str('Chose the type of the %s spine\spine cluster:' % self.x[self.i])
        self.label.setText(text)
        self.i=self.i+1
        
        

    def Button2(self):
       
        if self.result_for_leafes[0]<=self.i2:
            QMessageBox().warning(self,"Error", "Unijeli ste previse", QMessageBox.Ok)
            return False
         
        odabir=self.comboBox_2.currentText()
        if odabir == "NRU 01":
            self.d=self.d+1    
        elif odabir == "NSU":
            self.e=self.e+1
        elif odabir == "NRU 02":
            self.f=self.f+1

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
        self.label.setText("Chose the type of the 1st spine\spine cluster:")
        self.label_2.setText("Chose the type of the 1st leaf cluster:")
        self.dialog1=QtWidgets.QDialog()
        QtCore.QMetaObject.connectSlotsByName(Dialog)
		
        
        
        
        "konekcija za bazu"
        
        self.conn = psycopg2.connect(database="hds", user="postgres", password="slashh123", host="localhost", port="5432")
        
        #postavljanje vrijednosti u bazi na 0 da se nebi uzimale vrijednosti od prijasnjih puta
        a=["NRU 01","NSU","NRU 02"]
        for j in range (0,3):
            naredba=str('UPDATE vrsta SET "%s"=0;'% a[j])
            cursor=self.conn.cursor()
            cursor.execute(naredba)
            self.conn.commit()
        #brojači odabira
        self.a=0
        self.b=0
        self.c=0
        self.d=0
        self.e=0
        self.f=0
        
        
        
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
        
        "pristupanje bazi za dobivanje broja interconnectsa"
        naredba3=str('SELECT num_spine_leaf FROM layer WHERE id=1;')
        cursor3=self.conn.cursor()
        cursor3.execute(naredba3)
        self.interconnects=cursor3.fetchone()
        
        "brojaci za odabir ovo 1st 2nd,.."
        self.i=0
        self.i2=0
        self.x=["2nd","3rd","4th","5th","6th","7th","8th","9th","10th"]
        
        
        "akcije prilikon pritiska 1 i 2 buttona"
        self.pushButton_3.clicked.connect(self.Button1)
        self.pushButton_4.clicked.connect(self.Button2)
        "akcije prilikon pritiska next buttona"
        self.pushButton.clicked.connect(self.btnNext)
        
        
        

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
    ui = Ui_layer3biranje()
    ui.setupUi(Dialog)
    Dialog.show()

    sys.exit(app.exec_())

