from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication
import sys

class PyQt_kiwoomConnect:
    """
    GetCommData(
        BSTR strTrCode,   // TR 이름
        BSTR strRecordName,   // 레코드이름
        long nIndex,      // TR반복부
        BSTR strItemName
    ) // TR에서 얻어오려는 출력항목이름
          
    OnReceiveTRData()이벤트가 호출될때 조회데이터를 얻어오는 함수입니다.
    이 함수는 반드시 OnReceiveTRData()이벤트가 호출될때 그 안에서 사용해야 합니다.
                    
    [OPT10081 : 주식일봉차트조회요청예시]
          
    OnReceiveTrDataKhopenapictrl(...)
    {
      if(strRQName == _T("주식일봉차트"))
      {
        int nCnt = OpenAPI.GetRepeatCnt(sTrcode, strRQName);
        for (int nIdx = 0; nIdx < nCnt; nIdx++)
        {
          strData = OpenAPI.GetCommData(sTrcode, strRQName, nIdx, _T("종목코드"));   strData.Trim();
          strData = OpenAPI.GetCommData(sTrcode, strRQName, nIdx, _T("거래량"));   strData.Trim();
          strData = OpenAPI.GetCommData(sTrcode, strRQName, nIdx, _T("시가"));   strData.Trim();
          strData = OpenAPI.GetCommData(sTrcode, strRQName, nIdx, _T("고가"));   strData.Trim();
          strData = OpenAPI.GetCommData(sTrcode, strRQName, nIdx, _T("저가"));   strData.Trim();
          strData = OpenAPI.GetCommData(sTrcode, strRQName, nIdx, _T("현재가"));   strData.Trim();
        }
      }
    }
    """
    def __init__(self) -> None:

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        self.kiwoom.OnEventConnect.connect(self.OnEventConnect)
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

    def OnReceiveTrData(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext, nDataLength, sErrorCode, sMessage, sSplmMsg):
        if sRQName == "opt10001_req":
            name = self.kiwoom.dynamicCall("GetCommData(QString, QString, QString, QString", [sTrCode, "", 0, "종목명"]).strip()
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", sTrCode, "", sRQName, 0, "거래량").strip()
            code = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", sTrCode, "", sRQName, 0, "종목코드").strip()
            print(f"종목명 : {name}")
            print(f"거래량 : {volume}")
            print(f"종목코드 : {code}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()
