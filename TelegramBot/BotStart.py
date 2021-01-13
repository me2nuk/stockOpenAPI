from telegram.ext import CommandHandler
from telegram.ext import Updater
import Telegram_CommandList
import __setting__

TelegramBotStart = Updater(token=__setting__.__BotTelegramToken__,)
MessageRecvUpdate = TelegramBotStart.dispatcher


class TelegramBot_Run:
    def __init__(self) -> None:

        self.CountCmd = len(Telegram_CommandList.BotStartCommand)

    def __str__(self) -> str:
        return f"<TelegramBot(Cmd_Count=<[{self.CountCmd}])>"

    def Cmd_Add(self):
        """
        <Command variable> = CommandHandler(<command>, self.TelegramStart._<command>)
        """
        global MessageRecvUpdate


        for TelegramCommand , TelegramSendText in Telegram_CommandList.BotStartCommand.items():
            CommandAdd = CommandHandler(TelegramCommand, (lambda Telegram_UpdateChat_id, NetxSend_MessAge: NetxSend_MessAge.bot.send_message(chat_id=Telegram_UpdateChat_id.effective_chat.id, text=TelegramSendText)))
            MessageRecvUpdate.add_handler(CommandAdd)

    def bot_start(self) -> bool:
        """
        TelegramBot Start
        """
        global TelegramBotStart

        try:
            TelegramBotStart.start_polling()
            return True
        except:
            return False