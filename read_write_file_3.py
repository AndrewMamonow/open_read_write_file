# Задача №3
import os.path

# Список файлов для объединения
name_files = ['1.txt', '2.txt', '3.txt']
# Файл с результатом объединения
name_files_res = 'result.txt'

# Функция чтения из файла
def open_file(name_file):
    if not os.path.exists(name_file):
        return f'Ошибка: Файла {name_file} нет'
    with open(name_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

# Функция добавления в файл
def write_file(name_file, lines):
    with open(name_file, 'a', encoding='utf-8') as file:
        file.write(lines)

# Функция очистки файла для записи результата
def clear_file(name_file):
    with open(name_file, 'w') as file:
        file.write('')

# Чтение файлов из списка и сортировка
files_dict = {}     
for file in name_files:
    file_read=open_file(file)
    files_dict[len(file_read)] = [file, file_read]
files_sorted = sorted(files_dict.items())

# Объединение файлов и запись результата в один файл
clear_file (name_files_res)
for k, v in files_sorted:
    write_file(name_files_res, v[0] + '\n')
    write_file(name_files_res, str(k) + '\n')
    write_file(name_files_res, ''.join(v[1]) + '\n')

#print('Задача №3 выполнена')