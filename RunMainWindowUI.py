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
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.Qt import QThread, QMutex
from MainWindowUI import Ui_MainWindow
from options import model_options
import sys


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.image_style = None
        # 添加信号与槽
        self.OpenImageButton.clicked.connect(self.OpenImage)
        self.SaveImageButton.clicked.connect(self.SaveImage)
        self.BeginConvButton.clicked.connect(self.BeginConv)
        for sb in self.styleButton:
            sb.clicked.connect(self.model_change)

    def model_change(self):
        obj_name = self.sender().objectName()[:-6]
        self.image_style = obj_name
        print(self.image_style)

    def OpenImage(self):
        img_path, img_type = QFileDialog.getOpenFileName(self, 'Open Image', '.', 'image files(*.png , *.jpg);;All Files(*)')
        print(img_path)
        # img = cv2.imread(image)
        # img = cv2.resize(img,dsize=(self.label.width(),self.label.height()),interpolation=cv2.INTER_CUBIC)
        # print(self.label.width(),self.label.height())
        # print("image resized")
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img = np.asanyarray(img)
        # img = QImage(img,self.label.width(),self.label.height(),QImage.Format_RGB888)
        img = QPixmap(img_path)
        self.label.setPixmap(img)
        self.imagePath_label.setText(img_path)
        print("show image on label.")

    def SaveImage(self):
        """
        这是保存图片按钮
        如果未有图片生成，应弹出窗口提示
        :return: None
        """
        pass

    def BeginConv(self):
        """
        这是开始转化按钮
        如果未选择风格，则应弹出窗口提示。
        :return: None
        """
        ops = model_options.ModelOps()
        ops.Load_model(image_style=self.image_style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())