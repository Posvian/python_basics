# Есть два файла: в одном хранятся ФИО
# пользователей сайта, а в другом — данные
# об их хобби. Загрузить данные из обоих файлов
# и сформировать словарь: ключи — ФИО, значения
# — данные о хобби. Сохранить словарь в текстовый
# файл. Проверить сохранённые данные.
# Выполните запись результирующего словаря в файл
# json формата. Сделайте так чтобы русские букву
# читались как обычный текст, без преобразования
# в коды unicode.

from os.path import join
import json

path1 = join('.', 'files', 'task_3_users.csv')
path2 = join('.', 'files', 'task_3_hobby.csv')
path3 = join('.', 'files', 'task_3_rezult.json')
rezult = {}


def dict_write():
    rezult_str = json.dumps(rezult, ensure_ascii=False)
    f3.write(rezult_str)


with open(path1, mode='rt', encoding='utf-8') as f:
    with open(path2, mode='rt', encoding='utf-8') as f2:
        with open(path3, mode='wt', encoding='utf-8') as f3:
            users = f.readlines()
            hobbies = f2.readlines()
            i = 0
            if len(users) >= len(hobbies):
                while i < len(users):
                    user = users[i].strip().split(',')
                    hobby = hobbies[i].strip().replace(',', ';')
                    if len(hobby[i]) == 0:
                        hobby = None
                    key = user[0][0] + user[1][0] + user[2][0]
                    rezult[key] = hobby
                    i += 1
                dict_write()
            else:
                while i < len(users):
                    user = users[i].strip().split(',')
                    hobby = hobbies[i].strip().replace(',', ';')
                    key = user[0][0] + user[1][0] + user[2][0]
                    rezult[key] = hobby
                    i += 1
                dict_write()
                exit(1)
