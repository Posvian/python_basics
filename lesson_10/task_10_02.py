# Реализовать проект расчёта суммарного
# расхода ткани на производство одежды


from abc import abstractmethod, ABC


class Cloth(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add_to_reserve(self):
        pass


class Coat(Cloth):
    coat_reserve = 0

    def __init__(self, size, cloth_require=0):
        self.size = size
        self.cloth_require = cloth_require
        super().__init__('пальто')

    @property
    def add_to_reserve(self):
        self.cloth_require = self.size/6.5 + 0.5
        Coat.coat_reserve += self.cloth_require
        return self.cloth_require

class Costume(Cloth):
    costume_reserve = 0

    def __init__(self, height, cloth_require=0):
        self.height = height
        self.cloth_require = cloth_require
        super().__init__('костюм')

    @property
    def add_to_reserve(self):
        self.cloth_require = self.height * 2 + 0.3
        Costume.costume_reserve += self.cloth_require
        return self.cloth_require


if __name__ == '__main__':
    c1 = Coat(12)
    c2 = Coat(1)
    c3 = Coat(121)
    c1.add_to_reserve
    c2.add_to_reserve
    c3.add_to_reserve
    print(c1.cloth_require)
    print(c2.cloth_require)
    print(c3.cloth_require)
    print(Coat.coat_reserve)

    costume1 = Costume(13)
    costume2 = Costume(10)
    costume3 = Costume(40)
    costume1.add_to_reserve
    costume2.add_to_reserve
    costume3.add_to_reserve
    print(costume1.cloth_require)
    print(costume2.cloth_require)
    print(costume3.cloth_require)
    print(Costume.costume_reserve)












