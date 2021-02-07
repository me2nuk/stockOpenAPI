from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class PyQt_kiwoomConnect:
    def __init__(self) -> None:
        QMainWindow()
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")    
        self.kiwoom.OnEventConnect.connect(self.Login_Event)

    def Login_Event(self, err_code):
        if err_code == 0:
            print('로그인 성공')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()