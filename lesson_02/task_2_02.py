# Дан список строк. Выполнить обработку списка
# (смотри текст задания) и сформировать на его
# основе строку

# Создать новый список и наполнить его элементами по
# схеме:
# Обособить каждое целое число (исходного списка)
# кавычками (добавить элемент списка: строку-кавычку
# до и после элемента списка, являющегося числом)

# дополнить это число нулём до двух целочисленных
# разрядов
# Например исходный список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'].
# Тогда новый список: ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"',
# '+05', '"', 'градусов'].
#
# Новый список вывести на экран

# ПЕРВАЯ ПРОВЕРКА
lst1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
lst2 = []
for idx in lst1:
    if '.' in idx:
        lst2.append(idx)
    elif idx.isdigit():
        lst2.append('"')
        idx = idx.zfill(2)
        lst2.append(idx)
        lst2.append('"')
    elif idx[0] == '+':
        lst2.append('"')
        idx = idx[0] + idx[1:].zfill(2)
        lst2.append(idx)
        lst2.append('"')
    elif idx[0] == '-':
        lst2.append('"')
        idx = idx[0] + idx[1:].zfill(2)
        lst2.append(idx)
        lst2.append('"')
    else:
        lst2.append(idx)

print(lst2)


message = ''
for i in range(len(lst2)):
    if lst2[i] == '"':
        if i == len(lst2) - 1 or lst2[i + 1].isdigit() or lst2[i + 1][0] == '+' or lst2[i + 1][0] == '-':
            message += lst2[i]
        else:
            message += lst2[i]
            message += ' '
    elif lst2[i].isdigit():
        message += lst2[i]
    elif '.' in lst2[i]:
        message += lst2[i]
        message += ' '
    elif lst2[i][0] == '+':
        message += lst2[i]
    elif lst2[i][0] == '-':
        message += lst2[i]
    else:
        message += lst2[i]
        message += ' '

print(message)

# ВТОРАЯ ПРОВЕРКА
lst1 = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']

lst2 = []
for idx in lst1:
    if '.' in idx:
        lst2.append(idx)
    elif idx.isdigit():
        lst2.append('"')
        idx = idx.zfill(2)
        lst2.append(idx)
        lst2.append('"')
    elif idx[0] == '+':
        lst2.append('"')
        idx = idx[0] + idx[1:].zfill(2)
        lst2.append(idx)
        lst2.append('"')
    elif idx[0] == '-':
        lst2.append('"')
        idx = idx[0] + idx[1:].zfill(2)
        lst2.append(idx)
        lst2.append('"')
    else:
        lst2.append(idx)

print(lst2)


message = ''
for i in range(len(lst2)):
    if lst2[i] == '"':
        if i == len(lst2) - 1 or lst2[i + 1].isdigit() or lst2[i + 1][0] == '+' or lst2[i + 1][0] == '-':
            message += lst2[i]
        else:
            message += lst2[i]
            message += ' '
    elif lst2[i].isdigit():
        message += lst2[i]
    elif '.' in lst2[i]:
        message += lst2[i]
        message += ' '
    elif lst2[i][0] == '+':
        message += lst2[i]
    elif lst2[i][0] == '-':
        message += lst2[i]
    else:
        message += lst2[i]
        message += ' '

print(message)

# ТРЕТЬЯ ПРОВЕРКА
lst1 = ['+9', 'примерно в', '23', 'часа', '8', 'минут', '03', '05', 'секунд', 'температура', 'воздуха', 'была', '5',
        'градусов Цельсия', 'темп','воды','+2.0','градусов','Цельсия', '-2', '11']
lst2 = []
for idx in lst1:
    if '.' in idx:
        lst2.append(idx)
    elif idx.isdigit():
        lst2.append('"')
        idx = idx.zfill(2)
        lst2.append(idx)
        lst2.append('"')
    elif idx[0] == '+':
        lst2.append('"')
        idx = idx[0] + idx[1:].zfill(2)
        lst2.append(idx)
        lst2.append('"')
    elif idx[0] == '-':
        lst2.append('"')
        idx = idx[0] + idx[1:].zfill(2)
        lst2.append(idx)
        lst2.append('"')
    else:
        lst2.append(idx)

print(lst2)


message = ''
for i in range(len(lst2)):
    if lst2[i] == '"':
        if i == len(lst2) - 1 or lst2[i + 1].isdigit() or lst2[i + 1][0] == '+' or lst2[i + 1][0] == '-':
            message += lst2[i]
        else:
            message += lst2[i]
            message += ' '
    elif lst2[i].isdigit():
        message += lst2[i]
    elif '.' in lst2[i]:
        message += lst2[i]
        message += ' '
    elif lst2[i][0] == '+':
        message += lst2[i]
    elif lst2[i][0] == '-':
        message += lst2[i]
    else:
        message += lst2[i]
        message += ' '

print(message)
