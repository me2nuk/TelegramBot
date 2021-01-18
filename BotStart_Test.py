"""import BotStart

TelegramBot = BotStart.TelegramBot_Run()
TelegramBot.Cmd_Add()
TelegramBot.bot_start()
"""
"""import BotStart

TelegramBot = BotStart.TelegramBot_Run()

def test():
    return 'HelloWorld'

TelegramBot.FunctionCmd_Add('help', test)
TelegramBot.bot_start()"""
"""import BotStart

TelegramBot = BotStart.TelegramBot_Run()

def test(url):
    return __import__("requests").get(url).text[:400]

TelegramBot.FunctionCmd_Add('help', test, args=('https://www.naver.com'))
TelegramBot.bot_start()"""
"""def test():
    print('hello')

a = BotStart.TimeStartBotSend()
a._Runh(test)
a.TimeStart()"""

"""import TelegramBot as TelegramBot_

TelegramBot = TelegramBot_.TelegramBot_Run()

def request(url):
    return url

def msg(msga):
    print("ab : ",msga)

TelegramBot.FuncCmd_Add('ab',request, args = ('https://www.google.com'), _FuncFind = msg)
TelegramBot.bot_start()
"""

"""from telegram.ext import Updater
from telegram.ext import CommandHandler

BotToken = __import__("__setting__").__BotTelegramToken__

updater = Updater(token=BotToken, use_context=True)
dispatecher = updater.dispatcher

def start(update, context):
    print(context.args)
    context.bot.send_message(chat_id = update.effective_chat.id, text="hello")

start_handler =CommandHandler('start',start)

dispatecher.add_handler(start_handler)

updater.start_polling()
updater.idle()"""