import os
import shutil

templates_path = os.path.join('.', 'my_project', 'templates')
# if not os.path.exists(templates_path):
#     os.mkdir(templates_path)

paths = []
for root, dirs, files in os.walk('my_project'):
    for dir in dirs:
        rel_path = os.path.relpath(os.path.join(root, dir), 'my_project')
        if 'templates' in rel_path:
            correct_path = os.path.join('.', 'my_project', rel_path)
            paths.append(correct_path)


for path in paths:
    path = path.split('/')
    path = path[:path.index('templates') + 1]
    path = '/'.join(path)
    try:
        shutil.copytree(path, templates_path, dirs_exist_ok=True)
    except shutil.Error:
        print('the same files')

# for path in paths:
#     shutil.copytree(path, templates_path, dirs_exist_ok=True)