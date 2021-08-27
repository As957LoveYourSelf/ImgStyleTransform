"""
Create 2021.8.22 11:26
Author: ChuQi Zhang
Content:
1. Add preprocessing parameters to the model
2. Select model by args
"""
import tensorflow as tf
import torch as th
import os
import sys
from PyQt5.QtWidgets import *
from MainWindowUI import Ui_MainWindow

class ModelOps(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None):
        super(ModelOps, self).__init__(parent)

    def Load_model(self, image_style):
        """
        if image_style == None, pop up prompt window
        :param image_style: output image style
        :return:
        """
        model_path = "../model_pretrained_parameter"
        ganName, style = image_style.split('_')
        if image_style == None:
            pass
        else:
            model_list = os.listdir(os.path.join(model_path, ganName))
            model = None
            for m in model_list:
                if style in m:
                    model = m
                    print("Clicked model: ", model)
                    break
            if model != None:
                # begin load model
                imagepath = self.imagePath_label.text()
                print("image path: ", imagepath)

            else:
                print("No model!")

    def __generateImage(self, image, model_path):
        pass
