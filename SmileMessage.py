from pywebio.output import *
from pywebio.input import *

while True:
    text = radio('Выбери одно из уведомлений', ['хи-хи-хи ха', 'пон, да?', 'реклама', 'песенка'])
    if text == 'хи-хи-хи ха':
        toast('ХИ-ХИ-ХИ ХА😂')
    elif text == 'пон, да?':
        toast('Слыш я тут крутой, пон, да?')
    elif text == 'секрет':
        toast('Ноу секрет')
    elif text == 'реклама':
        popup('РЕКЛАМА📺', 'Подпишись на наш телеграм канал @PulmeshkaNewsBot')
    elif text == 'песенка':
        popup('Music🎧', 'My name is ЧИКИ\nчики-чики-чики\nmy name is ЧА-ЧА\nclop-clop ЧА-ЧА-ЧА\nmy name is БУМ-БУМ\nБУМ-БУМ-БУМ\nmy name is ля-ля\nЛЯ-ЛЯ ЛЯ-ЛЯ-ЛЯ')
    else:
        popup('вам пришло сообщение', 'АЛЁ ТЫ НЕ ОБНАГЛЕЛ, ДАЖЕ НЕ ВЫБРАЛ НИЧЕГО')