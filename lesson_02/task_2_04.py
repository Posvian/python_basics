#4. Обработка списка чисел.
lst1 = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]
print('Исходный список:')
print(lst1)
str1 = ''
for price in lst1:
    rub = int(price // 1)
    cent = round((price - rub)*100, 2)
    cent = int(cent)
    message = f'{rub} руб {cent:02d} коп, '
    str1 += message

print(str1)
print('Доказательство операции in place:')
print(f'id перед сортировкой {id(lst1)}')
lst1.sort()
print(f'id после сортировки {id(lst1)}')
print(lst1)


lst2 = sorted(lst1, reverse=True)
print(f'id нового списка {id(lst2)}')

print('5 самых дорогих товаров:')
for i in range(5):
    print(max(lst2))
    lst2.remove(max(lst2))
