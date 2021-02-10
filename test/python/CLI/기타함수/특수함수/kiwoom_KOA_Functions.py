from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication
import sys

class PyQt_kiwoomConnect:
    """
    KOA_Functions(
        BSTR sFunctionName,   // 함수이름 혹은 기능이름
        BSTR sParam   // 함수 매개변수
    ))
          
    KOA_Function() 함수는 OpenAPI기본 기능외에 기능을 사용하기 쉽도록 만든 함수이며 두 개 인자값을 사용합니다. 이 함수가 
    제공하는 기능과 필요한 인자값은 공지를 통해 제공할 예정입니다.          
    
    [KOA_Functions() 함수 사용예시]
          
    1. 계좌비밀번호 설정창표시
        OpenAPI.KOA_Functions(_T("ShowAccountWindow"), _T(""));// 계좌비밀번호 설정창을 출력한다.
          
    2. 접속서버확인
        OpenAPI.KOA_Functions(_T("GetServerGubun"), _T(""));// 접속서버 구분을 알려준다. 1 : 모의투자 접속, 나머지 : 실서버 접속 
          
    3. 주식종목 시장구분, 종목분류등 정보제공 
        OpenAPI.KOA_Functions(_T("GetMasterStockInfo"), _T("039490"));
        호출결과는 입력한 종목에 대한 대분류, 중분류, 업종구분값을 구분자로 연결한 문자열이며 여기서 구분자는 '|'와 ';'입니다.
        예를들어 OpenAPI.KOA_Functions("GetMasterStockInfo", "039490")을 호출하면 시장구분0|거래소;시장구분1|중형주;업종구분|금융업; 이렇게 결과를 얻을 수 있습니다. 
          
    4. 조검검색 종목코드와 현재가 수신(실시간 조건검색은 사용할수 없음)
        조건검색결과에 종목코드와 그 종목의 현재가를 함께 수신하는 방법이며 실시간 조건검색에서는 사용할 수 없고 오직 조건검색에만 사용할수 있습니다.
        OpenAPI.KOA_Functions(_T("SetConditionSearchFlag"), _T("AddPrice")); // 현재가 포함하도록 설정 
        현재가 포함으로 설정시 OnReceiveTrCondition()이벤트에 "종목코드1^현재가1;종목코드2^현재가2;...종목코드n^현재가n"형식으로 전달됨
          
        OpenAPI.KOA_Functions(_T("SetConditionSearchFlag"), _T("DelPrice")); // 현재가 미포함 (원래상태로 전환)
        현재가 미포함시 기존처럼 "종목코드1^종목코드2...종목코드n" 형식으로 전달므로 설정에 따라 수신데이터 처리방법이 달라져야 하므로 주의하셔야 합니다
        이 방법은 실시간 조건검색에서는 사용할 수 없고 수신데이터에 현재가가 포함되므로 데이터처리방법을 달리해야 합니다
          
    5. 업종코드 획득
        OpenAPI.KOA_Functions(_T("GetUpjongCode"), _T("0")); // 장내업종코드요청
        두 번째 인자로 사용할 수 있는 값은 0,1,2,4,7 이며 0:장내, 1: 코스닥, 2:KOSPI200, 4:KOSPI100(KOSPI50), 7:KRX100 이며 필요한 업종을 구별해서 사용하시면 됩니다.
        함수반환값은 "시장구분값,업종코드,업종명|시장구분값,업종코드,업종명|...|시장구분값,업종코드,업종명" 형식입니다.
        즉 하나의 업종코드는 입력한 시장구분값과 업종코드 그리고 그 업종명이 쉼표(,)로 구분되며 각 업종코드는 '|'로 구분됩니다.
    """
    def __init__(self) -> None:

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        self.kiwoom.OnEventConnect.connect(self.OnEventConnect)

    def OnEventConnect(self, err_code):
        if err_code == 0:
            print('키움증권 OpenAPI+ 로그인 성공')
            self.kiwoom.KOA_Functions("ShowAccountWindow","")
            
        elif err_code == -100:
            print('사용자 정보교환 실패')
        elif err_code == -101:
            print('서버접속 실패')
        elif err_code == -102:
            print('버전처리 실패')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()