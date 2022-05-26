# Реализовать класс Stationery
# (канцелярская принадлежность)

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашем')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


a = Pen('Ручка')
a.draw()
b = Pencil('Карандаш')
b.draw()
c = Handle('Маркер')
c.draw()