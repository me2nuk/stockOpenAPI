from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication
import sys

class PyQt_kiwoomConnect:
    """
    OnReceiveMsg(
    BSTR sScrNo,   // 화면번호
    BSTR sRQName,  // 사용자 구분명
    BSTR sTrCode,  // TR이름
    BSTR sMsg     // 서버에서 전달하는 메시지
    )
          
    서버통신 후 수신한 메시지를 알려줍니다.
    메시지에는 6자리 코드번호가 포함되는데 이 코드번호는 통보없이 수시로 변경될 수 있습니다. 따라서 주문이나 오류관련처리를
    이 코드번호로 분류하시면 안됩니다.
    """
    def __init__(self) -> None:

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        self.kiwoom.OnEventConnect.connect(self.OnEventConnect)
        self.kiwoom.OnReceiveMsg.connect(self.OnReceiveMsg)

    def OnEventConnect(self, err_code):
        if err_code == 0:
            print('키움증권 OpenAPI+ 로그인 성공')
        elif err_code == -100:
            print('사용자 정보교환 실패')
        elif err_code == -101:
            print('서버접속 실패')
        elif err_code == -102:
            print('버전처리 실패')

    def OnReceiveMsg(self, sScrNo, sRQName, sTrCode, sMsg):
        print(f"sScrNo : {sScrNo}")
        print(f"sRQName : {sRQName}")
        print(f"sTrCode : {sTrCode}")
        print(f"sMsg : {sMsg}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()