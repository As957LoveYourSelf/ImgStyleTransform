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
        self.styleButton = []

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

        self.OrgImage = QtWidgets.QLabel(self.centralwidget)
        self.OrgImage.setGeometry(QtCore.QRect(20, 230, 500, 330))
        self.OrgImage.setMinimumSize(QtCore.QSize(500, 330))
        self.OrgImage.setFrameShape(QtWidgets.QFrame.Box)
        self.OrgImage.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.OrgImage.setMidLineWidth(1)
        self.OrgImage.setScaledContents(True)
        self.OrgImage.setAlignment(QtCore.Qt.AlignCenter)
        self.OrgImage.setWordWrap(False)
        self.OrgImage.setOpenExternalLinks(False)
        self.OrgImage.setObjectName("OrgImage")

        self.ConvImage = QtWidgets.QLabel(self.centralwidget)
        self.ConvImage.setGeometry(QtCore.QRect(550, 230, 500, 330))
        self.ConvImage.setMinimumSize(QtCore.QSize(500, 330))
        self.ConvImage.setFrameShape(QtWidgets.QFrame.Box)
        self.ConvImage.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ConvImage.setMidLineWidth(1)
        self.ConvImage.setScaledContents(True)
        self.ConvImage.setAlignment(QtCore.Qt.AlignCenter)
        self.ConvImage.setObjectName("ConvImage")

        self.ShinkaiButton = QtWidgets.QRadioButton(self.centralwidget)
        self.ShinkaiButton.setGeometry(QtCore.QRect(250, 40, 89, 16))
        self.ShinkaiButton.setObjectName("CartoonGAN_ShinkaiButton")
        self.styleButton.append(self.ShinkaiButton)

        self.CNPaintingButton = QtWidgets.QRadioButton(self.centralwidget)
        self.CNPaintingButton.setGeometry(QtCore.QRect(420, 40, 89, 16))
        self.CNPaintingButton.setObjectName("CNPaintingButton")
        self.styleButton.append(self.CNPaintingButton)

        self.PencilPainButton = QtWidgets.QRadioButton(self.centralwidget)
        self.PencilPainButton.setGeometry(QtCore.QRect(560, 40, 89, 16))
        self.PencilPainButton.setObjectName("PencilPainButton")
        self.styleButton.append(self.PencilPainButton)

        self.VanGoghButton = QtWidgets.QRadioButton(self.centralwidget)
        self.VanGoghButton.setGeometry(QtCore.QRect(710, 40, 89, 16))
        self.VanGoghButton.setObjectName("VanGoghButton")
        self.styleButton.append(self.VanGoghButton)

        self.HayaoButton = QtWidgets.QRadioButton(self.centralwidget)
        self.HayaoButton.setGeometry(QtCore.QRect(250, 60, 89, 16))
        self.HayaoButton.setObjectName("CartoonGAN_HayaoButton")
        self.styleButton.append(self.HayaoButton)

        self.HosodaButton = QtWidgets.QRadioButton(self.centralwidget)
        self.HosodaButton.setGeometry(QtCore.QRect(420, 60, 89, 16))
        self.HosodaButton.setObjectName("CartoonGAN_HosodaButton")
        self.styleButton.append(self.HosodaButton)

        self.PaprikaButton = QtWidgets.QRadioButton(self.centralwidget)
        self.PaprikaButton.setGeometry(QtCore.QRect(560, 60, 89, 16))
        self.PaprikaButton.setObjectName("CartoonGAN_PaprikaButton")
        self.styleButton.append(self.PaprikaButton)

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
        self.OrgImage.setText(_translate("MainWindow", "原始图片"))
        self.ConvImage.setText(_translate("MainWindow", "结果图片"))
        self.ShinkaiButton.setText(_translate("MainWindow", "新海诚画风"))
        self.CNPaintingButton.setText(_translate("MainWindow", "国风"))
        self.PencilPainButton.setText(_translate("MainWindow", "铅笔画"))
        self.VanGoghButton.setText(_translate("MainWindow", "梵高星空风"))
        self.HayaoButton.setText(_translate("MainWindow", "宫崎骏画风"))
        self.HosodaButton.setText(_translate("MainWindow", "细田守画风"))
        self.PaprikaButton.setText(_translate("MainWindow", "红辣椒画风"))
