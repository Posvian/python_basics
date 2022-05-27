# Реализуйте класс Car (self.name)

class Car:

    def __init__(self, color, name, is_police=None):
        self._speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self, up_to_speed):
        print(f'{self.name} поехала, стартовав со скорости {self._speed}')
        self._speed += up_to_speed
        print(f'{self.name} разогналась до скорости {self._speed}')

    def stop(self):
        print(f'{self.name} ехала со скоростью {self._speed}')
        self._speed = 0
        print(f'{self.name} остановилась')

    def turn(self, direction):
        turning_speed = 5
        if self._speed < turning_speed:
            self._speed += turning_speed
            print(f'{self.name} разогналась до {self._speed} и повернула на {direction}')
        else:
            self._speed = turning_speed
            print(f'{self.name} притормозила до {self._speed} и повернула на {direction}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self._speed}')


class TownCar(Car):
    def __init__(self, color, speed_limit=60):
        self._speed_limit = speed_limit
        super().__init__(color, 'TownCar')

    def show_speed(self):
        if self._speed > self._speed_limit:
            print(f'{self.name} едет со скоростью {self._speed}, ВНИМАНИЕ')


class WorkCar(Car):
    def __init__(self, color, speed_limit=40):
        self._speed_limit = speed_limit
        super().__init__(color, 'WorkCar')

    def show_speed(self):
        if self._speed > self._speed_limit:
            print(f'{self.name} едет со скоростью {self._speed}, ВНИМАНИЕ')


class SportCar(Car):
    def __init__(self, color):
        super().__init__(color, 'SportCar')


class PoliceCar(Car):
    def __init__(self, color):
        super().__init__(color, 'PoliceCar', is_police=True)


a = TownCar('black')
a.car_go(61)
a.show_speed()
a.turn('налево')
a.stop()

b = WorkCar('brown')
b.car_go(30)
b.show_speed()
c = SportCar('red')
c.car_go(100)
c.show_speed()
d = PoliceCar('blue')
d.car_go(90)
d.show_speed()
print(d.is_police)
print(a.is_police)