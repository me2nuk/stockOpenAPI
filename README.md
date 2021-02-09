# 키움증권 OpenApi

<br>

## What is it

이 프로젝트는 키움증권 OpenAPI를 편하게 사용하기 위해 만들어졌으며,
다양한 가이드와 키움증권 OpenAPI예시 또는 사용법이 있습니다.

| name | Explanation | 현재 상태 |
| - | - | - |
| [test](https://github.com/kimminwyk/PrediCtionMoney/blob/main/test/) | 키움증권 OpenAPI를 사용한 코드가 작성되어있습니다. | 작성중(X) |
| Kiwoom-Image | 키움증권 가이드를 작성하면서 사용된 이미지 파일 | 작성중(X) |
| scripts | 키움증권 OpenAPI 수익을 위해 트레이닝 코드가 들어갈 __예정__ 입니다. | 작성중(X) |


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
        + [로그인 버전처리](#로그인-버전처리)
            + [CommConnect()](#commconnect)
            + [CommTerminate()](#commterminate)
            + [GetConnectState()](#getconnectstate)
            + [GetLoginInfo()](#getlogininfo)
            + [OnEventConnect](#oneventconnect)
            + [OnReceivMsg](#onreceivmsg)
        + [조회와 실시간데이터처리](#조회와-실시간데이터처리)
        + [주문과 잔고처리](#주문과-잔고처리)
        + [조건검색](#조건검색)
        + [기타함수](#기타함수)
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

        [Example python](https://github.com/kimminwyk/PrediCtionMoney/blob/main/test/python/CLI/kiwoom_CommConnect.py)

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

        [Example python](https://github.com/kimminwyk/PrediCtionMoney/blob/main/test/python/CLI/kiwoom_GetConnectState.py)

        GetConnectState 반환값(return)

        | 1 | 0 |
        | - | - |
        | 연결| 연결안됨 |

        <br>

    + #### GetLoginInfo()

        > 로그인 후에만 사용할 수 있으며 인자값에 따라 다양항 정보를 얻을 수 있습니다. 

        [Example python](https://github.com/kimminwyk/PrediCtionMoney/blob/main/test/python/CLI/kiwoom_GetLoginInfo.py)

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

        [Example python](https://github.com/kimminwyk/PrediCtionMoney/blob/main/test/python/CLI/kiwoom_OnEventConnect.py)

        | nErrCode | 상태 |
        | --------- | --- |
        | 0 | 로그인 성공 |
        | -100 | 사용자 정보교환 실패 |
        | -101 | 서버접속 실패 |
        | -102 | 버전처리 실패 |

        <br>

    + #### OnReceiveMsg()

        > 서버통신한 다음 수신한 메시지를 알려줍니다.

        [Example python](https://github.com/kimminwyk/PrediCtionMoney/blob/main/test/python/CLI/kiwoom_OnReceiveMsg.py)

        | 이름 | 설명 |
        | -- | -- |
        | sScrNo | 화면번호 |
        | sRQName | 사용자 구분명 |
        | sTrCode | TR이름 | 
        | sMsg | 서버에서 전달하는 메세지 |

<br>

+ ### 조회와 실시간데이터처리

    + 설명

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

    + #### CommRqData()

        > 

<br>

+ ### 주문과 잔고처리

__아직 작성중__

<br>

+ ### 조건검색

__아직 작성중__

<br>

+ ### 기타함수

__아직 작성중__

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