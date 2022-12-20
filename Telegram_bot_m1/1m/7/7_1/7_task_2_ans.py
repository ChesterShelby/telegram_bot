a = ['hello', 'world']
b = ' '.join(a)
c = ''
for letter in a:
    c += letter
    c += ' '
print(b)
print(c)
