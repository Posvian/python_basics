from sys import argv
from os.path import join

path1 = join('.', 'bakery.csv')

if len(argv) == 1:
    with open(path1, mode='rt', encoding='utf-8') as f:
        content = f.readlines()
        for line in content:
            print(line.strip())
elif len(argv) == 2 and argv[1].isdigit():
    with open(path1, mode='rt', encoding='utf-8') as f:
        content = f.readlines()
        i = int(argv[1]) - 1
        while i < len(content):
            print(content[i].strip())
            i += 1
elif len(argv) == 3 and argv[1].isdigit() and argv[2].isdigit():
    with open(path1, mode='rt', encoding='utf-8') as f:
        content = f.readlines()
        i = int(argv[1]) - 1
        if int(argv[2]) > len(content):
            while i < len(content):
                print(content[i].strip())
                i += 1
        else:
            while i < int(argv[2]):
                print(content[i].strip())
                i += 1
else:
    print('Скрипт может быть запущен с одним или двумя аргументами, аргументы должны быть целыми числами')
