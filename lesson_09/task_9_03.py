# Реалself=Noneласс Worker (работник)

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return f'Полная зарплата на позиции {self.position} составляет {total_income} рублей.'


director = Position('Алексей', 'Посвянский', 'директор', 50000, 100000)
print(director.name)
print(director.surname)
print(director.position)
print(director.get_full_name())
print(director.get_total_income())

programmer = Position('Дмитрий', 'Посвянский', 'програмист', 200000, 100000)
print(programmer.get_full_name())
print(programmer.get_total_income())
