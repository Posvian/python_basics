#Выполните условие задачи, но формат
# вывода включает и должность, например:
# "Привет, инженер-конструктор Игорь",
# "Привет, главный бухгалтер Марина!" и т.п.


lst1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for cell in lst1:
    lst2 = cell.split()
    name = lst2[-1].capitalize()
    position = ' '.join(lst2[0:len(lst2)-1])
    print(f'Привет, {position} {name}!')