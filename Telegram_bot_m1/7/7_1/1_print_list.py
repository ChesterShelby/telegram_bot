a = [1, 2, 3, 'a', True]

for i in a:
    print(i)

print()

for i in range(len(a)):
    print(a[i])

print()

print(*a)   # распаковка списка(выводит без квадратных скобок)
print(a)
