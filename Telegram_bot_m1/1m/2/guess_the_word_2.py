print("Попробуй угадать слово по буквам!")

secret_word = "машина"
attempts = 5
user_chars = []

for i in range(len(secret_word)):
    print("*", end=' ')

print()
user_char = input('Введите букву ')

if user_char not in user_chars:
    user_chars.append(user_char)

for char in secret_word:
    if char in user_chars:
        print(char, end=' ')
    else:
        print('*', end=' ')
