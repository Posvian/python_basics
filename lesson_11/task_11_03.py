# Создайте собственный класс-исключение,
# используемый для проверки содержимого
# списка на наличие только чисел.

class IsNotNumber(ValueError): pass


lst1 = []


def is_digit(a):
    if a.isdigit():
        return int(a)
    else:
        raise IsNotNumber


while True:
    a = input('Введите число для добавления в список. Если хотите остановить программу введите stop.')
    if a == 'stop':
        break
    try:
        a = is_digit(a)
    except IsNotNumber:
        print('Введите число')
    else:
        lst1.append(a)
