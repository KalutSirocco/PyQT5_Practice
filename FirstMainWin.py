import sys
from turtle import screensize
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QDesktopWidget  # 用于获取电脑屏幕参数
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QPushButton  # 用于设置控件
from PyQt5.QtGui import QIcon
from cv2 import QT_PUSH_BUTTON


class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)

        #设置主窗口标题
        self.setWindowTitle('第一个主窗口应用')
        #设置窗口尺寸
        self.resize(400, 300)

        #获得当前状态栏
        self.status = self.statusBar()
        #显示消息
        self.status.showMessage('只存在5秒的消息', 5000)

        #设置窗口初始位置
        self.move(100, 100)

        #添加Button
        self.button1 = QPushButton('退出')
        #将信号槽关联
        self.button1.clicked.connect(self.onClick_Button)

        #布局为水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        #添加主框架
        mainFrame = QWidget()
        #将上面创建的水平布局放置到主框架中
        mainFrame.setLayout(layout)
        #将主框架放置到中心窗口 #每个创建应用程序的语法都是这样
        self.setCentralWidget(mainFrame)

    #设置居中
    def center(self):
        #获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2
        self.move(newLeft, newTop)

    #按钮单击事件的方法（Slot）
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+' 按钮被按下')
        #获取当前应用程序
        app = QApplication.instance()
        #退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(
        'E:\\BaiduNetdiskDownload\\Icon1800\\常用图标库\\PNG@2_black_icons\\ spiral [#29].png'))
    main = FirstMainWin()
    main.center()
    main.show()

    sys.exit(app.exec_())
