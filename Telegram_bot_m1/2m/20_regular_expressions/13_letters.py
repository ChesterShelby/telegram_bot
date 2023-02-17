import re

result1 = re.findall(r'[яи]\w+', 'Я изучаю язык программирования Python')
print(result1)
result2 = re.findall(r'\b[яи]\w+', 'Я изучаю язык программирования Python')
print(result2)
