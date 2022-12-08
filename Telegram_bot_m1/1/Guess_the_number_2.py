secret_number = 5                               # указываем секретное число
attempts = 3                                    # Количество попыток

print('Это программа угадай число. У Вас 3 попытки,'
      ' чтобы постараться отгадать число.')


while attempts > 0:
    print('Попыток ' + str(attempts))               # выводим попытки
    attempts -= 1                         # уменьшаем попытки
    user_number = input('Введите ваше число: ')     # Ввод пользователя
    user_number = int(user_number)                  # преобразование из строки в число
    if user_number > secret_number:                 # условие сравнивает число с загаданным.
        print('Загаданное число меньше')
    if user_number < secret_number:
        print('Загаданное число больше')
    if user_number == secret_number:
        print('Вы угадали!')
