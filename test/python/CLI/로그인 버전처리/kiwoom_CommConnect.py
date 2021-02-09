from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication
import sys

class PyQt_kiwoomConnect:
    """
    수동 로그인설정인 경우 로그인창을 출력해서 로그인을 시도하거나 자동로그인 설정인 경우 로그인창 출력없이 로그인을 시도합니다.
    """
    def __init__(self) -> None:
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        print('kiwoom OpenAPI CommConnect() 호출 성공')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()