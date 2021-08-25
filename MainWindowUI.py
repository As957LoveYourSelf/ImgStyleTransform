# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImgStyleTransform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

"""
Clicked：鼠标左键点击按钮并释放触发该信号。最常用。

Pressed：鼠标左键按下时触发该信号

Released：鼠标左键释放时触发该信号

Toggled：控件标记状态发生改变时触发该信号。
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.OpenImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenImageButton.setGeometry(QtCore.QRect(210, 600, 120, 30))
        self.OpenImageButton.setObjectName("OpenImage")

        self.imagePath_label = QtWidgets.QLabel(self.centralwidget)
        self.imagePath_label.setGeometry(QtCore.QRect(195, 650, 150, 50))
        self.imagePath_label.setText("图片路径")
        self.imagePath_label.setWordWrap(True)
        self.imagePath_label.setAlignment(QtCore.Qt.AlignCenter)

        self.SaveImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveImageButton.setGeometry(QtCore.QRect(750, 590, 120, 30))
        self.SaveImageButton.setObjectName("SaveImage")

        self.BeginConvButton = QtWidgets.QPushButton(self.centralwidget)
        self.BeginConvButton.setGeometry(QtCore.QRect(455, 700, 150, 40))
        self.BeginConvButton.setObjectName("BeginConv")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 500, 330))
        self.label.setMinimumSize(QtCore.QSize(500, 330))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setMidLineWidth(1)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 230, 500, 330))
        self.label_2.setMinimumSize(QtCore.QSize(500, 330))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setMidLineWidth(1)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(250, 40, 89, 16))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(420, 40, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(560, 40, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(710, 40, 89, 16))
        self.radioButton_4.setObjectName("radioButton_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)



        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图风转"))
        self.OpenImageButton.setText(_translate("MainWindow", "OpenImage"))
        self.SaveImageButton.setText(_translate("MainWindow", "Save"))
        self.BeginConvButton.setText(_translate("MainWindow", "BeginConv"))
        self.label.setText(_translate("MainWindow", "原始图片"))
        self.label_2.setText(_translate("MainWindow", "结果图片"))
        self.radioButton.setText(_translate("MainWindow", "新海诚画风"))
        self.radioButton_2.setText(_translate("MainWindow", "国风"))
        self.radioButton_3.setText(_translate("MainWindow", "铅笔画"))
        self.radioButton_4.setText(_translate("MainWindow", "梵高星空风"))


