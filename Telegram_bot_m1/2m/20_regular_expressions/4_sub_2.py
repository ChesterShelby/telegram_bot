import re

sentence = 'Java. Я занимаюсь программированием на Java!'
result = re.sub(r'Java', 'Python', sentence)
print(result)
