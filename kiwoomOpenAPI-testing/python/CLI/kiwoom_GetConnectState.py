from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication
import sys

class PyQt_kiwoomConnect:
    def __init__(self) -> None:
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        print('kiwoom OpenAPI CommConnect() 호출 성공')
        GetConnectState = self.kiwoom.dynamicCall("GetConnectState()")
        # 현재 로그인 상태를 알려줍니다.

        print(GetConnectState)
        sys.exit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()