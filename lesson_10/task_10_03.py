# Реализовать программу работы с органическими
# клетками, состоящими из ячеек

class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            raise ValueError('Cell number should be above zero')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, number_in_row):
        number_of_rows = self.number // number_in_row
        cells_in_last_row = self.number % number_in_row
        cell = '*'
        cells_in_row = cell * number_in_row + '\n'
        return f'{cells_in_row * number_of_rows + cell * cells_in_last_row}'



if __name__ == '__main__':
    c1 = Cell(1)
    print(c1.make_order(5))
    c2 = Cell(5)
    print(c2.make_order(5))
    c3 = c1 + c2
    print(c3.number)
    print(type(c3))
    print(c3.make_order(5))
    c4 = c2 - c1
    print(c4.number)
    print(type(c4))
    print(c4.make_order(5))
    c5 = c2 * c3
    print(c5.number)
    print(type(c5))
    print(c5.make_order(5))
    c7 = Cell(3)
    c6 = c5 // c7
    print(c6.number)
    print(type(c6))
    print(c6.make_order(5))
