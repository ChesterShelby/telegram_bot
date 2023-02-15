"""
Давайте попрактикуемся и попробуем найти email в строке. Предположим мы имеем строку:
sentence = 'Моя почта example@example.ru'
Из данной строки мы видим, что для поиска нам однозначно не подходит match, так как он ищет только в начале строки.
Если бы мы должны были найти более одной почты, то нам подошел бы только findall.
В данном же случае мы можем использовать search.
"""

import re

sentence = 'Моя почта example@example.ru'

r = re.search(r'(\w+)@(\w+).(\w{2})', sentence)
print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.group(3))

"""
В данном примере мы применили группировку, для того чтобы могли по отдельности вывести как имя почты до символа @, 
так и доменного имени и доменной зоны. Из нового для нас здесь мы видим только \w{2}, что означает, 
что любой буквенный символ ровно 2 раза.
"""
