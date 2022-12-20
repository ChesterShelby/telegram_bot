word = 'hello world'
print(word.index('o'))
print(word.index('o'))
print(word.rindex('o'))

"""
Основное отличие состоит в том, что Python find() выдает -1, если не может найти подстроку, 
тогда как index() генерирует исключение ValueError.
"""