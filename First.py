import sys

from PyQt5.QtWidgets import QApplication,QWidget
from matplotlib.pyplot import show

if __name__=='__main__':
    # 创建QApplication类的实例
    app=QApplication(sys.argv)
    # 创建一个窗口
    w=QWidget()
    # 设置窗口的尺寸
    w.resize(400,200)
    # 移动窗口（以窗口左上角为基准点）
    w.move(300,300)

    #设置窗口标题
    w.setWindowTitle('第一个基于PyQt5的桌面应用')

    w.show()

    #进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())

    