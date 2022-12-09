print('and')
print('|   x    |   y   |   F   |')
for x in range(2):
    for y in range(2):
        if x and y:
            print(f'|   {x}    |   {y}   |   1   |')
        else:
            print(f'|   {x}    |   {y}   |   0   |')

print()
print('or')
print('|   x    |   y   |   F   |')
for x in range(2):
    for y in range(2):
        if x or y:
            print(f'|   {x}    |   {y}   |   1   |')
        else:
            print(f'|   {x}    |   {y}   |   0   |')


print()
print('not')
print('|   x    |   !x   |')
for x in range(2):
    if not x:
        print(f'|   {x}    |    1   |')
    else:
        print(f'|   {x}    |    0   |')

print()
print('==')
print('|   x    |   y   |   F   |')
for x in range(2):
    for y in range(2):
        if x == y:
            print(f'|   {x}    |   {y}   |   1   |')
        else:
            print(f'|   {x}    |   {y}   |   0   |')

input()
