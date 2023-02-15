import re

user_mail = input('Введите адрес электронной почты: ')   # example@example.ru
if re.match(r'[a-z]+@[a-z]+\.[a-z]{2,}', user_mail):
    print('Почта введена верно')
else:
    print('Почта неверна')

"""
В данной реализации мы говорим, что проверять стоит только по английскому алфавиту, 
в диапазоне от a до я в нижнем регистре. Если проверять и верхний и нижний регистр, 
то можно указать [a-zA-Z], а если добавить и русский язык, то [a-zA-Zа-яёА-ЯЁ]. 
При использовании русского языка, следует не забывать, 
что буква ё не входит в диапазон от а до я и ее необходимо добавлять отдельно.
"""