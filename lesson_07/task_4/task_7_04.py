# Написать скрипт, который для заданной
# папки выводит статистику размеров файлов

import os
list_of_borders = [100, 1000, 10000, 100000]

dict_1 = {}
value = 0
for i in list_of_borders:
    dict_1[i] = value

folder = 'some_data'
all_files = [file for file in os.listdir(folder)]
for file in all_files:
    if os.stat(os.path.join(folder, file)).st_size < list_of_borders[0]:
        dict_1[list_of_borders[0]] += 1
    elif list_of_borders[0] < os.stat(os.path.join(folder, file)).st_size < list_of_borders[1]:
        dict_1[list_of_borders[1]] += 1
    elif list_of_borders[1] < os.stat(os.path.join(folder, file)).st_size < list_of_borders[2]:
        dict_1[list_of_borders[2]] += 1
    elif list_of_borders[2] < os.stat(os.path.join(folder, file)).st_size < list_of_borders[3]:
        dict_1[list_of_borders[3]] += 1

print('{')
for key, value in dict_1.items():
    print(f'{key}: {value}')
print('}')

