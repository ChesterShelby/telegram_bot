class Test(int):
    def __init__(self, num) -> None:
        super().__init__()
        self.num = num

    def __add__(self, num2):
        return f'{self.num * num2}'


a = Test(5)
print(a + 10)
