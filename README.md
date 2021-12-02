# 키움증권 OpenApi

<br>

## What is it

이 프로젝트는 키움증권 OpenAPI를 편하게 사용하기 위해 만들어졌으며,
다양한 가이드와 키움증권 OpenAPI예시 또는 사용법이 있습니다.

<br>

| name | Explanation | 현재 상태 |
| - | - | - |
| [test](https://github.com/kimminwyk/stockOpenAPI/tree/main/test) | 키움증권 OpenAPI를 사용한 코드가 작성되어있습니다. | 작성중 |
| [Kiwoom-Image](https://github.com/kimminwyk/stockOpenAPI/tree/main/scripts) | 키움증권 가이드를 작성하면서 사용된 이미지 파일 | 작성중 |
| [guide](https://github.com/kimminwyk/stockOpenAPI/tree/main/guide) | 키움증권 OpenAPI 사용 가이드입니다. | 작성중 |

<br>

+ [키움 Open API+](https://www1.kiwoom.com/nkw.templateFrameSet.do?m=m1408000000)

+ [키움 OpenAPI+ 개발가이드 PDF](https://download.kiwoom.com/web/openapi/kiwoom_openapi_plus_devguide_ver_1.5.pdf)

+ [키움 OpenAPI 교육 VOD](https://www.howtostock.com/acdm/getLectureList.action?COUR_SEQ=49&CURR_SEQ=218)

<br><br>

## Kiwoom OpenAPI Contents

* * *

<br>

+ [키움증권 OpenApi](#키움증권-openapi) 
    + [Kiwoom OpenAPI Contents](#kiwoom-openapi-contents)
    + [Kiwoom OpenApi](#kiwoom-openapi)
    + [OpenAPI Step](#openapi-step)
        + [Step1](#Step1)
        + [Step2](#Step2)
        + [Step3](#Step3)
        + [Step4](#Step4)
    + [kiwoom openapi method](#kiwoom-openapi-method)
        + [로그인 버전처리](#로그인%20버전처리)
            + [설명](#설명)
            + [CommConnect()](#commconnect)
            + [CommTerminate()](#commterminate)
            + [GetConnectState()](#getconnectstate)
            + [GetLoginInfo()](#getlogininfo)
            + [OnEventConnect()](#oneventconnect)
            + [OnReceiveMsg()](#onreceivemsg)
        + [조회와 실시간데이터처리](#조회와-실시간데이터처리)
            + [설명](#설명-1)
            + [CommRqData()](#commrqdata)
            + [SetInputValue()](#setinputvalue)
            + [CommGetData()](#commgetdata)
            + [DisconnectRealData()](#disconnectrealdata)
            + [GetRepeatCnt()](#getrepeatcnt)
            + [CommKwRqData()](#commkwrqdata)
            + [GetCommData()](#getcommdata)
            + [GetCommRealData()](#getcommrealdata)
            + [GetCommDataEx()](#getcommdataex)
            + [OnReceiveTrData()](#onreceivetrdata)
            + [OnReceiveRealData()](#onreceiverealdata)
            + [OnReceiveMsg()](#onreceivemsg-1)
        + [주문과 잔고처리](#주문과-잔고처리)
            + [설명](#설명-2)
            + [SendOrder()](#sendorder)
            + [SendOrderFO()](#sendorderfo)
            + [SendOrderCredit()](sendordercredit)
            + [GetChejanData()](#getchejandata)
            + [OnReceiveChejanData()](#onreceivechejandata)
            + [OnReceiveMsg()](#onreceivemsg-2)
            + [OnReceiveTrData()](#onreceivetrdata-1)
        + [조건검색](#조건검색)
            + [설명](#설명-3)
        + [기타함수](#기타함수)
            + [종목정보관련함수](#종목정보관련함수)
                + [GetCodeListByMarket()](#getcodelistbymarket)
            + [특수함수](#특수함수)
                + [KOA_Functions()](#koa_functions)
    + [kiwoom OpenAPI ErrorMsg](#kiwoom-openapi-errormsg)
        + [opstarter](#-opstarter)
        + [mfc100.dll](#-mfc100dll)
        + [MSVCR100.dll](#-msvcr100dll)
        + [QAxBase Error](#-qaxbase-error)
        + [ModuleNotFoundError](#-modulenotfounderror)

<br>

## Kiwoom OpenApi

* * *

<br>

<p align="center"><img src="./Kiwoom-Image/OpenApiMainPage.png"></p>

<br>

## OpenAPI Step

* * *

<br>

+ #### Step1

   + OpenApi 서비스 사용 신청

+ #### Step2

    + 키움 Open API+ 모듈 다운로드

+ #### Step3

    + 개발가이드
    + KOA Studio
    + 교육 VOD
    + 자료실

+ #### Step4

    + 상시 모의투자 신청

<br>

## kiwoom OpenAPI Method

* * *

<br>

+ ### 로그인 버전처리

    + #### 설명
    
    <br>

    ```
    [로그인 개요]
        로그인은 CommConnect()함수를 호출하며 OnEventConnect 이벤트 인자값으로 로그인 성공여부를 알수 있습니다.
        이 값이 0이면 성공이고 나머지는 실패로 오류코드값을 참고해서 실패원인을 파악할수 있습니다. 
        실서버와 동일한 시세데이터로 주문테스트를 할수 있는 모의투자서버를 제공하는데 로그인창에서 "모의투자 서버"을 선택해서 간단히 접속하실수 있습니다.
        
    [수동 로그인]
        로그인창에 로그인ID와 비밀번호를 직접입력해서 로그인을 하는것을 말하며 기본적으로 이 로그인방법을 사용하게 됩니다.
        수동 로그인중에 버전처리내용이 있는 경우 버전처리도 함께 진행됩니다.
        
    [자동 로그인]
        로그인한 다음 계좌비밀번호 입력창을 통해 자동로그인을 설정할 수 있습니다.
        트레이 메뉴(모니터 오른쪽 하단)에서 "계좌비밀번호 저장" 메뉴를 선택하면 화면이 표시되는데 여기서 로그인 이후 사용할 계좌와
        계좌비밀번호를 입력하고 등록버튼을 눌러서 저장한 다음 계좌번호 아래에 있는 AUTO체크 박스를 선택하시면 자동 로그인을 위한
        설정이 모두 끝납니다.
        로그인 설정을 자동으로 하면 종목정보를 제외한 버전처리를 모두 무시하게 되며 버전처리를 다시 받으려면 AUTO버튼을 체크
        해지하고 프로그램을 재 실행 하시면 됩니다.

    [계좌비밀번호 설정]
        잔고나 주문가능금액,수량등 계좌관련 조회나 주문전에 미리 계좌비밀번호를 설정해야 오류 알림창과 -301 오류코드없이 사용하실수 있습니다.
        계좌비밀번호 설정은 계좌비밀번호 입력창에서만 가능하며 이 입력창은 메뉴나 함수로 출력하실수 있습니다.
        메뉴이용 - 로그인후 트레이 메뉴(모니터 오른쪽 하단)에서 "계좌비밀번호 저장"선택
        함수이용 - 로그인후 OpenAPI.KOA_Functions(_T("ShowAccountWindow"), _T(""))호출
        
    [버전 처리]
        로그인할때 버전처리가 필요한 경우 버전처리 알림창이 출력될수 있습니다.
        이 알림창이 표시되면 OpenAPI프로그램을 먼저 모두 종료한다음 알림창에 있는 닫기버튼을 누르셔야 합니다.
        그렇지 않으면 버전처리가 정상적으로 끝나지 않아서 로그인할때 또 버전처리 알림창이 표시됩니다.
        그리고 알림창이 표시되었을때 KOA Studio도 실행중이면 역시 함께 종료시켜주셔야 합니다.
        이렇게 OpenAPI프로그램을 모두 종료하신 다음 알림창을 닫아주시면 버전처리가 자동으로 진행되고 프로그램을 재실행 해주시면 됩니다.

    [모의투자]
        로그인 창에서 모의투자접속을 선택을 체크하면 모의투자로 접속하며 이 체크를 풀면 실서버(운영서버)로 접속합니다.
        단 KOA Studio 프로그램은 항상 모의투자로만 접속가능해서 모의투자접속 체크 해지가 않됩니다.
        모의투자로 로그인하시려면 당사 홈페이지에서 미리 모의투자 사용신청을 하셔야 하며 상세한 내용은 당사 홈페이지를 참고하시기 바랍니다.
        모의투자 계좌번호, 주문 가능종목, 수수료등 정책은 실서버와 차이가 있으므로 상세한 내용은 홈페이지 내용을 꼭 참고해 주세요.
        
    [중복로그인]
        OpenAPI는 중복로그인을 허용하지 않기 때문에 동일PC나 다른PC나 관계없이 마지막에 로그인한 경우만 유지되고 이전에 로그인한 프로그램은 자동으로 로그오프됩니다.
        모의투자서버 로그인 역시 중복로그인을 허용하지 않습니다.
    ```

    <br>

    | 타입 | 이름 | 설명 |
    | ---- | ---- | ---- |
    | LONG | CommConnect() | 수동 로그인설정인 경우 로그인창출력 후 로그인 시도하거나 자동로그인 설정인 경우 자동으로 로그인을 시도합니다. |
    | Void | CommTerminate() | 현재 지원하지않는 함수입니다. |
    | LONG | GetConnectState() | 현재 로그인 상태를 알려줍니다. |
    | LONG | GetLoginInfo() | 로그인 후에만 사용할 수 있으며 인자값에 따라 다양항 정보를 얻을 수 있습니다. |
    | void | OnEventConnect() | 현재 로그인 상태를 알려줍니다. |
    | void | OnReceiveMsg() | 서버통신한 다음 수신한 메시지를 알려줍니다. |

    <br>

    + #### CommConnect()

        > 수동 로그인설정인 경우 로그인창출력 후 로그인 시도하거나 자동로그인 설정인 경우 자동으로 로그인을 시도합니다.

        [Example python](https://github.com/kimminwyk/stockOpenAPI/tree/main/test/python/CLI/로그인%20버전처리/kiwoom_CommConnect.py)

        <br>

        ActiveX를 사용하여 KHOPENAPI.KHOpenAPICtrl.1를 불러온 다음 CommConnect()한 다음 
        <br>

        <p align="left"><img src="./Kiwoom-Image/kiwoomOpenAPILogin.png"></p>

        이런식으로 로그인 창이 뜨면 성공이다.

        <br>

    + #### CommTerminate()

        > 현재 지원하지않는 함수입니다.

        <br>

    + #### GetConnectState()

        > 현재 로그인 상태를 알려줍니다.

        [Example python](https://github.com/kimminwyk/stockOpenAPI/tree/main/test/python/CLI/로그인%20버전처리/kiwoom_GetConnectState.py)

        GetConnectState 반환값(return)

        | 1 | 0 |
        | - | - |
        | 연결| 연결안됨 |

        <br>

    + #### GetLoginInfo()

        > 로그인 후에만 사용할 수 있으며 인자값에 따라 다양항 정보를 얻을 수 있습니다. 

        [Example python](https://github.com/kimminwyk/stockOpenAPI/tree/main/test/python/CLI/로그인%20버전처리/kiwoom_GetLoginInfo.py)

        + #### GetLoginInfo() 인자 종류

            | 인자이름 | 설명 |
            | - | - |
            | ACCOUNT_CNT | 보유계좌 수를 반환합니다. |
            | ACCLIST | 구분자 ';'로 연결된 보유계좌 목록을 반환합니다. |
            | USER_ID | 사용자 ID를 반환합니다. |
            | USER_NAME | 사용자 이름을 반환합니다. |
            | KEY_BSECGB | 키보드 보안 해지여부를 반환합니다.(0 : 정상, 1 : 해지) |
            | FIREW_SECGB | 방화벽 설정여부를 반환합니다.(0 : 미설정, 1 : 설정, 2 : 해지) |
            | GetServerGubun | 접속서버 구분을 반환합니다.(1 : 모의투자, 나머지 : 실서버) |
                

        <br>

    + #### OnEventConnect()

        > 현재 로그인 상태를 알려줍니다.

        [Example python](https://github.com/kimminwyk/stockOpenAPI/tree/main/test/python/CLI/로그인%20버전처리/kiwoom_OnEventConnect.py)

        | nErrCode | 상태 |
        | --------- | --- |
        | 0 | 로그인 성공 |
        | -100 | 사용자 정보교환 실패 |
        | -101 | 서버접속 실패 |
        | -102 | 버전처리 실패 |

        <br>

    + #### OnReceiveMsg()

        > 서버통신한 다음 수신한 메시지를 알려줍니다.

        [Example python](https://github.com/kimminwyk/stockOpenAPI/tree/main/test/python/CLI/로그인%20버전처리/kiwoom_OnReceiveMsg.py)

        | 이름 | 설명 |
        | -- | -- |
        | sScrNo | 화면번호 |
        | sRQName | 사용자 구분명 |
        | sTrCode | TR이름 | 
        | sMsg | 서버에서 전달하는 메세지 |

<br>

+ ### 조회와 실시간데이터처리

    + #### 설명

    <br>

    ```
    [조회처리(조회요청)]
        OpenAPI가 제공하는 데이터중에서 원하는 데이터를 서버에 요청해서 가져오는 것을     말하는데 TR(Transaction)단위로 처리됩니다.
        TR이란 서버와 데이터를 주고받을때 정의한 약속된 규약이며 입력부분(Input)과    데이터를 수신하는 출력부분(Output)을 가지고 있습니다.
        입력부분은 요청하는 데이터에 따라 입력갯수(입력항목)가 달라지며 출력부분은 보통   데이터갯수(출력항목)가 여러개로 구성됩니다.

        출력부분은 출력항목이 한번씩만 전달되는 싱글데이터와 복수로 전달되는 멀티데이터가     있고 TR에 따라 싱글데이터(또는 멀티데이터)만
        있거나 둘다 있는 경우도 있습니다.
        OpenAPI가 제공하는 TR은 KOA Studio의 TR목록 탭에서 찾아볼 수 있고 각 TR별로   조회도 가능합니다.
        OPT10070 : 당일주요거래원요청 - 싱글데이터
        OPT10081 : 주식일봉차트조회요청 - 싱글 + 멀티데이터

    [계좌비밀번호 설정]
        잔고나 주문가능금액,수량등 계좌관련 조회나 주문전에 미리 계좌비밀번호를 설정해야  오류 알림창과 -301 오류코드없이 사용하실수 있습니다.
        계좌비밀번호 설정은 계좌비밀번호 입력창에서만 가능하며 이 입력창은 메뉴나 함수로  출력하실수 있습니다.
        메뉴이용 - 로그인후 트레이 메뉴(모니터 오른쪽 하단)에서 "계좌비밀번호 저장"선택
        함수이용 - 로그인후 OpenAPI.KOA_Functions(_T("ShowAccountWindow"), _T(""))호출

    [조회제한]
        OpenAPI 조회는 1초당 5회로 제한되며 복수종목 조회와 조건검색 조회 횟수가  합산됩니다.
        가령 1초 동안 시세조회2회 관심종목 1회 조건검색 2회 순서로 조회를 했다면 모두     합쳐서 5회이므로 모두 조회성공하겠지만 
        조건검색을 3회 조회하면 맨 마지막 조건검색 조회는 실패하게 됩니다.

    [조회제한 강화]
        기존 1초당 5회 조회제한외에 분당, 시간당 유동적 조회제한이 2017년 4월 6일     17:00이후 반영되었습니다.
        (OpenAPI 게시판 조회제한 관련 공지내용을 참고하세요.)

        조회제한 강화 발생시 에러코드(-200)리턴과 알림 메시지가 표시되며 조회제한 강화가  발생한 프로그램은 다시 로그인해야 조회기능을 다시 이용할 수 있으며 
        구체적인 조회제한 기준은 비공개로 운영하고 있습니다.

        이 조회제한 강화는 거래시간, 거래일에 관계없이 OpenAPI프로그램 실행시 항상    점검합니다.
        점검방법은 CommRqData()함수와 CommKwRqData()함수를 이용한 조회횟수를 합산하는     것으로 연속조회 역시 CommRqData()를 이용므로 합산됩니다.
        이외 SetRealReg()함수호출이나 나머지 OpenAPI함수호출은 조회제한 강화와 관련없으며     실시간 시세데이터 사용도 관련없습니다.
        조회횟수 합산은 프로그램별로 합산하며 로그인ID 별로는 합산하지 않습니다.
        예를들어 같은ID로 로그인한 2개 프로그램에서 각각 10회씩 조회했다면 프로그램별 10회    조회이며 20조회로 합산하지 않습니다.

    [연속조회]
        TR별로 한번에 전달할 수 있는 데이터 갯수가 정해져 있습니다. 그런데 이 갯수보다    조회데이터가 많을때 연속조회로 모든 데이터를 조회하게 됩니다.
        연속조회는 모든 조회처리에 적용되는 공통사항이며 CommRqData()에서 인자값만 바꿔서     처리합니다.

        아래처럼 설정해서 맨 처음 조회했을때 추가로 조회할 데이터가 있다면
        OpenAPI.CommRqData("일별데이터조회", "OPT10086" , 0, "0001");
        OnReceiveTRData()이벤트에서 5번째 인자값(sPrevNext)에 "2"가 전달됩니다.
        그렇다면 연속조회하실때는 CommRqData("일별데이터조회", "OPT10086" , 2, "0001");   3번째 인자값을 2로 설정해서 조회하시면 됩니다.
        정리하면 다음과 같습니다.
        OpenAPI.CommRqData("일별데이터조회", "OPT10086" , 0, "0001"); // 처음조회시   혹은 연속데이터가 없을때
        OpenAPI.CommRqData("일별데이터조회", "OPT10086" , 2, "0001"); // 연속조회시

    [실시간 데이터]
        시세조회요청이 성공하면 관련 실시간 시세데이터가 발생했을때 서버에서 자동으로     OnReceiveRealData()이벤트로 실시간 타입단위로 전달해줍니다.
        KOA Studio의 실시간 탭을 여시면 Real Type과 "주식시세"에서 "종목프로그램매매"까지     나열된 이름을 확인할 수 있습니다.
        이들 하나하나를 실시간 타입이라고 하며 관련있는 FID(숫자)와 이름(실시간 항목)를   임의로 모아놓은 것입니다.
        예를들어 실시간 타입 "주식시세"는 FID 10 현재가 ~ FID 568 하한가발생시간까지 19개     FID로 구성되며 한꺼번에 전달되는것입니다.
        또 실시간 타입 "주식체결"는 FID 20 체결시간 ~ FID 1313 Extra Item까지 35개 FID가  한번에 전달됩니다.

    [실시간 데이터 - 주의사항]
        실시간 타입 "주문체결", "잔고", "파생잔고"는 주문관련 실시간 데이터를 전달하기    때문에 시세조회한 뒤나 SetRealReg()함수로 등록해서 사용할 수 없습니다.
        이 실시간 타입은 주문을 해야 발생하며 주문전용 OnReceiveChejanData()이벤트로  전달됩니다.

        아래 실시간 타입은 시스템 내부용으로 사용할수없는 실시간 타입입니다.
        1. 임의연장정보
        2. 시간외종목정보
        3. 주식거래원
        4. 순간체결량
        5. 선물옵션합계
        6. 투자자별매매

    [참고 SetRealReg() 함수]
        SetRealReg()함수로도 실시간 시세데이터 수신이 가능하며 시세조회요청과 방법만  다를뿐 수신하는 실시간 시세데이터 그리고 데이터 처리 방법은 동일합니다
        이 함수는 조건검색 항목에서 사용법을 설명하고 있습니다.
    ```

    <br>

    | 타입 | 이름 | 설명 |
    | -- | -- | -- |
    | LONG | CommRqData() | 조회요청함수이며 빈번하게 조회요청하면 시세과부하 에러값으로 -200이 전달됩니다. |
    | void | SetInputValue() | 조회요청시 TR의 Input값을 지정하는 함수이며 조회 TR 입력값이 많은 경우 이 함수를 반복적으로 호출합니다. |
    | BSTR | CommGetData() | 일부 TR에서 사용상 제약이 있음므로 이 함수 대신 GetCommData()함수를 사용하는것을 권장합니다. |
    | void | DisconnectRealData() | 화면번호 설정한 실시간 데이터를 해지합니다. |
    | LONG | GetRepeatCnt() | 조회수신한 멀티데이터의 갯수(반복)수를 얻을수 있습니다. |
    | LONG | CommKwRqData() | 한번에 100종목을 조회할 수 있는 관심종목 조회함수입니다. |
    | BSTR | GetCommData() | OnReceiveTRData()이벤트가 호출될때 조회데이터를 얻어오는 함수입니다. |
    | BSTR | GetCommRealData() | OnReceiveRealData()이벤트가 호출될때 실시간데이터를 얻어오는 함수입니다. | 
    | VARIANT | GetCommDataEx() | 조회 수신데이터 크기가 큰 차트데이터를 한번에 가져올 목적으로 만든 전용함수입니다. |
    | void | OnReceiveTrData() | 조회요청 응답을 받거나 조회데이터를 수신했을때 호출됩니다. |
    | void | OnReceiveRealData() | 실시간 데이터 수신할때마다 호출되며 SetRealReg()함수로 등록한 실시간 데이터도 이 이벤트로 전달됩니다. |
    | void | OnReceiveMsg() | 서버통신 후 수신한 메시지를 알려줍니다. |

    <br>

    + #### CommRqData()

        > 조회요청함수이며 빈번하게 조회요청하면 시세과부하 에러값으로 -200이 전달됩니다.

        [Example python](https://github.com/kimminwyk/stockOpenAPI/blob/main/test/python/CLI/%EC%A1%B0%ED%9A%8C%EC%99%80%20%EC%8B%A4%EC%8B%9C%EA%B0%84%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%B2%98%EB%A6%AC/kiwoom_CommRqData.py)

    + #### SetInputValue()

        > 조회요청시 TR의 Input값을 지정하는 함수이며 조회 TR 입력값이 많은 경우 이 함수를 반복적으로 호출합니다.

    <br>

    + #### CommGetData()

        > 일부 TR에서 사용상 제약이 있음므로 이 함수 대신 GetCommData()함수를 사용하시기 바랍니다.

    <br>

    + #### DisconnectRealData()

        > 화면번호 설정한 실시간 데이터를 해지합니다.

    <br>


    + #### GetRepeatCnt()

        > 조회수신한 멀티데이터의 갯수(반복)수를 얻을수 있습니다. 예를들어 차트조회는 한번에 최대 900개 데이터를 수신할 수 있는데 이렇게 수신한 데이터갯수를 얻을때 사용합니다.
          이 함수는 반드시 OnReceiveTRData()이벤트가 호출될때 그 안에서 사용해야 합니다.

    <br>

    + #### CommKwRqData()

        > 한번에 100종목을 조회할 수 있는 관심종목 조회함수인데 영웅문HTS [0130] 관심종목 화면과는 이름만 같은뿐 전혀관련이 없습니다.
          함수인자로 사용하는 종목코드 리스트는 조회하려는 종목코드 사이에 구분자';'를 추가해서 만들면 됩니다.
          조회데이터는 관심종목정보요청(OPTKWFID) Output을 참고하시면 됩니다.
          이 TR은 CommKwRqData()함수 전용으로 임의로 사용하시면 에러가 발생합니다.

    <br>


    + #### GetCommData()

        > OnReceiveTRData()이벤트가 호출될때 조회데이터를 얻어오는 함수입니다.
          이 함수는 반드시 OnReceiveTRData()이벤트가 호출될때 그 안에서 사용해야 합니다.

    <br>

    + #### GetCommRealData()

        > OnReceiveRealData()이벤트가 호출될때 실시간데이터를 얻어오는 함수입니다.
          이 함수는 반드시 OnReceiveRealData()이벤트가 호출될때 그 안에서 사용해야 합니다.

    <br>

    + #### GetCommDataEx()

        > 조회 수신데이터 크기가 큰 차트데이터를 한번에 가져올 목적으로 만든 전용함수입니다.

    <br>

    + #### OnReceiveTrData()

        >  조회요청 응답을 받거나 조회데이터를 수신했을때 호출됩니다.
          조회데이터는 이 이벤트내부에서 GetCommData()함수를 이용해서 얻어올 수 있습니다.
    
    <br>

    + #### OnReceiveRealData()

        >  실시간 데이터 수신할때마다 호출되며 SetRealReg()함수로 등록한 실시간 데이터도 이 이벤트로 전달됩니다.
          GetCommRealData()함수를 이용해서 실시간 데이터를 얻을수 있습니다.

    <br>

    + #### OnReceiveMsg()

        > 서버통신 후 수신한 메시지를 알려줍니다.
          메시지에는 6자리 코드번호가 포함되는데 이 코드번호는 통보없이 수시로 변경될 수 있습니다. 따라서 주문이나 오류관련처리를
          이 코드번호로 분류하시면 안됩니다. 

        [Example python](https://github.com/kimminwyk/stockOpenAPI/blob/main/test/python/CLI/%EC%A1%B0%ED%9A%8C%EC%99%80%20%EC%8B%A4%EC%8B%9C%EA%B0%84%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%B2%98%EB%A6%AC/kiwoom_CommRqData.py)

        | 이름 | 설명 |
        | -- | -- |
        | sScrNo | 화면번호 |
        | sRQName | 사용자 구분명 |
        | sTrCode | TR이름 | 
        | sMsg | 서버에서 전달하는 메세지 |

    <br>

<br>

+ ### 주문과 잔고처리

    + #### 설명

    <br>

    ```
    [개요]
        OpenAPI를 이용하면 국내주식과 코스피200 지수선물/옵션, 주식선물을 거래할 수 있습니다.
        상품별로 전용 주문함수가 있으며 국내주식 주문의 경우 SendOrderCredit()함수를 이용해서 대주를 제외한 신용주문도 지원합니다.
        정정주문은 원주문에 대한 수량정정과 가격정정만 가능하며 거래구분을 변경하는 정정주문은 지원하지 않습니다.
        
    [계좌비밀번호 설정]
        잔고나 주문가능금액,수량등 계좌관련 조회나 주문전에 미리 계좌비밀번호를 설정해야 오류 알림창과 -301 오류코드없이 사용하실수 있습니다.
        계좌비밀번호 설정은 계좌비밀번호 입력창에서만 가능하며 이 입력창은 메뉴나 함수로 출력하실수 있습니다.
        메뉴이용 - 로그인후 트레이 메뉴(모니터 오른쪽 하단)에서 "계좌비밀번호 저장"선택
        함수이용 - 로그인후 OpenAPI.KOA_Functions(_T("ShowAccountWindow"), _T(""))호출
        
    [주문]
        주문을 내면 OnReceiveTRData(), OnReceiveMsg(), OnReceiveChejan()이벤트가 차례로 호출됩니다.
        주문성공 확인
        OnReceiveTRData()이벤트는 주로 조회요청후 호출되는 함수이지만 주문시에도 호출되는데 이 이벤트내부에서 주문번호를
        얻어올 수 있습니다.그런데 만일 주문이 실패하게 되면 주문번호는 공백("")으로 전달됩니다.
        각 주문함수의 리턴값이 0(성공)이여도 장 개시전 주문, 시장가 주문주문가격입력, 호가범위를 벗어난 주문등 다양한 원인으로 주문은 실패할수 있습니다.
        
        보유하고 있는 현금을 넘는 수량으로 주문한 경우 자동으로 미수로 계산되므로 [0398] 계좌증거금률 변경등록 화면을 통해 
        100%현금 주문만 가능하도록 설정할 수도 있습니다.
        이러한 경우에도 적은 비용에 대해선 비수발생가능 하며 자세한 내용은 해당화면 설명을 참고하시기 바랍니다.
        미수거래는 주문매체별로 설정 할 수 있는 것이 아니라 계좌별로 설정가능한 것이라서 OpenAPI에서도 가능한 점 알려드립니다.

        모의투자에서는 실서버와 다른 전용 계좌번호를 써야하며 주문가능, 주문제한 종목이 있고, 지정가, 시장가 주문만 가능합니다.
        이외 모의투자 운영방침은 당사 홈페이지에서 관련내용을 참고해주세요.

    [주문제한]
        국내 주식주문과 국내 주식신용주문, 선물옵션주문은 모두 1초당 5회로 제한 됩니다.
        
    [주문체결, 잔고]
        주문과 관련한 이벤트는 OnReceiveMsg(), OnReceiveTRData(), OnReceiveChejan()이렇게 3개입니다.
        OnReceiveMsg()이벤트는 주문성공, 실패 메시지를 코드와 함께 전달하므로 상세한 내용을 파악할 수 있습니다.
        OnReceiveTRData()이벤트는 주문후 호출되며 주문번호를 얻을수 있습니다.만약 이 이벤트에서 주문번호를 얻을수 없으면
        해당 주문은 실패한 것입니다.
        마지막으로 소개할 OnReceiveChejan()이벤트는 주문접수, 체결, 잔고발생시 호출되며 이 이벤트를 통해 대부분의 주문관련
        정보를 얻을 수 있습니다.
        
        주문요청에 대한 응답은 주문접수, 주문체결, 잔고수신 순서로 진행됩니다.이때 주문번호는 처음 접수?을때 한번 부여되지만 
        체결번호는 체결될때 마다 체번되서 전달됩니다. 이상의 과정을 간단히 정리하면 다음과 같습니다.
        
        주문 ---> 접수 ---> 체결1 ---> 잔고1  ---> 체결2  ---> 잔고2... ---> 체결n  ---> 잔고n
        
        주문에 대한 자세한 내용은 OnReceiveChejanData()이벤트가 호출될때 전달되는 sGubun값, sFidList값을 이용하는데 
        sGubun값은 접수와 체결시 '0'값, 잔고전달은 '1'값을 가지게 됩니다. 이값에 따라 ';'로 연결된 sFidList값도 달라지는데 이 값을
        파싱해서 GetChejanData()함수호출시 인자로 사용하시면 보다 상세한 내용을 얻을 수 있습니다.
        
        [OnReceiveChejan()이벤트로 전달되는 FID목록정리]
        
        "9201" : "계좌번호" 
        "9203" : "주문번호" 
        "9001" : "종목코드" 
        "913" : "주문상태" 
        "302" : "종목명" 
        "900" : "주문수량" 
        "901" : "주문가격" 
        "902" : "미체결수량" 
        "903" : "체결누계금액" 
        "904" : "원주문번호" 
        "905" : "주문구분" 
        "906" : "매매구분" 
        "907" : "매도수구분" 
        "908" : "주문/체결시간" 
        "909" : "체결번호" 
        "910" : "체결가" 
        "911" : "체결량" 
        "10" : "현재가" 
        "27" : "(최우선)매도호가" 
        "28" : "(최우선)매수호가" 
        "914" : "단위체결가" 
        "915" : "단위체결량" 
        "919" : "거부사유" 
        "920" : "화면번호" 
        "917" : "신용구분" 
        "916" : "대출일" 
        "930" : "보유수량" 
        "931" : "매입단가" 
        "932" : "총매입가" 
        "933" : "주문가능수량" 
        "945" : "당일순매수수량" 
        "946" : "매도/매수구분" 
        "950" : "당일총매도손일" 
        "951" : "예수금" 
        "307" : "기준가" 
        "8019" : "손익율" 
        "957" : "신용금액" 
        "958" : "신용이자" 
        "918" : "만기일" 
        "990" : "당일실현손익(유가)" 
        "991" : "당일실현손익률(유가)" 
        "992" : "당일실현손익(신용)" 
        "993" : "당일실현손익률(신용)" 
        "397" : "파생상품거래단위" 
        "305" : "상한가" 
        "306" : "하한가"
    ```

    | 타입 | 이름 | 설명 |
    | - | - | - |
    | LONG | SendOrder() |  9개 인자값을 가진 국내 주식주문 함수입니다. |
    | LONG | SendOrderFO() | 코스피지수200 선물옵션, 주식선물 전용 주문함수입니다. |
    | LONG | SendOrderCredit() | 국내주식 신용주문 전용함수입니다. 대주거래는 지원하지 않습니다. |
    | BSTR | GetChejanData() | OnReceiveChejan()이벤트가 호출될때 체결정보나 잔고정보를 얻어오는 함수입니다. |
    | void | OnReceiveChejanData() | 주문요청후 주문접수, 체결통보, 잔고통보를 수신할 때 마다 호출되며 GetChejanData()함수를 이용해서 상세한 정보를 얻을수 있습니다. |
    | void | OnReceiveMsg() | 서버통신 후 수신한 메시지를 알려줍니다. |
    | void | OnReceiveTrData() | 조회요청 응답을 받거나 조회데이터를 수신했을때 호출됩니다. |

    <br>

    + #### SendOrder()
        > 9개 인자값을 가진 국내 주식주문 함수이며 리턴값이 0이면 성공이며 나머지는 에러입니다.
          1초에 5회만 주문가능하며 그 이상 주문요청하면 에러 -308을 리턴합니다.

        [Example python](https://github.com/kimminwyk/stockOpenAPI/blob/main/test/python/CLI/%EC%A3%BC%EB%AC%B8%EA%B3%BC%20%EC%9E%94%EA%B3%A0%EC%B2%98%EB%A6%AC/kiwoom_SendOrder.py)

        + #### SeneOrder 함수 인자

            ```
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
            ```

            해당 함수는 sRQName에 의해 주식 매도, 주식 매수등의 기능이 결정되는것이 아닌, nOrderType인자로 인해 바뀌게됩니다.

            1:신규매수, 2:신규매도 3:매수취소, 4:매도취소, 5:매수정정, 6:매도정정

            | 인자 값 | 설명 |
            | - | - |
            | 1 | 신규매수 |
            | 2 | 신규매도 |
            | 3 | 매수취소 |
            | 4 | 매도취소 |
            | 5 | 매수정정 |
            | 6 | 매도정정 |

        <br>

    + #### SendOrderFO()
        > 코스피지수200 선물옵션, 주식선물 전용 주문함수입니다.
        
        <br>

    + #### SendOrderCredit()
        >  국내주식 신용주문 전용함수입니다. 대주거래는 지원하지 않습니다. 모의투자에서는 지정가 주문과 시장가 주문만 가능합니다.

        <br>

    + #### GetChejanData()
        > OnReceiveChejan()이벤트가 호출될때 체결정보나 잔고정보를 얻어오는 함수입니다.
          이 함수는 반드시 OnReceiveChejan()이벤트가 호출될때 그 안에서 사용해야 합니다.

        <br>

    + #### OnReceiveChejanData()
        > 주문요청후 주문접수, 체결통보, 잔고통보를 수신할 때 마다 호출되며 GetChejanData()함수를 이용해서 상세한 정보를 얻을수 있습니다.
        
        <br>

    + #### OnReceiveMsg()
        > 서버통신 후 수신한 메시지를 알려줍니다.
          메시지에는 6자리 코드번호가 포함되는데 이 코드번호는 통보없이 수시로 변경될 수 있습니다. 따라서 주문이나 오류관련처리를
          이 코드번호로 분류하시면 안됩니다.
        
        [Example python](https://github.com/kimminwyk/stockOpenAPI/blob/main/test/python/CLI/%EC%A1%B0%ED%9A%8C%EC%99%80%20%EC%8B%A4%EC%8B%9C%EA%B0%84%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%B2%98%EB%A6%AC/kiwoom_CommRqData.py)

        | 이름 | 설명 |
        | -- | -- |
        | sScrNo | 화면번호 |
        | sRQName | 사용자 구분명 |
        | sTrCode | TR이름 | 
        | sMsg | 서버에서 전달하는 메세지 |

        <br>

    + #### OnReceiveTrData()
        >조회요청 응답을 받거나 조회데이터를 수신했을때 호출됩니다. 
        조회데이터는 이 이벤트에서 GetCommData()함수를 이용해서 얻어올 수 있습니다.
        
        <br>

<br>

+ ### 조건검색

    + #### 설명

    ```
    [조건검색 개요]
        OpenAPI에서 제공하는 조건검색 기능은 영웅문HTS에서 작성 조건식을 불러서 사용하는 방식이며 OpenAPI에서 조건검색 수식작성이나
        수식편집은 지원하지 않습니다.
        
        조건검색 관련 6개 함수와 3개 이벤트가 제공되며 이를 이용해서 조건검색과 실시간 조건검색(반복적인 조건검색 요청없이 
        자동으로 신규종목 편입, 이탈되는 기능)을 설정할수 있습니다.
        영웅문HTS와 동일하게 실시간 조건검색은 최대 10개 조건식만 실시간 조건검색으로 요청할수 있는데 조건검색 결과가 100종목을 
        넘게 되면 실시간 조건검색을 할수가 없습니다.
        
    [조건검색 제한]
        조건검색(실시간 조건검색 포함)은 시세조회와 관심종목조회와 합산해서 1초에 5회만 요청 가능하며 1분에 1회로 조건검색 제한됩니다.
        조건검색 제한에 대한 자세한 내용은 하단을 참고해 주세요.
        
        10개 조건검색식을 한번에 모두 조회하는 프로그램이 있으며 조건검색만 요청한다고 가정해서 설명하면 다음과 같습니다.
                
    첫번째 제한조건 : 1초에 5회만 조회가능
    두번째 제한조건 : 조건별 1분당 1회로 제한(실시간 조건검색 수신에는 영향없음)
        
    09:00:00  조회 시작
        1번부터 5번 조건식은 조회성공(첫번째 제한조건, 두번째 제한조건 모두 만족)
        6번부터 10번 조건식은 조회실패(첫번째 제한조건)
        
    09:00:01 조회 재시작(1초후 재조회)
        1번부터 5번 조건식은 조회실패(두번째 제한조건)
        6번부터 10번 조건식은 조회성공(첫번째 제한조건, 두번째 제한조건 모두 만족)
        
    09:01:00 조회시작 (첫조회 1분후)
        1번부터 5번 조건식은 조회성공(첫번째 제한조건, 두번째 제한조건 모두 만족)
        6번부터 10번 조건식은 조회실패(첫번째 제한조건)
        
    09:00:01 조회 재시작(1분 1초후 재조회)
        1번부터 5번 조건식은 조회실패(두번째 제한조건)
        6번부터 10번 조건식은 조회성공(첫번째 제한조건, 두번째 제한조건 모두 만족)
                
    [실시간 조건검색]
        실시간 조건검색 결과로 100종목 이상이 검색되는 조건식은 실시간 조건검색 실행이 안됩니다.그리고 실시간 조건검색은 모두 10개 
        조건식만 사용할 수 있습니다.
    ```

    <br>

    | 타임 | 이름 | 설명 |
    | - | - | - |
    | LONG | GetConditionLoad() | 사용자 조건검색 목록을 서버에 요청합니다. 조건검색 목록을 모두 수신하면 OnReceiveConditionVer()이벤트가 호출됩니다. 조건검색 목록 요청을 성공하면 1, 아니면 0을 리턴합니다. |
    | BSTR | GetConditionNameList() | 서버에서 수신한 사용자 조건식을 조건명 인덱스와 조건식 이름을 한 쌍으로 하는 문자열들로 전달합니다. 조건식 하나는 조건명 인덱스와 조건식 이름은 '^'로 나뉘어져 있으며 각 조건식은 ';'로 나뉘어져 있습니다. 이 함수는 반드시 OnReceiveConditionVer()이벤트에서 사용해야 합니다. |
    | LONG | SendCondition() | 서버에 조건검색을 요청하는 함수로 맨 마지막 인자값으로 조건검색만 할것인지 실시간 조건검색도 할 것인지를 지정할 수 있습니다. |
    | void | SendConditionStop() | 조건검색을 중지할 때 사용하는 함수입니다. 조건식 조회할때 얻는 조건식 이름과 조건명 인덱스 쌍을 맞춰서 사용해야 합니다. |
    | LONG | SetRealReg() | 실시간 시세를 받으려는 종목코드와 FID 리스트를 이용해서 실시간 시세를 등록하는 함수입니다. |
    | void | SetRealRemove() | 실시간 시세해지 함수이며 화면번호와 종목코드를 이용해서 상세하게 설정할 수 있습니다. |
    | void | OnReceiveConditionVer() | 사용자 조건식요청에 대한 응답을 서버에서 수신하면 호출되는 이벤트입니다. |
    | void | OnReceiveTrCondition() |  조건검색 요청으로 검색된 종목코드 리스트를 전달하는 이벤트입니다. 종목코드 리스트는 각 종목코드가 ';'로 구분되서 전달됩니다. |
    | void | OnReceiveRealCondition() | 실시간 조건검색 요청으로 신규종목이 편입되거나 기존 종목이 이탈될때 마다 호출됩니다. |

    <br>

<br>

+ ### 기타함수

    + ### 종목정보관련함수

        | 타입 | 이름 | 설명 |
        | - | - | - |
        | BSTR | GetCodeListByMarket() | 국내 주식 시장별 종목코드를 ';'로 구분해서 전달합니다. |
        | BSTR | GetMasterCodeName() | 종목코드에 해당하는 종목명을 전달합니다. |
        | LONG | GetMasterListedStockCnt() | 입력한 종목코드에 해당하는 종목 상장주식수를 전달합니다. |
        | BSTR | GetMasterConstruction() | 입력한 종목코드에 해당하는 종목의 감리구분(정상, 투자주의, 투자경고, 투자위험, 투자주의환기종목)을 전달합니다. |
        | BSTR | GetMasterListedStockDate() | 입력한 종목의 상장일을 전달합니다. |
        | BSTR | GetMasterLastPrice() | 입력한 종목의 전일가를 전달합니다. |
        | BSTR | GetMasterStockState() | 입력한 종목의 증거금 비율, 거래정지, 관리종목, 감리종목, 투자융의종목, 담보대출, 액면분할, 신용가능 여부를 전달합니다. |
        | BSTR | GetBranchCodeName() | TR 조회에 필요한 회원사 정보를 회원사 코드와 회원사 이름으로 구성해서 전달합니다. |
        | BSTR | GetFutureList() | 지수선물 종목코드 리스트를 ';'로 구분해서 전달합니다. |
        | BSTR | GetActPriceList() | 지수옵션 행사가에 100을 곱해서 소수점이 없는 값을 ';'로 구분해서 전달합니다. |
        | BSTR | GetMonthList() | 지수옵션 월물정보를 ';'로 구분해서 전달하는데 순서는 콜 11월물 ~ 콜 최근월물 풋 최근월물 ~ 풋 최근월물가 됩니다. |
        | BSTR | GetOptionCode() | 인자로 지정한 지수옵션 코드를 전달합니다. |
        | BSTR | GetOptionATM() | 지수옵션 소수점을 제거한 ATM값을 전달합니다. 예를들어 ATM값이 247.50 인 경우 24750이 전달됩니다. |
        | BSTR | GetSFutureList() | 기초자산 구분값을 인자로 받아서 주식선물 종목코드, 종목명, 기초자산이름을 구할수 있습니다. |

        <br>

        + #### GetCodeListByMarket()
            > 국내 주식 시장별 종목코드를 ';'로 구분해서 전달합니다. 만일 시장구분값이 NULL이면 전체 시장코드를 전달합니다.

            <br>

    + ### 특수함수

        | 타입 | 이름 | 설명 |
        | - | - | - |
        | BSTR | KOA_Functions() | [자세한 내용은 클릭...](#koa_functions) | 

        + #### KOA_Functions()
            
            ```
            KOA_Function() 함수는 OpenAPI기본 기능외에 기능을 사용하기 쉽도록 만든 함수이며 두 개 인자값을 사용합니다. 이 함수가 
          제공하는 기능과 필요한 인자값은 공지를 통해 제공할 예정입니다.
          
          ------------------------------------------------------------------------------------------------------------------------------------
          
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
            ```

            [Example python](https://github.com/kimminwyk/stockOpenAPI/blob/main/test/python/CLI/%EA%B8%B0%ED%83%80%ED%95%A8%EC%88%98/%ED%8A%B9%EC%88%98%ED%95%A8%EC%88%98/kiwoom_KOA_Functions.py)

<br>

<br><br>

### kiwoom OpenAPI ErrorMsg

* * *

+ __[opstarter](#-opstarter)__
+ __[mfc100.dll](#-mfc100dll)__
+ __[MSVCR100.dll](#-msvcr100dll)__
+ __[QAxBase Error](#-qaxbase-error)__
+ __[ModuleNotFoundError](#-modulenotfounderror)__

<br>

### \# opstarter

```
버전 처리를 받으시려면 현재 실행 중인 OpenAPI OCX를 탑재한 프로그램을 종료하신 후 확인버튼을 눌러주시기 바랍니다.
그대로 진행시 버전처리가 정상적으로 실행되지 않습니다.
```

<br>

<p align="center"><img src="./Kiwoom-Image/opstarterOpenAPI_OCX.png"></p>

위의 경고 메세지가뜬다면 현재 실행중인 키움증권 OpenAPI창을 닫고 
KOA Studio를 연 다음 

<p align="center"><img src="./Kiwoom-Image/opstarterOpenAPI_OCX_KOA.png"></p>

__파일(F)>Open API__ 접속 누르고 로그인을 하면 위의 __opstarter 경고 메세지__ 가 또 뜨게되는데

<p align="center"><img src="./Kiwoom-Image/kiwoomOpenAPILogin.png"></p>


그때 해당 경고 메세지의 경고창을 닫지말고 

<p align="center"><img src="./Kiwoom-Image/KOAStudio.png"></p>

<br>

KOA StudioSA프로그램 종료시키고 전에나온 opstarter 경고 메세지의 확인 버튼을 누르면된다.

<p align="center"><img src="./Kiwoom-Image/KiwoomUpdateError.png"></p>

__확인 버튼을 누른 다음 업데이트 버튼이 나오는데 확인 버튼을 누르고 다시시작하면 된다.__

<br>

* * *

<br>

### \# mfc100.dll

```
mfc100.dll이(가) 없어 코드 실행을 진행할 수 없습니다. 프로그램을 다시 설치하면 이 문제가 해결될 수 있습니다.
```

<br>

<p align="center"><img src="./Kiwoom-Image/mfc100dll.png"></p>

KOAStudio를 실행하는 과정에 위의 경고창이 뜬다면 

__첫번째 방법__ 은 사전에 다운받은 OpenAPI폴더(C:\OpenAPI\)에 

<p align="center"><img src="./Kiwoom-Image/KOAStudioFile.png"></p>

KOALoader.dll, KOAStudioSA.exe두개의 파일을 이동시켜주면 정상적으로 실행이 된다.

__두번째 방법__ 은 해당 mfc100.dll을 다운로드하면 된다.

__32비트__

https://www.microsoft.com/ko-kr/download/confirmation.aspx?id=5555

__64비트__

https://www.microsoft.com/ko-KR/download/confirmation.aspx?id=14632

각 운영체제마다 다른 URL에 들어가서 접속한 후 다운로드되는 파일을 실행하면서 설치해주면 된다.

<br>

* * *

<br>

### \# MSVCR100.dll

```
MSVCR100.dll이(가) 없어 코드 실행을 진행할 수 없습니다. 프로그램을 다시 설치하면 이 문제가 해결될 수 있습니다.
```

<br>

<p align="center"><img src="./Kiwoom-Image/MSVCR100dll.png"></p>

해당 에러또한 위의 [mfc100.dll](#mfc100dll) 에러와 동일하게 따라하면 해결할 수 있다.
<br>

* * *

<br>

### \# QAxBase Error

```
QAxBase::setControl: requested control KHOPENAPI.KHOpenAPICtrl.1 could not be instantiated

QAxBase::dynamicCallHelper: Object is not initialized, or initialization failed
```

python PyQt 모듈을 사용하여 KHOPENAPI.KHOpenAPICtr1.1 Active를 불러오는 과정에 해당 오류가 난다면 

[KiwoomOpenAPI Module Install](https://www1.kiwoom.com/nkw.templateFrameSet.do?m=m1408000000)
해당 링크에 들어가 __키움 Open API+ 모듈 다운로드__ 버튼을 눌러 다운로드 하거나

사전에 다운로드했다면 OpenAPISetup.exe를 실행하여

![OpenAPISetup.exe](./Kiwoom-Image/OpenAPI-InstallShield.png)

__제거(R)__ 를 눌러 설치된 모든 기능을 제거한 다음 다시 OpenAPISetup.exe를 실행하고 설치하면된다.
<br>

* * *

<br>

### \# ModuleNotFoundError

```
ModuleNotFoundError: No module named 'PyQt5'
```

<br>

python PyQt5를 사용할때 ModuleNotFoundError 에러가 난다면 cmd 또는 터미널창에

```bash
pip install PyQt5
pip3 install PyQt5
```

본인의 pip 버전에 맞게 PyQt5를 설치하면 된다.
