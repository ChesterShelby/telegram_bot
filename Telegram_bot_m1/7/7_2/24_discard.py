"""
Метод discard() полезен, потому что он удаляет конкретный элемент и не возвращает ошибку,
если тот не был найден во множестве.
"""

set1 = {1, 3, 4, 'a', 'p'}
set1.discard('a')
print(set1)
