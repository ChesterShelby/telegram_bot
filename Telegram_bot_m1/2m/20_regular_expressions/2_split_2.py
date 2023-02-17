import re

sentence = 'Я изучаю регулярные выражения, которые помогают при работе с текстом.'
result = re.split(r',', sentence)
print(result)
