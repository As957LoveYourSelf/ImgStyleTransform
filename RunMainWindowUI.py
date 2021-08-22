import MainWindowUI as mui
from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    myui = mui.Ui_MainWindow()
    myui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())