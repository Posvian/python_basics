# Реализовать класс Road (дорога)

class Road:

    cm_in_meter = 1000

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_mass(self, kilo_on_one_cm, asphalt_thickness):
        rez = self._length * self._width * kilo_on_one_cm * asphalt_thickness / self.cm_in_meter
        return f'{self._length} м*{self._width} м*{kilo_on_one_cm} кг*{asphalt_thickness} см = {int(rez)} т'


road1 = Road(5000, 20)
road2 = Road(2000, 15)
road3 = Road(1000, 10)
print(road1.count_mass(25, 5))
print(road1.count_mass(30, 15))
print(road1.count_mass(3, 10))
print(road2.count_mass(3, 10))
print(road3.count_mass(3, 10))