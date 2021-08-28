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
import traceback
import sys, os


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.image_style = None
        self.image_save_path = None
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
        img_path, img_type = QFileDialog.getOpenFileName(self, 'Open Image', '.', 'image files(*.png , *.jpg)')
        print("Open Image path: ", img_path)
        # img = cv2.imread(image)
        # img = cv2.resize(img,dsize=(self.label.width(),self.label.height()),interpolation=cv2.INTER_CUBIC)
        # print(self.label.width(),self.label.height())
        # print("image resized")
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img = np.asanyarray(img)
        # img = QImage(img,self.label.width(),self.label.height(),QImage.Format_RGB888)
        if img_path != '':
            img = QPixmap(img_path)
            self.OrgImage.setPixmap(img)
            self.imagePath_label.setText(img_path)
            print("show image on label.")
        else:
            print("You are not open the image.")

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
            # PIL transform to QImage
            # image = QImage(ImageQt.ImageQt(image))
            # print(type(image))
            image_name = str(self.image_style) + '_' + os.path.split(self.imagePath_label.text())[1]
            self.image_save_path = "./result/" + image_name
            vuts.save_image(image, self.image_save_path)
            image = QPixmap(self.image_save_path)
            self.ConvImage.setPixmap(image)
        except Exception as e:
            traceback.print_exc()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
