class Parent:
    def say_hello():
        print('Привет я метод родительского класса')


class Children(Parent):
    def say_hello():
        print('Привет я метод дочернего класса')


child = Children
child.say_hello()
