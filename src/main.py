#vesion 0.1.4
from msg import Ui_short    #an esay msg box
#import from qt
from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QMainWindow
from PyQt6.QtCore import QRect,QMetaObject
#login window
class Ui_login(object):
    def setupUi(self, login):

        login.setObjectName("login")
        login.resize(290, 120)
        login.setFixedSize(290, 120)
        login.setWindowTitle("登录")

        self.login_name = QLineEdit(parent=login)
        self.login_name.setGeometry(QRect(10, 10, 270, 30))
        self.login_name.setInputMask("")
        self.login_name.setText("")
        self.login_name.setFrame(True)
        self.login_name.setReadOnly(False)
        self.login_name.setObjectName("login_name")
        self.login_name.setPlaceholderText("用户账号")

        self.password = QLineEdit(parent=login)
        self.password.setGeometry(QRect(10, 50, 270, 30))
        self.password.setText("")
        self.password.setObjectName("password")
        self.password.setPlaceholderText("密码")

        self.checkout = QPushButton(parent=login)
        self.checkout.setGeometry(QRect(205, 85, 75, 25))
        self.checkout.setObjectName("checkout")
        self.checkout.setText("确认")
        self.checkout.clicked.connect(self.login_button_cicked)

        self.no_login = QPushButton(parent=login)
        self.no_login.setGeometry(QRect(120, 85, 75, 25))
        self.no_login.setObjectName("no_login")
        self.no_login.setText("无账号")
        self.no_login.clicked.connect(self.no_login_button_cicked)

        QMetaObject.connectSlotsByName(login)

    def login_button_cicked(self):
        login.hide()
        MainWindow.show()
    def no_login_button_cicked(self):
        login.hide()
        MainWindow.show()

#main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 452)
        MainWindow.setFixedSize(800, 450)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("主页面")

        self.version_button = QPushButton(parent=self.centralwidget)
        self.version_button.setGeometry(QRect(710, 10, 75, 25))
        self.version_button.setObjectName("pushButton")
        self.version_button.setText("更新日志")
        self.version_button.clicked.connect(self.version_button_cicked)

        self.bug_button = QPushButton(parent=self.centralwidget)
        self.bug_button.setGeometry(QRect(710, 40, 75, 25))
        self.bug_button.setObjectName("pushButton")
        self.bug_button.setText("问题反馈")
        self.bug_button.clicked.connect(self.bug_button_clicked)

        self.button = QPushButton(parent=self.centralwidget)
        self.button.setGeometry(QRect(10, 10, 430, 430))
        self.button.setObjectName("pushButton")
        self.button.setText("点我")
        self.button.clicked.connect(self.button_clicked)
        
        QMetaObject.connectSlotsByName(MainWindow)

    def version_button_cicked(self):
        version.show()
    def bug_button_clicked(self):
        bug.show()
    def button_clicked(self):
        click.show()

#main
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    login = QWidget()
    Window1 = Ui_login()
    Window1.setupUi(login)

    MainWindow = QMainWindow()
    Window2 = Ui_MainWindow()
    Window2.setupUi(MainWindow)

    version = QWidget()
    Window3 = Ui_short()
    Window3.setupUi(version,"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">当前版本 dev 0.1.3</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">更新日志</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dev 0.1.4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">修复bug</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dev 0.1.3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">新增了问题反馈页面</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dev 0.1.2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">新增了问题反馈按钮</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dev 0.1.1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">新增了更新日志页面</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dev 0.1.0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">新增登录页面</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dev 0.0.1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">新增窗口</p></body></html>","更新日志")

    bug = QWidget()
    Window4 = Ui_short()
    Window4.setupUi(bug,"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">没有哈哈哈:)\n","问题反馈")
    
    click = QWidget()
    Window5 = Ui_short()
    Window5.setupUi(click,"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">别打了\n"
,"别打了")

    login.show()
    sys.exit(app.exec())

