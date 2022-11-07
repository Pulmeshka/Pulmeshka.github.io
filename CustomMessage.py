from pywebio.output import *
from pywebio.input import *

while True:
    message = input('Введиет как будет выглядеть ваше сообщение')
    message2 = input('Введите заголовок сообщение')
    popup(message2, message)