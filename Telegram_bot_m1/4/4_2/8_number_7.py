n = int(input())
d = n
flag = False

while n != 0:
    last_digit = n % 10
    if last_digit == 7:
        flag = True
        break
    n //= 10

if flag:
    print('Число', d, 'содержит цифру 7')
else:
    print('Число', d, 'не содержит цифру 7')
