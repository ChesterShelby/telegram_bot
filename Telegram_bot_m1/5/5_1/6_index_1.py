s = 'Python'

for i in range(len(s)):
    print(s[i], i)

print()

for i in range(len(s) * -1, 0):
    print(s[i], i)

print()

print(s[-6], s[0])
print(s[len(s)-1], s[-1])
