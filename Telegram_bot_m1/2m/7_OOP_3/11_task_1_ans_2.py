#   travka - обозначает плотоядное животное или травоядное
#   homea - домашнее животное или дикое

class Animal:
    def __init__(self, name, color, travka, homea="Домашнее"):
        self._color = color
        self._travka = travka
        self.homea = homea
        self.name = name
        self.__walk()

    def __walk(self):
        print(f'{self.name} идет куда-то...')

    @property
    def color(self):
        return f'Это животное {self._color}'

    @color.setter
    def color(self, val):
        self._color = val


Animal1 = Animal("Барсик", "Разного", 'плотоядное')
print(Animal1.homea)
# Animal1._Animal__walk()
a = Animal1.color
print(a)
