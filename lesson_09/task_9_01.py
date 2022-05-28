# Создать класс TrafficLight (светофор)

import time
from itertools import cycle


class TrafficLight:
    colors_time = {'красный': 7, 'желтый': 2, 'зеленый': 5}

    def __init__(self, color='красный'):
        self.__color = color

    def state(self):
        return f'Цвет светофора {self.__color}'

    def running(self, duration):
        i = 0
        for color in cycle(self.colors_time.keys()):
            self.__color = color
            print(self.state())
            time.sleep(self.colors_time[color])
            i += self.colors_time[color]
            if self.__color == 'зеленый':
                self.__color = 'желтый'
                print(self.state())
                time.sleep(self.colors_time[self.__color])
                i += self.colors_time[self.__color]
            if i >= duration or i >= 50:
                break


a = TrafficLight()
a.running(20)


