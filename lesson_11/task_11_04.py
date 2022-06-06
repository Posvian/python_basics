# Реализовать проект «Операции с
# комплексными числами».

class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex((self.x * other.x - self.y * other.y), (self.x * other.y + self.y * other.x))

    def __str__(self):
        return '{:-d}{:+d}j'.format(self.x, self.y)

a = Complex(2, 3)
b = Complex(-1, 1)

c = a + b
print(c)
print(type(c))

d = a - b
print(d)
print(type(d))

e = a * b
print(e)
