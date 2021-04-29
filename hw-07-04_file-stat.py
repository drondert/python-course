"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:

{
  100: 15,
  1000: 3,
  10000: 7,
  100000: 2
}

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os
import sys
import pprint


def return_biggest_multiple_of_ten(numeral, base_power=2):
    if numeral // 10 ** base_power != 0:
        return return_biggest_multiple_of_ten(numeral, base_power=base_power + 1)
    else:
        return 10 ** base_power


folder_path = sys.argv[1]
# folder_path = 'my_project'
if __name__ == '__main__':
    dir_of_sizes = {}
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                dir_of_sizes.update({
                    return_biggest_multiple_of_ten(os.stat(os.path.abspath(os.path.join(root, file))).st_size):
                        dir_of_sizes.setdefault(return_biggest_multiple_of_ten(os.stat(os.path.abspath(os.path.join(root, file))).st_size), 0) + 1
                })
    except FileNotFoundError:
        print('Ошибка! Каталога не существует!')
    else:
        pprint.pprint(dir_of_sizes)
