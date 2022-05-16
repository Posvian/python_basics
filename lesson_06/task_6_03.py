# Есть два файла: в одном хранятся ФИО
# пользователей сайта, а в другом — данные
# об их хобби. Загрузить данные из обоих файлов
# и сформировать словарь: ключи — ФИО, значения
# — данные о хобби. Сохранить словарь в текстовый
# файл. Проверить сохранённые данные.

from os.path import join

path1 = join('.', 'files', 'task_3_users.csv')
path2 = join('.', 'files', 'task_3_hobby.csv')
path3 = join('.', 'files', 'task_3_rezult.txt')
rezult = {}
with open(path1, mode='rt', encoding='utf-8') as f:
    with open(path2, mode='rt', encoding='utf-8') as f2:
        for line in f:
            line = line.strip().split(',')
            line1 = f2.readline().replace(',', ';').strip()
            if len(line1) == 0:
                line1 = None
            key = line[0][0] + line[1][0] + line[2][0]
            rezult[key] = line1

with open(path3, mode='wt', encoding='utf-8') as f3:
    f3.write('{')
    for key, value in rezult.items():
        f3.write(f"'{key}': '{value}', ")
    f3.write('}')



