def decorator_with_args(func):
    print('> декоратор с аргументами...')

    def decorated(c, d):
        print('до вызова функции', func.__name__)
        ret = func(c, d)
        print('после вызова функции', func.__name__)
        return ret

    return decorated


@decorator_with_args
def add(a, b):
    print('функция 1')
    return a + b


@decorator_with_args
def sub(a, b):
    print('функция 2')
    return a - b


print('>> старт')
r = add(10, 5)
print('r:', r)
g = sub(10, 5)
print('g:', g)
print('>> конец')
