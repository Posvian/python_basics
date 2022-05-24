# Есть два списка: tutors - имена
# учеников, groups - названия их
# классов.Необходимо реализовать генератор или
# функцию - генератор, возвращающий кортежи вида
# '(<tutor>, <group>)'.

def my_func(tutors, groups):
    i = 0
    while i < len(tutors):
        if i >= len(groups):
            yield tutors[i], None
        else:
            yield tutors[i], groups[i]
        i += 1


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen1 = my_func(tutors, groups)
print('Результат где учеников меньше: ')
print(type(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

gen2 = my_func(tutors=['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'],
               groups=['9А', '7В', '9Б', '9В'])

print('Результат где учеников больше: ')
print(type(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
