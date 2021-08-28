"""
Create 2021.8.22 11:26
Author: ChuQi Zhang
Content:
1. Add preprocessing parameters to the model
2. Select model by args
"""
import tensorflow as tf
import torch
import torchvision.transforms as transforms
import os
import traceback
from PIL import Image
from torch.autograd import Variable
import numpy as np
from models import *
import sys
from PyQt5.QtWidgets import *
from MainWindowUI import Ui_MainWindow
from models import CartoonGAN


class ModelOps:
    def Load_model(self, image_style, image_path):
        """
        if image_style == None, pop up prompt window
        :param image_style: output image style
        :return: an image
        """
        models_path = ".\\model_pretrained_parameter"
        if image_style == None:
            # pop up prompt window
            pass
        else:
            try:
                ganName, style = image_style.split('_')
                print(ganName, style)
                model_list = os.listdir(os.path.join(models_path, ganName))
                model = None
                for m in model_list:
                    if style in m:
                        model = m
                        print("Clicked model: ", model)
                        break
                if model != None:
                    # begin load model
                    imagepath = image_path
                    model_path = os.path.join(models_path, ganName+"\\"+model)
                    print("image path: ", imagepath)
                    image = Image.open(imagepath)
                    return self.__generateImage(image, model_path)
                else:
                    print("No model!")
            except Exception as e:
                print("Program Error:")
                # print(e)
                traceback.print_exc()

    def __generateImage(self, image, model_path):
        """
        generate the conversion image
        :param image: Image class
        :param model_path: model path
        :return: a conversion Image class
        """
        if "CartoonGAN" in model_path:
            GAN = CartoonGAN.Transformer()
        elif "CycleGAN" in model_path:
            GAN = None
        else:
            print("None GAN")
            return
        with torch.no_grad():
            model = torch.load(model_path)
            GAN.load_state_dict(model)
            GAN.eval()
            if torch.cuda.is_available():
                GAN.cuda()
                print("GPU mode")
            else:
                GAN.float()
                print("CPU mode")
            input_image = image.convert("RGB")
            H = h = input_image.size[0]
            W = w = input_image.size[1]
            # you can change the LOAD_SIZE to change image input size
            ##############
            LOAD_SIZE = h
            ##############
            ratio = h*1.0/w
            if ratio > 1:
                h = LOAD_SIZE
                w = int(h*1.0/ratio)
            else:
                w = LOAD_SIZE
                h = int(w*ratio)
            input_image = input_image.resize((h,w),Image.BICUBIC)
            print("input_image size: ", input_image.size,end=" ")
            input_image = np.asarray(input_image)
            # RGB -> BGR
            input_image = input_image[:, :, [2,1,0]]
            input_image = transforms.ToTensor()(input_image).unsqueeze(0)
            # preprocess (-1, 1)
            input_image = -1 + 2*input_image
            if torch.cuda.is_available():
                input_image = Variable(input_image).cuda()
            else:
                input_image = Variable(input_image).float()
            print("Begin generate image")
            # into model, get result
            output_image = GAN(input_image)
            output_image = output_image[0]
            # BGR -> RGB
            output_image = output_image[[2,1,0],:,:]
            # deprocess, (0, 1)
            output_image = output_image.data.cpu().float() * 0.5 + 0.5
            output_image = output_image.squeeze(0)
            # save origin size
            output_image = transforms.ToPILImage()(output_image)
            output_image = output_image.resize((H, W), Image.BICUBIC)
            print("output_image size: ", output_image.size,end=" ")
        return output_image
