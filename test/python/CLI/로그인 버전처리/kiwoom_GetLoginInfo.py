from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication
import sys

class PyQt_kiwoomConnect:
    """
    로그인 후 사용할 수 있으며 인자값에 대응하는 정보를 얻을 수 있습니다.
          
    인자는 다음값을 사용할 수 있습니다.
          
    "ACCOUNT_CNT" : 보유계좌 수를 반환합니다.
    "ACCLIST" 또는 "ACCNO" : 구분자 ';'로 연결된 보유계좌 목록을 반환합니다.
    "USER_ID" : 사용자 ID를 반환합니다.
    "USER_NAME" : 사용자 이름을 반환합니다.
    "KEY_BSECGB" : 키보드 보안 해지여부를 반환합니다.(0 : 정상, 1 : 해지)
    "FIREW_SECGB" : 방화벽 설정여부를 반환합니다.(0 : 미설정, 1 : 설정, 2 : 해지)
    "GetServerGubun" : 접속서버 구분을 반환합니다.(1 : 모의투자, 나머지 : 실서버)
          
    리턴값
    인자값에 대응하는 정보를 얻을 수 있습니다.          
    [보유계좌 목록 예시]
          
    CString   strAcctList = GetLoginInfo("ACCLIST");
    여기서 strAcctList는 ';'로 분리한 보유계좌 목록임
    예) "3040525910;567890;3040526010"
    """
    def __init__(self) -> None:
        
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")    
        self.kiwoom.OnEventConnect.connect(self.Login_Event)

    def Login_Event(self, err_code):
        if err_code == 0:
            print('키움증권 OpenAPI+ 로그인 성공')

            GetLoginInfoList = [
                'ACCOUNT_CNT', # 보유계좌 수를 반환합니다.
                'ACCLIST', # 구분자 ';'로 연결된 보유계좌 목록을 반환합니다.
                'USER_ID', # 사용자 ID를 반환합니다.
                'USER_NAME', # 사용자 이름을 반환합니다.
                'KEY_BSECGB', # 키보드 보안 해지여부를 반환합니다.(0 : 정상, 1 : 해지)
                'FIREW_SECGB', # 방화벽 설정여부를 반환합니다.(0 : 미설정, 1 : 설정, 2 : 해지)
                'GetServerGubun' # 접속서버 구분을 반환합니다.(1 : 모의투자, 나머지 : 실서버)
            ]
            GetLoginInformationAppand = {}

            for _ in GetLoginInfoList:
                this = self.kiwoom.dynamicCall("GetLoginInfo(QString", [_])
                GetLoginInformationAppand.update({_ : this})

            for InfoKeys, InfoValues in GetLoginInformationAppand.items():
                print(f'{InfoKeys} : {InfoValues}')
            
            #ACCOUNT_CNT = self.kiwoom.dynamicCall("GetLoginInfo(QString)", ["ACCOUNT_CNT"])
            #보유계좌 수를 반환합니다.

            #ACCLIST = self.kiwoom.dynamicCall("GetLoginInfo(QString)",["ACCLIST"])
            #구분자 ';'로 연결된 보유계좌 목록을 반환합니다.

            #USER_ID = self.kiwoom.dynamicCall("GetLoginInfo(QString)",["USER_ID"])
            #사용자 ID를 반환합니다.

            #USER_NAME = self.kiwoom.dynamicCall("GetLoginInfo(QString)",["USER_NAME"])
            #사용자 이름을 반환합니다.

            #KEY_BSECGB = self.kiwoom.dynamicCall("GetLoginInfo(QString)",["KEY_BSECGB"])
            #키보드 보안 해지여부를 반환합니다.(0 : 정상, 1 : 해지)

            #FIREW_SECGB = self.kiwoom.dynamicCall("GetLoginInfo(QString)",["FIREW_SECGB"])
            #방화벽 설정여부를 반환합니다.(0 : 미설정, 1 : 설정, 2 : 해지)

            #GetServerGubun = self.kiwoom.dynamicCall("GetLoginInfo(QString)",["GetServerGubun"])
            #접속서버 구분을 반환합니다.(1 : 모의투자, 나머지 : 실서버)

            sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()