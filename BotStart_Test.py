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

import BotStart

TelegramBot = BotStart.TelegramBot_Run()

def request(url):
    return __import__("requests").get(url).text

TelegramBot.FunctionCmd_Add('ab',request, args = ('https://www.google.com'))
TelegramBot.bot_start()