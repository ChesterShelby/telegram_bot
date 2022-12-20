a = {2: 1}
b = a.copy()   # создаем копию
c = a
print(b)
print(b is a)  # b не является a
print(c is a)  # c является a
