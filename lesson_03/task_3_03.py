#Написать функцию thesaurus(), принимающую
# в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи —
# первые буквы имен, а значения — списки,
# содержащие имена, начинающиеся с соответствующей
# буквы.

def thesaurus(*args):
    dict_1 = {}
    for idx in args:
        arg = []
        if idx[0] in dict_1:
            dict_1[idx[0]].append(idx)
        else:
            arg.append(idx)
            dict_1[idx[0]] = arg
    dict_2 = {}
    for key in sorted(dict_1):
        dict_2[key] = dict_1.get(key)
    return dict_2


result = thesaurus("Иван", "Мария", "Петр", "Илья", "Артем", "Вадим", "Анатолий")

print('{')
for key, value in result.items():
    print(f'"{key}": {value}')

print('}')
