# Реализовать класс Stationery
# (канцелярская принадлежность)

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__('ручка')

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('карандаш')

    def draw(self):
        print('Запуск отрисовки карандашем')


class Handle(Stationery):
    def __init__(self):
        super().__init__('маркер')

    def draw(self):
        print('Запуск отрисовки маркером')


a = Pen()
a.draw()
b = Pencil()
b.draw()
c = Handle()
c.draw()