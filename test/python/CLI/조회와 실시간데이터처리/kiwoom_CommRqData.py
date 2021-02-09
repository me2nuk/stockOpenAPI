from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication
import sys

class PyQt_kiwoomConnect:
    """
    CommRqData(
        BSTR sRQName,    // 사용자 구분명
        BSTR sTrCode,    // 조회하려는 TR이름
        long nPrevNext,  // 연속조회여부
        BSTR sScreenNo  // 화면번호
    )
          
    조회요청함수이며 빈번하게 조회요청하면 시세과부하 에러값으로 -200이 전달됩니다.
    리턴값
    0이면 조회요청 정상 나머지는 에러
    -200 시세과부하
    -201 조회전문작성 에러
    """
    def __init__(self) -> None:

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        self.kiwoom.OnEventConnect.connect(self.OnEventConnect)
        self.kiwoom.OnReceiveMsg.connect(self.OnReceiveMsg)

    def OnEventConnect(self, err_code):
        if err_code == 0:
            print('키움증권 OpenAPI+ 로그인 성공')
            self.kiwoom.dynamicCall("SetInputValue(QString, QString)", ["종목코드" ,"000020"])
            self.kiwoom.dynamicCall("SetInputValue(QString, QString)", ["기준일자","20200221"])
            self.kiwoom.dynamicCall("SetInputValue(QString, QString)", ["수정주가구분","1"])
            self.kiwoom.dynamicCall("SetInputValue(QString, QString, QString, QString))", ["RQName","opt10081","0","화면번호"])
            test = self.kiwoom.dynamicCall("CommRqData(QString, QString, QString, QString)", ["RQName", "opt10081", "0", "화면번호"])
            print(test)

        elif err_code == -100:
            print('사용자 정보교환 실패')
        elif err_code == -101:
            print('서버접속 실패')
        elif err_code == -102:
            print('버전처리 실패')

    def OnReceiveMsg(self, sScrNo, sRQName, sTrCode, sMsg):
        print(f"sScrNo : {sScrNo}")# 화면번호
        print(f"sRQName : {sRQName}")# 사용자 구분명
        print(f"sTrCode : {sTrCode}")# TR이름
        print(f"sMsg : {sMsg}")# 서버에서 전달하는 메시지

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()