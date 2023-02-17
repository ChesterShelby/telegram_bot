"""
re.split(шаблон, строка, максимальное кол-во разделений=0)
Максимальное количество разделений, является опциональным и если мы его не укажем,
то разбиение строки будет столько раз, сколько совпал шаблон с нашей строкой.
"""

import re

sentence = 'Python. Я занимаюсь программированием на Python!'
result1 = re.split(r'Python', sentence)
print(result1)
print(sentence.split('Python'))

# result2 = re.split(r'Python', sentence, maxsplit=1)
# print(result2)
