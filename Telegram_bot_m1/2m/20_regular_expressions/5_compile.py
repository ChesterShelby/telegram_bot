"""
Можно собрать регулярное выражение в отдельный объект, который может быть использован для поиска.
Это также избавит нас от переписывания одного и того же выражения.
"""

import re

pattern = re.compile('Python')
result = pattern.findall('Python. Я занимаюсь программированием на Python!')
print(result)
result2 = pattern.findall('Я люблю язык программирования Python')
print(result2)
result3 = pattern.sub('Java', 'Я знаю язык программирования Python')
print(result3)
