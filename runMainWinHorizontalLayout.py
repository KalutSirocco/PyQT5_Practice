import sys
import Ui_MainWinHorizontalLayout

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWinHorizontalLayout.Ui_MainWindow()
    ui.setupUi(MainWindow)#向主窗口添加控件
    MainWindow.show()
    sys.exit(app.exec_())
