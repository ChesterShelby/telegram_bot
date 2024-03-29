import re

user_mail = input('Введите адрес электронной почты: ')   # example@example.ru
if re.match(r'\w+@\w+\.\w{2,}', user_mail):
    print('Почта введена верно')
else:
    print('Почта неверна')

"""
Регулярное выражение в примере почти такое же, за исключением того, 
что доменная зона может иметь разную длину(ru, com и т.д). Поэтому мы указали \w{2,}, 
что значит любой буквенный символ от 2 и более раз.
"""