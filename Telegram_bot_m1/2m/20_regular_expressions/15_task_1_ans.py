import re

numbers = ['9999999999', '8999999999', '999999-999', '99999_9999']

for num in numbers:
    number = re.match(r'[8-9]{1}[0-9]{9}', num)
    if number and len(num) == 10:
        print('Номер верный', num)
    else:
        print('Номер неверный', num)
