# 키움증권 OpenApi

<br>

+ [키움 Open API+](https://www1.kiwoom.com/nkw.templateFrameSet.do?m=m1408000000)

+ [키움 OpenAPI+ 개발가이드 PDF](https://download.kiwoom.com/web/openapi/kiwoom_openapi_plus_devguide_ver_1.5.pdf)

+ [키움 OpenAPI 교육 VOD](https://www.howtostock.com/acdm/getLectureList.action?COUR_SEQ=49&CURR_SEQ=218)

<br><br>

### Kiwoom OpenAPI Contents

* * *

<br>

+ [키움증권 OpenApi](#키움증권-openapi)

    + [Kiwoom OpenAPI Contents](#kiwoom-openapi-contents)
    + [Kiwoom OpenApi](#kiwoom-openapi)
    + [OpenAPI Step](#openapi-step)
    + [kiwoom OpenAPI ErrorMsg](#kiwoom-openapi-errormsg)

<br>

### Kiwoom OpenApi

* * *

<br>

![OpenApi](./Kiwoom-Image/OpenApiMainPage.png)

<br>

### OpenAPI Step

* * *

<br>

+ ##### Step1

   + OpenApi 서비스 사용 신청

+ ##### Step2

    + 키움 Open API+ 모듈 다운로드

+ ##### Step3

    + 개발가이드
    + KOA Studio
    + 교육 VOD
    + 자료실

+ ##### Step4

    + 상시 모의투자 신청

<br>

### kiwoom OpenAPI ErrorMsg

* * *

<br>

### opstarter

```
# 버전 처리를 받으시려면 현재 실행 중인 OpenAPI OCX를 탑재한 프로그램을 종료하신 후 확인버튼을 눌러주시기 바랍니다.
그대로 진행시 버전처리가 정상적으로 실행되지 않습니다.
```

<br>

![OpenAPIErrorkiwoomOpenAPI](./Kiwoom-Image/opstarterOpenAPI_OCX.png)

위의 경고 메세지가뜬다면 현재 실행중인 키움증권 OpenAPI창을 닫고 
KOA Studio를 연 다음 

![OpenAPIErrorkiwoomOpenAPI-1](./Kiwoom-Image/opstarterOpenAPI_OCX_KOA.png)

<br><br>

### mfc100.dll

```
mfc100.dll이(가) 없어 코드 실행을 진행할 수 없습니다. 프로그램을 다시 설치하면 이 문제가 해결될 수 있습니다.
```

<br>

![OpenApiErrormfcdll](./Kiwoom-Image/mfc100dll.png)

KOAStudio를 실행하는 과정에 위의 경고창이 뜬다면 

__첫번째 방법__ 은 사전에 다운받은 OpenAPI폴더(C:\OpenAPI\)에 

![OpenApiFile](./Kiwoom-Image/KOAStudioFile.png)

KOALoader.dll, KOAStudioSA.exe두개의 파일을 이동시켜주면 정상적으로 실행이 된다.

__두번째 방법__ 은 해당 mfc100.dll을 다운로드하면 된다.

__32비트__

https://www.microsoft.com/ko-kr/download/confirmation.aspx?id=5555

__64비트__

https://www.microsoft.com/ko-KR/download/confirmation.aspx?id=14632

각 운영체제마다 다른 URL에 들어가서 접속한 후 다운로드되는 파일을 실행하면서 설치해주면 된다.

<br><br>

### MSVCR100.dll

```
MSVCR100.dll이(가) 없어 코드 실행을 진행할 수 없습니다. 프로그램을 다시 설치하면 이 문제가 해결될 수 있습니다.
```

<br>

![OpenApiMSVCR100dll](./Kiwoom-Image/MSVCR100dll.png)

해당 에러또한 위의 [mfc100.dll](#mfc100dll) 에러와 동일하게 따라하면 해결할 수 있다.