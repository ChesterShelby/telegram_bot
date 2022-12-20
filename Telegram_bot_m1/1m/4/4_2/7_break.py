result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break
    result += num
print(result)
