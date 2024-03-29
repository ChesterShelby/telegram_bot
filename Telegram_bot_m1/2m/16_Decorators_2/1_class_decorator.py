class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func

    def __call__(self):
        print('> перед вызовом класса...', self.func.__name__)
        self.func()
        print('> после вызова класса')


@Decorator
def wrapped():
    print('функция wrapped')


print('>> старт')
wrapped()
print('>> конец')


"""
Отличие в том, что класс инициализируется при объявлении. 
Он должен получить функцию в качестве аргумента для метода __init__. Это и будет декорируемая функция.

При вызове декорируемой функции на самом деле вызывается экземпляр класса. А поскольку объект вызываемый, 
то вызывается функция __call__.
"""
