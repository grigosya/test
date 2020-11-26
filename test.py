# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import sqlite3
import hashlib
import os
import csv
import random


class Ui_Form_Nfi(object):
    def setupUi_Nfi(self, Form):
        Form.setObjectName("Form")
        Form.resize(160, 110)
        self.vibor_file_tic = QtWidgets.QPushButton(Form)
        self.vibor_file_tic.setGeometry(QtCore.QRect(20, 40, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.vibor_file_tic.setFont(font)
        self.vibor_file_tic.setObjectName("vibor_file_tic")
        self.vibor_file_tic_2 = QtWidgets.QPushButton(Form)
        self.vibor_file_tic_2.setGeometry(QtCore.QRect(100, 50, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.vibor_file_tic_2.setFont(font)
        self.vibor_file_tic_2.setObjectName("vibor_file_tic_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.vibor_file_tic.setText(_translate("Form", "Файл"))
        self.vibor_file_tic_2.setText(_translate("Form", "->"))
        self.label.setText(_translate("Form", "Insert file"))
        self.label_2.setText(_translate("Form", "TextLabel"))


class Ui_Form_Nd(object):
    def setupUi_Nd(self, Form):
        Form.setObjectName("Form")
        Form.resize(220, 90)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 40, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name test"))
        self.pushButton.setText(_translate("Form", "->"))


class Ui_Form_adm(object):
    def setupUi_adm(self, Form):
        Form.setObjectName("Form")
        Form.resize(210, 150)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.insert_boton = QtWidgets.QRadioButton(Form)
        self.insert_boton.setGeometry(QtCore.QRect(20, 35, 82, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.insert_boton.setFont(font)
        self.insert_boton.setObjectName("insert_boton")
        self.del_boton = QtWidgets.QRadioButton(Form)
        self.del_boton.setGeometry(QtCore.QRect(20, 57, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.del_boton.setFont(font)
        self.del_boton.setObjectName("del_boton")
        self.dan_boton = QtWidgets.QRadioButton(Form)
        self.dan_boton.setGeometry(QtCore.QRect(20, 80, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.dan_boton.setFont(font)
        self.dan_boton.setObjectName("dan_boton")
        self.class_btn = QtWidgets.QPushButton(Form)
        self.class_btn.setGeometry(QtCore.QRect(20, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.class_btn.setFont(font)
        self.class_btn.setObjectName("class_btn")
        self.test_btn = QtWidgets.QPushButton(Form)
        self.test_btn.setGeometry(QtCore.QRect(130, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.test_btn.setFont(font)
        self.test_btn.setObjectName("test_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Admin"))
        self.insert_boton.setText(_translate("Form", "Запись"))
        self.del_boton.setText(_translate("Form", "Удаление"))
        self.dan_boton.setText(_translate("Form", "Получение данных"))
        self.class_btn.setText(_translate("Form", "Класс"))
        self.test_btn.setText(_translate("Form", "Тест"))


class Ui_Form_qu(object):
    def setupUi_qu(self, Form):
        Form.setObjectName("Form")
        Form.resize(311, 291)
        self.numder_question = QtWidgets.QLabel(Form)
        self.numder_question.setGeometry(QtCore.QRect(90, 0, 231, 52))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.numder_question.setFont(font)
        self.numder_question.setObjectName("numder_question")
        self.txt_qeuestion = QtWidgets.QLabel(Form)
        self.txt_qeuestion.setGeometry(QtCore.QRect(20, 50, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.txt_qeuestion.setFont(font)
        self.txt_qeuestion.setObjectName("txt_qeuestion")
        self.radioButton_1 = QtWidgets.QRadioButton(Form)
        self.radioButton_1.setGeometry(QtCore.QRect(20, 170, 40, 22))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_da")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 200, 87, 22))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_skoree_da")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(190, 200, 93, 22))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_skoree_net")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(190, 170, 46, 22))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_net")
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setGeometry(QtCore.QRect(110, 180, 72, 22))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_neznat")
        self.tic_question = QtWidgets.QPushButton(Form)
        self.tic_question.setGeometry(QtCore.QRect(100, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.tic_question.setFont(font)
        self.tic_question.setObjectName("tic_question")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.numder_question.setText(_translate("Form", "Вопрос _"))
        self.txt_qeuestion.setText(_translate("Form", "Текст"))
        self.radioButton_1.setText(_translate("Form", "Да"))
        self.radioButton_2.setText(_translate("Form", "Скорее Да"))
        self.radioButton_3.setText(_translate("Form", "Скорее Нет"))
        self.radioButton_4.setText(_translate("Form", "Нет"))
        self.radioButton_5.setText(_translate("Form", "Незнаю"))
        self.tic_question.setText(_translate("Form", "Далее ->"))


class Ui_Form_login(object):
    def setupUi_login(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 180)
        self.vod_login = QtWidgets.QLineEdit(Form)
        self.vod_login.setGeometry(QtCore.QRect(130, 10, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.vod_login.setFont(font)
        self.vod_login.setObjectName("vod_login")
        self.vod_password = QtWidgets.QLineEdit(Form)
        self.vod_password.setGeometry(QtCore.QRect(130, 50, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.vod_password.setFont(font)
        self.vod_password.setObjectName("vod_password")
        self.txt_login = QtWidgets.QLabel(Form)
        self.txt_login.setGeometry(QtCore.QRect(70, 0, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.txt_login.setFont(font)
        self.txt_login.setObjectName("txt_login")
        self.txt_password = QtWidgets.QLabel(Form)
        self.txt_password.setGeometry(QtCore.QRect(20, 40, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.txt_password.setFont(font)
        self.txt_password.setObjectName("txt_password")
        self.tic_fio = QtWidgets.QPushButton(Form)
        self.tic_fio.setGeometry(QtCore.QRect(210, 130, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.tic_fio.setFont(font)
        self.tic_fio.setObjectName("tic_fio")
        self.vod_name_test = QtWidgets.QLineEdit(Form)
        self.vod_name_test.setGeometry(QtCore.QRect(130, 90, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.vod_name_test.setFont(font)
        self.vod_name_test.setObjectName("vod_name_test")
        self.txt_name_test = QtWidgets.QLabel(Form)
        self.txt_name_test.setGeometry(QtCore.QRect(20, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.txt_name_test.setFont(font)
        self.txt_name_test.setObjectName("txt_name_test")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.txt_login.setText(_translate("Form", "login"))
        self.txt_password.setText(_translate("Form", "password"))
        self.tic_fio.setText(_translate("Form", "->"))
        self.txt_name_test.setText(_translate("Form", "name test"))


class MyWidget(QMainWindow, Ui_Form_login):
    def __init__(self):
        super().__init__()
        self.setupUi_login(self)

        self.tic_fio.clicked.connect(self.proverka_login)
        self.vod_password.setEchoMode(QLineEdit.Password)
        self.local_param_hash = 'c466177d01f4793399ba9a0285cbe1ae35e7a42859600ba69d7e0f01dd61b6d7'

    def proverka_login(self):
        txt_login = self.vod_login.text()
        txt_password = self.vod_password.text()
        txt_name_test = self.vod_name_test.text()

        self.vod_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vod_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vod_name_test.setStyleSheet("background-color: rgb(255, 255, 255);")

        if txt_login == '':
            self.vod_login.setStyleSheet("background-color: rgb(255, 51, 51);")
            return

        if txt_password == '':
            self.vod_password.setStyleSheet("background-color: rgb(255, 51, 51);")
            return

        if txt_name_test == '':
            self.vod_name_test.setStyleSheet("background-color: rgb(255, 51, 51);")
            return

        con = sqlite3.connect('BD_test.sqlite')
        cursor = con.cursor()
        pas = cursor.execute(
            f"""SELECT Password, Salt_pas, Student_id FROM Log WHERE Login = '{txt_login}'""").fetchall()
        c = 0
        for i in pas:
            password = hashlib.sha256(txt_password.encode('utf-8')).hexdigest() + i[1] + self.local_param_hash
            if password == i[0]:
                c += 1
                break
        if c == 0:
            self.vod_login.setStyleSheet('background-color: rgb(253, 233, 16);')
            self.vod_password.setStyleSheet('background-color: rgb(253, 233, 16);')
            return
        if i[2] == 31:
            self.vizov_adm()
        else:
            con = sqlite3.connect("BD_test.sqlite")
            cursor = con.cursor()
            if len(cursor.execute(f"SELECT id FROM Test WHERE Name_test = '{txt_name_test}'").fetchall()) == 0:
                self.vod_name_test.setStyleSheet('background-color: rgb(253, 233, 16);')
                return
            self.id_Test = cursor.execute(f"SELECT id FROM Test WHERE Name_test = '{txt_name_test}'").fetchone()[0]
            self.id_Student = i[2]
            self.vizov()

    def vizov(self):
        self.test = question_form(self.id_Student, self.id_Test)
        self.test.show()

    def vizov_adm(self):
        self.adm = adm_form()
        self.adm.show()


class question_form(QWidget, Ui_Form_qu):
    def __init__(self, id_Student, id_Test):
        self.id_t = id_Test
        self.id_s = id_Student
        super().__init__()
        self.count = 0
        self.answers = []
        self.setupUi_qu(self)
        self.radioButton_1.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()
        self.radioButton_4.hide()
        self.radioButton_5.hide()
        con = sqlite3.connect("BD_test.sqlite")
        cursor = con.cursor()
        var = cursor.execute(f"SELECT Var_otv FROM Varianti_otvetov WHERE id_test = '{id_Test}'").fetchall()
        self.var = []
        for i in var:
            self.var.append(i[0])
        if len(self.var) == 2:
            self.radioButton_1.show()
            self.radioButton_2.show()
            self.radioButton_1.setText(self.var[0])
            self.radioButton_2.setText(self.var[1])
        if len(self.var) == 3:
            self.radioButton_1.show()
            self.radioButton_2.show()
            self.radioButton_5.show()
            self.radioButton_1.setText(self.var[0])
            self.radioButton_2.setText(self.var[1])
            self.radioButton_5.setText(self.var[2])
        if len(self.var) == 4:
            self.radioButton_1.show()
            self.radioButton_2.show()
            self.radioButton_3.show()
            self.radioButton_4.show()
            self.radioButton_1.setText(self.var[0])
            self.radioButton_2.setText(self.var[1])
            self.radioButton_3.setText(self.var[2])
            self.radioButton_4.setText(self.var[3])
        if len(self.var) == 5:
            self.radioButton_1.show()
            self.radioButton_2.show()
            self.radioButton_3.show()
            self.radioButton_4.show()
            self.radioButton_5.show()
            self.radioButton_1.setText(self.var[0])
            self.radioButton_2.setText(self.var[1])
            self.radioButton_3.setText(self.var[2])
            self.radioButton_4.setText(self.var[3])
            self.radioButton_5.setText(self.var[4])
        qu = cursor.execute(f"SELECT Question FROM Questions WHERE Test_id = '{id_Test}'").fetchall()
        con.close()
        self.questions = []
        for i in qu:
            self.questions.append(i[0])
        self.count2 = len(self.questions)
        self.tic_question.clicked.connect(self.work)
        self.numder_question.setText(f'Вопрос {self.count + 1}')
        self.txt_qeuestion.setText(f'{self.questions[self.count]}')

    def work(self):
        if self.count >= self.count2:
            self.tic_question.setStyleSheet("background-color: rgb(255, 51, 51);")
            return
        if self.count == self.count2 - 1:
            otv = ''
            if self.radioButton_1.isChecked():
                otv = self.radioButton_1.text()
            if self.radioButton_2.isChecked():
                otv = self.radioButton_2.text()
            if self.radioButton_3.isChecked():
                otv = self.radioButton_3.text()
            if self.radioButton_4.isChecked():
                otv = self.radioButton_4.text()
            if self.radioButton_5.isChecked():
                otv = self.radioButton_5.text()
            if otv == '':
                self.tic_question.setStyleSheet("background-color: rgb(255, 51, 51);")
                return
            self.answers.append(otv)
            self.count += 1
            con = sqlite3.connect("BD_test.sqlite")
            cursor = con.cursor()
            answer = '_'.join(self.answers)
            if len(cursor.execute(f"""SELECT id FROM Answer WHERE Student_id = '{self.id_s}' AND Test_id = '{self.id_t}'""").fetchall()) == 0:
                cursor.execute(
                    f"""INSERT INTO Answer(Student_id, Test_id, Answers) VALUES('{self.id_s}', '{self.id_t}', '{answer}')""")
            con.commit()
            con.close()
        else:
            otv = ''
            if self.radioButton_1.isChecked():
                otv = self.radioButton_1.text()
            if self.radioButton_2.isChecked():
                otv = self.radioButton_2.text()
            if self.radioButton_3.isChecked():
                otv = self.radioButton_3.text()
            if self.radioButton_4.isChecked():
                otv = self.radioButton_4.text()
            if self.radioButton_5.isChecked():
                otv = self.radioButton_5.text()
            if otv == '':
                self.tic_question.setStyleSheet("background-color: rgb(255, 51, 51);")
                return
            self.answers.append(otv)
            self.count += 1
            if self.count != self.count2:
                self.numder_question.setText(f'Вопрос {self.count + 1}')
                self.txt_qeuestion.setText(f'{self.questions[self.count]}')


class adm_form(QWidget, Ui_Form_adm):
    def __init__(self):
        super().__init__()
        self.fail_name = ''
        self.setupUi_adm(self)
        self.test_btn.clicked.connect(self.chto_t)
        self.class_btn.clicked.connect(self.chto_c)

    def chto_t(self):
        if self.insert_boton.isChecked():
            self.insert('t')
        elif self.del_boton.isChecked():
            self.delete('t')
        elif self.dan_boton.isChecked():
            self.dan('t')

    def chto_c(self):
        if self.insert_boton.isChecked():
            self.insert('c')
        elif self.del_boton.isChecked():
            self.delete('c')
        elif self.dan_boton.isChecked():
            self.dan('c')

    def insert(self, c_t):
        if c_t == 't':
            self.ntfi()
        if c_t == 'c':
            self.ncfi()

    def delete(self, c_t):
        if c_t == 't':
            self.vizov_Ntd()
        if c_t == 'c':
            self.vizov_Ncd()
        else:
            self.fail_vibor.setStyleSheet('background-color: rgb(255, 51, 51);')

    def dan(self, c_t):
        self.d = Dan()
        self.d.show()

    def vizov_Ntd(self):
        self.ntd = Nd('t')
        self.ntd.show()

    def vizov_Ncd(self):
        self.ncd = Nd('c')
        self.ncd.show()

    def ntfi(self):
        self.nf = Nfi('t')
        self.nf.show()

    def ncfi(self):
        self.nf = Nfi('c')
        self.nf.show()


class Nd(QWidget, Ui_Form_Nd):
    def __init__(self, c_t):
        super().__init__()
        self.setupUi_Nd(self)
        if c_t == 't':
            self.pushButton.clicked.connect(self.ntd)
        elif c_t == 'c':
            self.label.setText('Name class')
            self.pushButton.clicked.connect(self.ncd)

    def ntd(self):
        txt_name_test_del = self.lineEdit.text()
        if len(txt_name_test_del) == 0:
            self.lineEdit.setStyleSheet("background-color: rgb(255, 51, 51);")
            return
        con = sqlite3.connect("BD_test.sqlite")
        cursor = con.cursor()
        names_tests = cursor.execute(f"SELECT Name_test FROM Test").fetchall()
        nt = []
        for i in names_tests:
            nt.append(i[0])
        if txt_name_test_del not in nt:
            self.lineEdit.setStyleSheet("background-color: rgb(255, 51, 51);")
            return
        name_test = txt_name_test_del
        id_t = cursor.execute(f"""SELECT id FROM Test WHERE Name_test = '{name_test}'""").fetchone()[0]
        cursor.execute(f"""DELETE FROM Answer WHERE Test_id = '{id_t}'""")
        cursor.execute(f"""DELETE FROM Questions WHERE Test_id = '{id_t}'""")
        cursor.execute(f"""DELETE FROM Varianti_otvetov WHERE id_test = '{id_t}'""")
        cursor.execute(f"""DELETE FROM Test WHERE id = '{id_t}'""")
        con.commit()
        con.close()
        self.lineEdit.setStyleSheet('background-color: rgb(15, 255, 131);')

    def ncd(self):
        txt_name_class_del = self.lineEdit.text()
        if len(txt_name_class_del) == 0:
            self.lineEdit.setStyleSheet("background-color: rgb(255, 51, 51);")
            return
        name_clas = txt_name_class_del
        con = sqlite3.connect("BD_test.sqlite")
        cursor = con.cursor()
        names_classes = cursor.execute(f"SELECT Class FROM Classes").fetchall()
        nc = []
        for i in names_classes:
            nc.append(i[0])
        if txt_name_class_del not in nc:
            self.lineEdit.setStyleSheet("background-color: rgb(255, 51, 51);")
            return
        con = sqlite3.connect("BD_test.sqlite")
        cursor = con.cursor()
        clas_id = cursor.execute(f"""SELECT id FROM Classes WHERE Class = '{name_clas}'""").fetchone()[0]
        lst_id_st = cursor.execute(f"""SELECT id FROM Students WHERE Class_id = '{clas_id}'""").fetchall()
        for id_st in lst_id_st:
            cursor.execute(f"""DELETE FROM Answer WHERE Student_id = '{id_st[0]}'""")
            cursor.execute(f"""DELETE FROM Log WHERE Student_id = '{id_st[0]}'""")
            cursor.execute(f"""DELETE FROM Students WHERE id = '{id_st[0]}'""")
        cursor.execute(f"""DELETE FROM Classes WHERE id = '{clas_id}'""")
        con.commit()
        con.close()
        self.lineEdit.setStyleSheet('background-color: rgb(15, 255, 131);')


class Nfi(QWidget, Ui_Form_Nfi):
    def __init__(self, c_t):
        super().__init__()
        self.setupUi_Nfi(self)
        self.label_2.setText('')
        self.vibor_file_tic.clicked.connect(self.vibor)
        if c_t == 't':
            self.vibor_file_tic_2.clicked.connect(self.insert_t)
        if c_t == 'c':
            self.vibor_file_tic_2.clicked.connect(self.insert_c)

    def vibor(self):
        self.fail_name = QFileDialog.getOpenFileName(self, 'Выбрать файл:', '', 'csv file(*.csv)')[0]
        self.label_2.setText(self.fail_name.split('/')[-1])

    def insert_t(self):
        if self.fail_name == '':
            self.vibor_file_tic.setStyleSheet("background-color: rgb(255, 51, 51);")
            return
        if self.fail_name.split('.')[-1] != 'csv':
            self.vibor_file_tic.setStyleSheet("background-color: rgb(255, 51, 51);")
        self.quesytion_read(self.fail_name)
        self.vibor_file_tic.setStyleSheet('background-color: rgb(15, 255, 131);')

    def insert_c(self):
        if self.fail_name == '':
            self.vibor_file_tic.setStyleSheet("background-color: rgb(255, 51, 51);")
            return
        if self.fail_name.split('.')[-1] != 'csv':
            self.vibor_file_tic.setStyleSheet("background-color: rgb(255, 51, 51);")
        self.clas_read(self.fail_name)
        self.vibor_file_tic.setStyleSheet('background-color: rgb(15, 255, 131);')

    def quesytion_read(self, name):
        read = []
        with open(name, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                read.append('_'.join(row))
        name_test = read[0]
        con = sqlite3.connect('BD_test.sqlite')
        cursor = con.cursor()
        for i in range(int(read[1])):
            pass
        if len(cursor.execute(f"""SELECT id FROM Test WHERE \
        Name_test = '{name_test}'""").fetchall()) == 0:
            cursor.execute(
                f"""INSERT INTO Test(Name_test, Key) VALUES('{name_test}', '{read[i + 3]}')""")
        id_test = (cursor.execute(
            f"""SELECT id FROM Test WHERE Name_test = '{name_test}'"""
        ).fetchone())[0]
        for i in range(int(read[1])):
            if len(cursor.execute(f"""SELECT id FROM Varianti_otvetov \
            WHERE id_test = '{id_test}' AND Var_otv = \
            '{read[i + 2]}'""").fetchall()) == 0:
                cursor.execute(
                    f"""INSERT INTO Varianti_otvetov(id_test, Var_otv) VALUES('{id_test}', '{read[i + 2]}')"""
                )
        for j in range(int(read[i + 4])):
            q = read[i + 5 + j]
            if len(cursor.execute(f"""SELECT id FROM Questions WHERE\
             Test_id = '{id_test}' AND Namber_in_test = '{j + 1}' AND\
              Question = '{q}'""").fetchall()) == 0:
                cursor.execute(
                    f"""INSERT INTO Questions(Test_id, Namber_in_test, Question) 
                    VALUES('{id_test}', '{j + 1}', '{q}')"""
                )
        con.commit()
        con.close()

    def clas_read(self, name):
        self.local_param_hash = 'c466177d01f4793399ba9a0285cbe1ae35e7a42859600ba69d7e0f01dd61b6d7'
        self.name_cheloveki = []
        with open(name, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            self.log = []
            self.pas = []
            self.pas_orig = []
            self.pas_salt = []
            for self.index, row in enumerate(reader):
                self.name_cheloveki.append(row)
                # make login
                translate = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V',
                             'в': 'v',
                             'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh',
                             'ж': 'zh',
                             'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L',
                             'л': 'l',
                             'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R',
                             'р': 'r',
                             'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh',
                             'х': 'kh',
                             'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch',
                             'Ы': 'Y',
                             'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'}
                alphabet = ['Ь', 'ь', 'Ъ', 'ъ', 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё',
                            'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
                            'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч',
                            'Ш', 'ш', 'Щ', 'щ', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']

                logs = row[0]
                logss = row[1]
                log = ''
                if self.index != 0:
                    for i in logs:
                        if i in alphabet:
                            log += translate[i]
                        else:
                            log += i
                    plas = ''
                    for i in ''.join(self.name_cheloveki[0]):
                        if i in alphabet:
                            plas += translate[i]
                        else:
                            plas += i
                    for i in logss:
                        if i in alphabet:
                            log += translate[i]
                        else:
                            log += i
                    log = log + plas
                    self.log.append(log)
                    # make password

                    pas = ''
                    for i in range(16):
                        pas += random.choice(
                            '1234567890!@#$%^&*()_qwertyuiop[]QWERTYUIOP{}ASDFGHJKLasdfghjklZXCVBNM<>?zxcvbnm')
                    self.pas_orig.append(pas)
                    salt = os.urandom(16)
                    salt = hashlib.sha256(salt).hexdigest()
                    hash_object = hashlib.sha256(pas.encode('utf-8'))
                    pas = hash_object.hexdigest() + salt + self.local_param_hash
                    self.pas.append(pas)
                    self.pas_salt.append(salt)
                    con = sqlite3.connect('BD_test.sqlite')
                    cursor = con.cursor()
                    clas = ''.join(self.name_cheloveki[0])
                    if len(cursor.execute(f"""SELECT id FROM Classes WHERE Class = '{clas}'""").fetchall()) == 0:
                        cursor.execute(f"""INSERT INTO Classes(Class) VALUES('{clas}')""")
                    con.commit()
                    if self.index != 0:
                        chel = self.name_cheloveki[self.index]
                        surname = chel[0]
                        name = chel[1]
                        midle_name = chel[2]
                        clas_id = (cursor.execute(f"SELECT id FROM Classes WHERE Class = '{clas}'").fetchone())[0]
                        login = self.log[self.index - 1]
                        password = self.pas[self.index - 1]
                        salt_pas = self.pas_salt[self.index - 1]
                        if len(cursor.execute(
                                f"""SELECT id FROM Students WHERE Surname = '{surname}' AND Name = '{name}' AND 
                                                            Middle_name = '{midle_name}' AND Class_id = '{clas_id}'""").fetchall()) == 0:
                            cursor.execute(
                                f"""INSERT INTO Students
                                        (Surname, Name, Middle_name, Class_id)
                                        VALUES 
                                        ('{surname}', '{name}', '{midle_name}', '{clas_id}')""")
                        student_id = \
                            (cursor.execute(
                                f"""SELECT id FROM Students WHERE Surname = '{surname}' AND Name = '{name}' AND 
                                                                Middle_name = '{midle_name}' AND Class_id = '{clas_id}'""").fetchone())[
                                0]

                        if len(cursor.execute(
                                f"""SELECT id FROM Log WHERE Login = '{login}' AND Student_id = '{student_id}'""").fetchall()) == 0:
                            cursor.execute(
                                f"""INSERT INTO Log
                                        (Login, Password, Salt_pas, Student_id)
                                        VALUES 
                                        ('{login}', '{password}', '{salt_pas}', '{student_id}')""")
                    con.commit()
                    con.close()

            con = sqlite3.connect("BD_test.sqlite")
            cursor = con.cursor()
            cursor.execute("INSERT INTO Count(Namber) VALUES('0')")
            cnt = cursor.execute("SELECT id FROM Count").fetchall()
            cnt_lst = []
            for i in cnt:
                cnt_lst.append(int(i[0]))
            count = max(cnt_lst)
            cursor.execute(f"DELETE FROM Count WHERE id = '{count - 1}'")
            con.commit()
            con.close()
            name_new_file = 'new_pas-log' + f'{count}' + '.csv'
            csv.register_dialect(name_new_file, delimiter=';', quotechar='"')
            with open(name_new_file, 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(len(self.pas_orig) - 1):
                    writer.writerow([self.log[i], self.pas_orig[i]])
                self.label_2.setText(name_new_file)


class Dan(QWidget, Ui_Form_Nd):
    def __init__(self):
        super().__init__()
        self.setupUi_Nd(self)
        self.label.setText('Test and Class')
        self.pushButton.clicked.connect(self.vid)

    def vid(self):
        if len(self.lineEdit.text().split()) != 2:
            self.lineEdit.setStyleSheet("background-color: rgb(255, 51, 51);")
            return
        clas = self.lineEdit.text().split()[1]
        test = self.lineEdit.text().split()[0]
        con = sqlite3.connect("BD_test.sqlite")
        cursor = con.cursor()
        if len(cursor.execute(f"SELECT id FROM Classes WHERE Class = '{clas}'").fetchall()) == 0 or \
                len(cursor.execute(f"SELECT id FROM Test WHERE Name_test = '{test}'").fetchall()) == 0:
            self.lineEdit.setStyleSheet("background-color: rgb(255, 51, 51);")
            return
        id_clas = cursor.execute(f"SELECT id FROM Classes WHERE Class = '{clas}'").fetchone()[0]
        id_test = cursor.execute(f"SELECT id FROM Test WHERE Name_test = '{test}'").fetchone()[0]
        st = cursor.execute(f"SELECT id, Surname, Name, Middle_name FROM Students WHERE Class_id = '{id_clas}'").fetchall()
        students = []
        print(st)
        key = cursor.execute(f"SELECT Key FROM Test WHERE id = '{id_test}'").fetchone()[0].split('_')
        for i in st:
            prav = 0
            answer = (cursor.execute(f"SELECT Answers FROM Answer WHERE Student_id = '{i[0]}' AND Test_id = '{id_test}'").fetchone()[0]).split('_')
            for j in range(len(key)):
                if key[j] == answer[j]:
                    prav += 1
            lst = []
            for j in i:
                lst.append(j)
            lst.append(answer)
            lst.append(prav)
            students.append(lst)

        con = sqlite3.connect("BD_test.sqlite")
        cursor = con.cursor()
        cursor.execute("INSERT INTO Count2(Namber) VALUES('0')")
        cnt = cursor.execute("SELECT id FROM Count2").fetchall()
        cnt_lst = []
        for i in cnt:
            cnt_lst.append(int(i[0]))
        count = max(cnt_lst)
        cursor.execute(f"DELETE FROM Count2 WHERE id = '{count - 1}'")
        con.commit()
        con.close()
        name_new_file = 'new_dan' + f'{count}' + '.csv'
        csv.register_dialect(name_new_file, delimiter=';', quotechar='"')
        with open(name_new_file, 'w', newline='') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in students:
                writer.writerow([i[1], i[2], i[3], '_'.join(i[4]), i[5]])
            self.label.setText(name_new_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MW = MyWidget()
    MW.show()
    sys.exit(app.exec())
