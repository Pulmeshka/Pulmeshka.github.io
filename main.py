from pywebio.output import *
from pywebio.input import *
from pywebio import start_server
def main():
    toast('10.11- обновление')
    choose = select('Привет, сдесь ты можешь выбрать игровой режим, чтобы зайти в другой режим или вы нашли баг(если баг отправте отзыв в телеграм канал @PulmeshkaNewsBot)-"перезагрузите страницу"', ['Смешнные сообщение', 'Чат бот', 'Список багов', 'мини-тест', 'кастом сообщение', 'кликер', 'список обновлений'])
    if choose == 'Смешнные сообщение':
        import SmileMessage
    elif choose == 'Чат бот':
        import ChatBot
    elif choose == 'Список багов':
        import BagsList
    elif choose == 'мини-тест':
        toast('Перезагрузите страницу...')
        toast('Скоро...')
    elif choose == 'кастом сообщение':
        import CustomMessage
    elif choose == 'кликер':
        import clicker
    elif choose == 'список обновлений':
        import UpdateList
start_server(main, debug=True, port=8080)