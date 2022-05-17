from sys import argv
from os.path import join

path1 = join('.', 'bakery.csv')

if len(argv) == 1 or not argv[1].isdigit():
    print('Необходимо ввести число.')
elif argv[1].isdigit() and len(argv) == 2:
    with open(path1, mode='at', encoding='utf-8') as f:
        f.write(f'{argv[1]}\n')
elif len(argv) > 2:
    print('Необходимо ввести только одно число.')

