# Распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
from os.path import join

path1 = join('.', 'files', 'nginx_logs.txt')
file1 = open(path1, mode='rt', encoding='utf-8')
line = file1.readline()
my_list = []
for line in file1:
    line = line.split()
    remote_addr = line[0]
    request_type = line[5][1:]
    requested_resource = line[6]
    my_tuple = (remote_addr, request_type, requested_resource)
    my_list.append(my_tuple)
file1.close()

print(my_list)
