# TelegramBot

<br>

![TelegramBot ProFile](./Image/PrediCtionMoneyBotProFile.jpg)

__태그 : @PrediCtionMoneyBot__

<br>

### 1. 텔레그램 봇 반응 커멘드 추가

텔레그램 봇이 /start 같은 커멘드에 반응하기 위해선
./Telegram_CommandList.py 파일의 BotStartCommand 변수를 추가하면 됩니다.

예시
```py
BotStartCommand = {
    'start':'Telegram Bot Start !',
    'help':'Hello User!'
}
```

__/start__ , __/help__ 커멘드를 추가한 다음 

```py
import BotStart

TelegramBot = BotStart.TelegramBot_Run()
TelegramBot.Cmd_Add()
TelegramBot.bot_start()
```

위 코드처럼 봇을 스타트시키면 __/start__ 과 __/help__ 명령어에 반응하게 됩니다.

* * *

<br>

### 2. 텔레그램 봇 반응시 함수 실행

텔레그램 봇을 실행하는 도중 특정 커맨드를 입력하면 함수를 실행시키기 위해

```py
import BotStart

TelegramBot = BotStart.TelegramBot_Run()

def test():
    return 'HelloWorld'

TelegramBot.FunctionCmd_Add('help', test)
#TelegramBot.FunctionCmd_Add(<원하는 반응 커멘드>, <실행시키고자 하는 함수 네임>)
TelegramBot.bot_start()
```

* * *

<br>

### 3. 텔레그램 봇 일정 시간마다 함수 실행

<br>

+ ___s(self, s, FunctionObject) -> None:__

    + (s)초마다 실행

    <br>

+ ___m(self, m , FunctionObject) -> None:__

    + (m)분마다 실행
    
    <br>

+ ___h(self, h, FunctionObject) -> None:__

    + (h)시간마다 일정하게 실행
    
    <br>

+ ___day(self, datetime, FunctionObject) -> None:__

    + 날마다 (datetime)시간대에 실행
    
    <br>

+ ___Runh(self,FunctionObject) -> None:__

    + 한시간마다 실행
    
    <br>

텔레그램 봇을 이용하여 24시간마다 hello 이라는 메세지를 전송하는 기능을 원한다면

```py
import BotStart

chat_id = "my telegram chat_id"

def MessageSend():
    global chat_id

    TelegramBot = _OneSendMsg()
    TelegramBot.Chat_idSend(chat_id, "hello")


a = BotStart.TimeStartBotSend()
a._day("00:00",MessageSend)
a.TimeStart()
```

이런식으로 _OneSendMsg 클래스를 이용하여 호출하는 함수를 만든 다음
TimeStartBotSned 클래스로 00:00시 마다 MessageSend 함수를 실행시킵니다.