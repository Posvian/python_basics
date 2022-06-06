# Реализовать класс «Дата»

class DateInitError(Exception): pass

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_create(cls, date):
        sep_date = date.split('-')
        try:
            day = int(sep_date[0])
            month = int(sep_date[1])
            year = int(sep_date[2])
        except ValueError:
            print('дата должна быть введена в формате день-месяц-год')
        else:
            if Data.date_verified(day, month, year):
                return Data(day, month, year)
            else:
                raise DateInitError


    @staticmethod
    def date_verified(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.year}.{self.month}.{self.day}'


if __name__ == '__main__':
    a = Data.date_create("31-12-2021")
    print(a)
    b = Data.date_create("31-12--2021")
    try:
        c = Data.date_create("32-12-2021")
    except DateInitError:
        print('Дата не прошла валидацию. Введите дату в формате день-месяц-год')
    else:
        print(c)
    d = Data.date_create("31-11-2025")
    print(d)
    e = Data.date_create("21-11-2021")
    print(e)