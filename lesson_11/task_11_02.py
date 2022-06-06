# Создать собственный класс-исключение,
# для обработки ситуации деления
# на ноль и функцию, выполняющую
# деление двух чисел

class MyZeroDivisionError(ZeroDivisionError): pass


def func(x, y):
    if y != 0:
        return x/y
    else:
        raise MyZeroDivisionError


if __name__ == '__main__':
    try:
        a = func(12, 3)
    except MyZeroDivisionError:
        print('Делить на ноль нельзя')
    else:
        print(a)

    try:
        b = func(12, 0)
    except MyZeroDivisionError:
        print('Делить на ноль нельзя')
    else:
        print(b)

    try:
        c = func(15, 3)
    except MyZeroDivisionError:
        print('Делить на ноль нельзя')
    else:
        print(c)


