# Написать скрипт, создающий стартер (заготовку)
# для проекта со следующей структурой папок:
import os

dirs = {
        'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']
        }

items = dirs.items()

for key, value in items:
    i = 0
    while i < len(value):
        dir_path = os.path.join(key, value[i])
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        i += 1



