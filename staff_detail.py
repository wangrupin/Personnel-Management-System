# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff_detail.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_staff_detail(object):
    def setupUi(self, staff_detail):
        staff_detail.setObjectName("staff_detail")
        staff_detail.setEnabled(True)
        staff_detail.resize(917, 571)
        staff_detail.setStyleSheet("background-color:#f4f9f4;")
        self.lineEdit = QtWidgets.QLineEdit(staff_detail)
        self.lineEdit.setGeometry(QtCore.QRect(390, 40, 121, 21))
        self.lineEdit.setStyleSheet("font: 14pt \"华文行楷\";\n"
"color:rgb(80, 126, 59);\n"
"background-color:transparent;\n"
"border:outset;")
        self.lineEdit.setObjectName("lineEdit")
        self.no = QtWidgets.QLineEdit(staff_detail)
        self.no.setEnabled(False)
        self.no.setGeometry(QtCore.QRect(320, 130, 101, 21))
        self.no.setStyleSheet("border:outset;\n"
"background:transparent;\n"
"")
        self.no.setText("")
        self.no.setObjectName("no")
        self.label_9 = QtWidgets.QLabel(staff_detail)
        self.label_9.setGeometry(QtCore.QRect(250, 130, 61, 21))
        self.label_9.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_9.setObjectName("label_9")
        self.email = QtWidgets.QLineEdit(staff_detail)
        self.email.setGeometry(QtCore.QRect(590, 330, 101, 21))
        self.email.setStyleSheet("border:outset;")
        self.email.setText("")
        self.email.setObjectName("email")
        self.name = QtWidgets.QLineEdit(staff_detail)
        self.name.setGeometry(QtCore.QRect(590, 130, 101, 21))
        self.name.setStyleSheet("border:outset;")
        self.name.setText("")
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(staff_detail)
        self.label.setGeometry(QtCore.QRect(520, 130, 61, 21))
        self.label.setStyleSheet("font: 10pt \"幼圆\";")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(staff_detail)
        self.label_5.setGeometry(QtCore.QRect(250, 330, 61, 21))
        self.label_5.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(staff_detail)
        self.label_2.setGeometry(QtCore.QRect(250, 170, 61, 21))
        self.label_2.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(staff_detail)
        self.label_3.setGeometry(QtCore.QRect(250, 210, 61, 21))
        self.label_3.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_3.setObjectName("label_3")
        self.tel = QtWidgets.QLineEdit(staff_detail)
        self.tel.setGeometry(QtCore.QRect(320, 330, 101, 21))
        self.tel.setStyleSheet("border:outset;")
        self.tel.setObjectName("tel")
        self.label_4 = QtWidgets.QLabel(staff_detail)
        self.label_4.setGeometry(QtCore.QRect(250, 250, 61, 21))
        self.label_4.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(staff_detail)
        self.label_8.setGeometry(QtCore.QRect(250, 290, 61, 21))
        self.label_8.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(staff_detail)
        self.label_7.setGeometry(QtCore.QRect(520, 170, 61, 21))
        self.label_7.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_7.setObjectName("label_7")
        self.identity = QtWidgets.QLineEdit(staff_detail)
        self.identity.setGeometry(QtCore.QRect(320, 250, 101, 21))
        self.identity.setStyleSheet("border:outset;")
        self.identity.setObjectName("identity")
        self.address = QtWidgets.QLineEdit(staff_detail)
        self.address.setGeometry(QtCore.QRect(320, 290, 101, 21))
        self.address.setStyleSheet("border:outset;")
        self.address.setText("")
        self.address.setObjectName("address")
        self.label_6 = QtWidgets.QLabel(staff_detail)
        self.label_6.setGeometry(QtCore.QRect(520, 330, 61, 21))
        self.label_6.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_6.setObjectName("label_6")
        self.sex = QtWidgets.QLineEdit(staff_detail)
        self.sex.setGeometry(QtCore.QRect(320, 170, 101, 21))
        self.sex.setStyleSheet("border:outset;")
        self.sex.setText("")
        self.sex.setObjectName("sex")
        self.birth = QtWidgets.QLineEdit(staff_detail)
        self.birth.setGeometry(QtCore.QRect(320, 210, 101, 21))
        self.birth.setStyleSheet("border:outset;")
        self.birth.setText("")
        self.birth.setObjectName("birth")
        self.isMarried = QtWidgets.QLineEdit(staff_detail)
        self.isMarried.setGeometry(QtCore.QRect(590, 170, 101, 21))
        self.isMarried.setStyleSheet("border:outset;")
        self.isMarried.setText("")
        self.isMarried.setObjectName("isMarried")
        self.label_10 = QtWidgets.QLabel(staff_detail)
        self.label_10.setGeometry(QtCore.QRect(520, 250, 61, 21))
        self.label_10.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(staff_detail)
        self.label_11.setGeometry(QtCore.QRect(250, 370, 61, 21))
        self.label_11.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_11.setObjectName("label_11")
        self.school = QtWidgets.QLineEdit(staff_detail)
        self.school.setGeometry(QtCore.QRect(320, 410, 101, 21))
        self.school.setStyleSheet("border:outset;")
        self.school.setText("")
        self.school.setObjectName("school")
        self.major = QtWidgets.QLineEdit(staff_detail)
        self.major.setGeometry(QtCore.QRect(590, 370, 101, 21))
        self.major.setStyleSheet("border:outset;")
        self.major.setObjectName("major")
        self.education = QtWidgets.QLineEdit(staff_detail)
        self.education.setGeometry(QtCore.QRect(320, 370, 101, 21))
        self.education.setStyleSheet("border:outset;")
        self.education.setObjectName("education")
        self.label_13 = QtWidgets.QLabel(staff_detail)
        self.label_13.setGeometry(QtCore.QRect(520, 210, 61, 21))
        self.label_13.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_13.setObjectName("label_13")
        self.department = QtWidgets.QLineEdit(staff_detail)
        self.department.setGeometry(QtCore.QRect(590, 210, 101, 21))
        self.department.setStyleSheet("border:outset;")
        self.department.setText("")
        self.department.setObjectName("department")
        self.professional = QtWidgets.QLineEdit(staff_detail)
        self.professional.setGeometry(QtCore.QRect(590, 250, 101, 21))
        self.professional.setStyleSheet("border:outset;")
        self.professional.setText("")
        self.professional.setObjectName("professional")
        self.label_school = QtWidgets.QLabel(staff_detail)
        self.label_school.setGeometry(QtCore.QRect(250, 410, 61, 21))
        self.label_school.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_school.setObjectName("label_school")
        self.label_major = QtWidgets.QLabel(staff_detail)
        self.label_major.setGeometry(QtCore.QRect(520, 370, 61, 21))
        self.label_major.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_major.setObjectName("label_major")
        self.label_17 = QtWidgets.QLabel(staff_detail)
        self.label_17.setGeometry(QtCore.QRect(520, 290, 61, 21))
        self.label_17.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_17.setObjectName("label_17")
        self.workingtime = QtWidgets.QLineEdit(staff_detail)
        self.workingtime.setGeometry(QtCore.QRect(590, 290, 101, 21))
        self.workingtime.setStyleSheet("border:outset;")
        self.workingtime.setText("")
        self.workingtime.setObjectName("workingtime")
        self.back = QtWidgets.QPushButton(staff_detail)
        self.back.setEnabled(True)
        self.back.setGeometry(QtCore.QRect(40, 20, 31, 31))
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setStyleSheet("border-image: url(:/newPrefix/images/back.png);")
        self.back.setText("")
        self.back.setObjectName("back")
        self.time = QtWidgets.QLineEdit(staff_detail)
        self.time.setGeometry(QtCore.QRect(590, 410, 101, 21))
        self.time.setStyleSheet("border:outset;")
        self.time.setText("")
        self.time.setObjectName("time")
        self.label_time = QtWidgets.QLabel(staff_detail)
        self.label_time.setGeometry(QtCore.QRect(520, 410, 61, 21))
        self.label_time.setStyleSheet("font: 10pt \"幼圆\";")
        self.label_time.setObjectName("label_time")
        self.label_9.setBuddy(self.no)
        self.label.setBuddy(self.name)
        self.label_5.setBuddy(self.tel)
        self.label_2.setBuddy(self.sex)
        self.label_3.setBuddy(self.birth)
        self.label_4.setBuddy(self.identity)
        self.label_8.setBuddy(self.address)
        self.label_7.setBuddy(self.isMarried)
        self.label_6.setBuddy(self.email)
        self.label_10.setBuddy(self.professional)
        self.label_11.setBuddy(self.education)
        self.label_13.setBuddy(self.department)
        self.label_school.setBuddy(self.school)
        self.label_major.setBuddy(self.major)
        self.label_17.setBuddy(self.workingtime)
        self.label_time.setBuddy(self.school)

        self.retranslateUi(staff_detail)
        self.back.clicked.connect(staff_detail.goback)
        QtCore.QMetaObject.connectSlotsByName(staff_detail)

    def retranslateUi(self, staff_detail):
        _translate = QtCore.QCoreApplication.translate
        staff_detail.setWindowTitle(_translate("staff_detail", "Form"))
        self.lineEdit.setText(_translate("staff_detail", "员工详细信息"))
        self.label_9.setText(_translate("staff_detail", "员工编号："))
        self.label.setText(_translate("staff_detail", "员工姓名："))
        self.label_5.setText(_translate("staff_detail", "电话："))
        self.label_2.setText(_translate("staff_detail", "性别："))
        self.label_3.setText(_translate("staff_detail", "出生日期："))
        self.label_4.setText(_translate("staff_detail", "身份证号："))
        self.label_8.setText(_translate("staff_detail", "住址："))
        self.label_7.setText(_translate("staff_detail", "婚否："))
        self.label_6.setText(_translate("staff_detail", "邮箱："))
        self.label_10.setText(_translate("staff_detail", "职位："))
        self.label_11.setText(_translate("staff_detail", "学历："))
        self.label_13.setText(_translate("staff_detail", "所属部门："))
        self.label_school.setText(_translate("staff_detail", "毕业院校："))
        self.label_major.setText(_translate("staff_detail", "专业："))
        self.label_17.setText(_translate("staff_detail", "工龄："))
        self.label_time.setText(_translate("staff_detail", "毕业时间："))

import img_rc
