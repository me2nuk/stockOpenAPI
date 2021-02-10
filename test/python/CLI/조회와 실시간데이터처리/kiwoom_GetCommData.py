from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication
import sys

class PyQt_kiwoomConnect:
    """
    void OnReceiveTrData(
        BSTR sScrNo,       // 화면번호
        BSTR sRQName,      // 사용자 구분명
        BSTR sTrCode,      // TR이름
        BSTR sRecordName,  // 레코드 이름
        BSTR sPrevNext,    // 연속조회 유무를 판단하는 값 0: 연속(추가조회)데이터 없음, 2:연속(추가조회) 데이터 있음
        LONG nDataLength,  // 사용안함.
        BSTR sErrorCode,   // 사용안함.
        BSTR sMessage,     // 사용안함.
        BSTR sSplmMsg     // 사용안함.
    )
          
    조회요청 응답을 받거나 조회데이터를 수신했을때 호출됩니다.
    조회데이터는 이 이벤트내부에서 GetCommData()함수를 이용해서 얻어올 수 있습니다.
          
          
    """
    def __init__(self) -> None:

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        self.kiwoom.OnEventConnect.connect(self.OnEventConnect)
        self.kiwoom.OnReceiveMsg.connect(self.OnReceiveMsg)
        self.kiwoom.OnReceiveTrData.connect(self.OnReceiveTrData)
        self.kiwoom.OnReceiveChejanData.connect(self.OnReceiveChejanData)

    def OnEventConnect(self, err_code):
        if err_code == 0:
            print('키움증권 OpenAPI+ 로그인 성공')
            self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", "060310")
            self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")
            self.kiwoom.KOA_Functions("ShowAccountWindow","")
            #self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "비밀번호", "0000")
            send = self.kiwoom.SendOrder('주식매도','10011', '8157939411', 1, "060310", 1, 0, '03', "")
            print(send)
            
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
        if sRQName == "opt10001_req":
            name = self.kiwoom.dynamicCall("GetCommData(QString, QString, QString, QString", [sTrCode, "", 0, "종목명"])
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", sTrCode, "", sRQName, 0, "거래량")
            code = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", sTrCode, "", sRQName, 0, "종목코드")
            print(f"종목명 : {name}")
            print(f"거래량 : {volume}")
            print(f"종목코드 : {code}")

    def OnReceiveChejanData(self, sGubun, nItemCnt, sFIdList):
        print(f"sGubun : {sGubun}")
        print(f"nItemCnt : {nItemCnt}")
        print(f"sFIdList : {sFIdList}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()
