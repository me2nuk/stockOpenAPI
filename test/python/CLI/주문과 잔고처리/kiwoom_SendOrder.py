from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication
import sys

class PyQt_kiwoomConnect:
    """
    SendOrder(
        BSTR sRQName, // 사용자 구분명
        BSTR sScreenNo, // 화면번호
        BSTR sAccNo,  // 계좌번호 10자리
        LONG nOrderType,  // 주문유형 1:신규매수, 2:신규매도 3:매수취소, 4:매도취소, 5:매수정정, 6:매도정정
        BSTR sCode, // 종목코드
        LONG nQty,  // 주문수량
        LONG nPrice, // 주문가격
        BSTR sHogaGb,   // 거래구분(혹은 호가구분)은 아래 참고
        BSTR sOrgOrderNo  // 원주문번호입니다. 신규주문에는 공백, 정정(취소)주문할 원주문번호를 입력합니다.
    )
          
    9개 인자값을 가진 국내 주식주문 함수이며 리턴값이 0이면 성공이며 나머지는 에러입니다.
    1초에 5회만 주문가능하며 그 이상 주문요청하면 에러 -308을 리턴합니다.
          
    [거래구분]
    모의투자에서는 지정가 주문과 시장가 주문만 가능합니다.
          
    00 : 지정가
    03 : 시장가
    05 : 조건부지정가
    06 : 최유리지정가
    07 : 최우선지정가
    10 : 지정가IOC
    13 : 시장가IOC
    16 : 최유리IOC
    20 : 지정가FOK
    23 : 시장가FOK
    26 : 최유리FOK
    61 : 장전시간외종가
    62 : 시간외단일가매매
    81 : 장후시간외종가
    """
    def __init__(self) -> None:

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        self.kiwoom.OnEventConnect.connect(self.OnEventConnect)
        self.kiwoom.OnReceiveMsg.connect(self.OnReceiveMsg)

    def OnEventConnect(self, err_code):
        if err_code == 0:
            print('키움증권 OpenAPI+ 로그인 성공')
            self.kiwoom.KOA_Functions("ShowAccountWindow","")
            send = self.kiwoom.SendOrder('주식매수','10011', '8157939411', 2, "060310", 1, 0, '03', "")
            print(send)
            send = self.kiwoom.SendOrder('주식매도','10011', '8157939411', 1, "060310", 1, 0, '03', "")
            print(send)
            
        elif err_code == -100: 
            print('사용자 정보교환 실패')
        elif err_code == -101:
            print('서버접속 실패')
        elif err_code == -102:
            print('버전처리 실패')

    def OnReceiveMsg(self, sScrNo, sRQName, sTrCode, sMsg):
        print(f"화면번호 : {sScrNo}")# 화면번호
        print(f"사용자 구분명 : {sRQName}")# 사용자 구분명
        print(f"TR이름 : {sTrCode}")# TR이름
        print(f"서버에서 전달하는 메시지 : {sMsg}")# 서버에서 전달하는 메시지

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoomLogin = PyQt_kiwoomConnect()
    app.exec_()
