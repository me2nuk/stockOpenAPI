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
        self.kiwoom.OnReceiveTrData.connect(self.OnReceiveTrData)

    def OnEventConnect(self, err_code):
        if err_code == 0:
            print('키움증권 OpenAPI+ 로그인 성공')
            self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", "060310")
            self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")

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

    def OnReceiveTrData(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext, nDataLength, sErrorCode, sMessage, sSplmMsg):
        print(f"화면번호 : {sScrNo}")
        print(f"사용자 구분명 : {sRQName}")
        print(f"TR이름 : {sTrCode}")
        print(f"레코드 이름 : {sRecordName}")
        print(f"연속조회 유무를 판단하는 값 0: 연속(추가조회)데이터 없음, 2:연속(추가조회) 데이터 있음 : {sPrevNext}")
        print(f"사용안함. : {nDataLength}")
        print(f"사용안함. : {sErrorCode}")
        print(f"사용안함. : {sMessage}")
        print(f"사용안함. : {sSplmMsg}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()