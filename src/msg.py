#an easy qt window generator
#using:
#windowname = QWidget()
#Window = Ui_short()
#Window.setupUi(windowname,"html text here")
from PyQt6.QtWidgets import QTextBrowser
from PyQt6.QtCore import QRect,QMetaObject
class Ui_short(object):
    def setupUi(self,Form,msg,title):
        self.msg = msg
        self.title = title
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setFixedSize(400, 300)
        self.textBrowser = QTextBrowser(parent=Form)
        self.textBrowser.setGeometry(QRect(0, 0, 400, 300))
        self.textBrowser.setObjectName("textBrowser")
        QMetaObject.connectSlotsByName(Form)
        Form.setWindowTitle(self.title)
        self.textBrowser.setHtml(self.msg)