from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication
import sys

class PyQt_kiwoomConnect:
    def __init__(self) -> None:
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")    
        #self.kiwoom.OnEventConnect.connect(self.Login_Event)
        self.kiwoom.OnEventConnect.connect(self.Login_Event)
    def Login_Event(self, err_code):
        if err_code == 0:
            print('키움증권 OpenAPI+ 로그인 성공')
            sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()