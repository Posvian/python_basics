# Написать декоратор для логирования(вывод
# в консоль) типов позиционных аргументов
# функции:


def type_logger(func):
    def temp(*args, **kwargs):
        print(f'Call for: {func.__name__}')
        if args:
            for arg in args:
                print(f'{arg}: {type(arg)}')
        if kwargs:
            for arg in kwargs:
                print(f"'{arg}' = {kwargs[arg]}: {type(kwargs[arg])}")
        rezult = func(*args, **kwargs)
        print(f'Rezult: {rezult}  type: {type(rezult)}')
    return temp


@type_logger
def render_input(*args, **kwargs):
    return 1


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(5)
render_input(1, a=2, b=True, c="q")
