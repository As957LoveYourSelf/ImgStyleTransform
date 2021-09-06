"""
Content:
1. Add Listener for Button:
    OpenImageButton(OpenImage)
    SaveImageButton(SaveImage)
    BeginConvButton(BeginConv)
    radioButton("新海诚画风")
    radioButton2("国风")
    radioButton3("铅笔画")
    radioButton4("梵高星空风")
Tips:
单个文件打开 QFileDialog.getOpenFileName()
多个文件打开 QFileDialog.getOpenFileNames()
文件夹选取 QFileDialog.getExistingDirectory()
文件保存 QFileDialog.getSaveFileName()
"""
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
from PyQt5.Qt import QThread, QMutex
from MainWindowUI import Ui_MainWindow
from options.model_options import ModelOps
import torchvision.utils as vuts
import torchvision.transforms as transforms
from PIL import ImageQt, Image
import utils.sqlutil as su
import traceback
import sys, os

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.image_style = None
        self.image_save_path = None
        self.imglabel_w, self.imglabel_h = self.OrgImage.width(), self.OrgImage.height()
        # 添加信号与槽
        self.OpenImageButton.clicked.connect(self.OpenImage)
        self.SaveImageButton.clicked.connect(self.SaveImage)
        self.BeginConvButton.clicked.connect(self.BeginConv)
        for sb in self.styleButton:
            sb.clicked.connect(self.model_change)

    def model_change(self):
        obj_name = self.sender().objectName()[:-6]
        self.image_style = obj_name
        print("change: ", self.image_style)

    def OpenImage(self):
        try:
            img_path, img_type = QFileDialog.getOpenFileName(self, 'Open Image', './inputs', 'image files(*.png , *.jpg , *.jpeg)')
            print("Open Image path: ", img_path)
            if img_path != '':
                # 将图片显示至label，自动缩放大小
                img_w, img_h = Image.open(img_path).size
                print("open image size: h:{},w:{}".format(img_h,img_w))
                if img_h >= img_w:
                    radio = img_h * 1.0 / img_w
                    self.OrgImage.setScaledContents(False)
                    img = QPixmap(img_path).scaled(int(self.imglabel_h/radio), int(self.imglabel_h))
                    print(img.size())
                else:
                    self.OrgImage.setScaledContents(True)
                    img = QPixmap(img_path)
                    print(img.size())
                self.OrgImage.setPixmap(img)
                self.imagePath_label.setText(img_path)
                print("Shown image on label.")
                # 插入数据库
                sqlu = su.SQLutil()
                sqlu.image2mysql(img_path, _type='org')
            else:
                print("You are not open the image.")
        except:
            traceback.print_exc()

    def SaveImage(self):
        """
        这是保存图片按钮
        如果未有图片生成，应弹出窗口提示
        :return: None
        """
        if self.image_save_path != None:
            save_image_path, image_type = QFileDialog.getSaveFileName(self,
                                                                      "Save Image",
                                                                      self.image_save_path,
                                                                      "Image File (*.jpg);;(*.png)")
            if save_image_path != '':
                self.SaveImagePath_label.setText("已另存至:"+save_image_path)
                print("Save image in: ", save_image_path)
            else:
                print("Quit saving.")
        else:
            print("Save path is None.")

    def BeginConv(self):
        """
        这是开始转化按钮
        如果未选择风格，则应弹出窗口提示。
        :return: None
        """
        try:
            ops = ModelOps()
            image_style = self.image_style
            print("input: ", image_style)
            image = ops.Load_model(image_style=image_style, image_path=self.imagePath_label.text())
            image = transforms.ToTensor()(image)
            image_name = str(self.image_style) + '_' + os.path.split(self.imagePath_label.text())[1]
            self.image_save_path = "./result/" + image_name
            vuts.save_image(image, self.image_save_path)
            # 将图片显示至label，自动缩放大小
            img_w, img_h = Image.open(self.image_save_path).size
            if img_h >= img_w:
                radio = img_h * 1.0 / img_w
                self.ConvImage.setScaledContents(False)
                image = QPixmap(self.image_save_path).scaled(int(self.imglabel_h/radio), int(self.imglabel_h))
                print(image.size())
            else:
                self.ConvImage.setScaledContents(True)
                image = QPixmap(self.image_save_path)
                print(image.size())
            self.ConvImage.setPixmap(image)
            print("Shown image in ConvLabel.")
            # 插入数据库
            sqlu = su.SQLutil()
            sqlu.image2mysql(self.image_save_path, _type='tran')
        except Exception as e:
            traceback.print_exc()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
