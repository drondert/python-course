"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?)
Как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект?
Можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import os

#  словарь словарей, последний каталог в дереве содержит пустой словарь
CONFIG_DICTIONARY = {
    'my_project': {
        'settings': {},
        'mainapp': {},
        'adminapp': {},
        'authapp': {}
    }
}


#  рекурсивный генератор путей из словаря словарей
def path_from_dir_gen(iterable, root_folder=''):
    for folder, sub_folder in iterable.items():
        if folder:
            yield os.path.join(root_folder, folder)
            yield from path_from_dir_gen(sub_folder, os.path.join(root_folder, folder))


if __name__ == '__main__':
    for full_path in path_from_dir_gen(CONFIG_DICTIONARY):
        dir_full_path = os.path.join(os.getcwd(), full_path)
        if not os.path.exists(dir_full_path):
            os.mkdir(dir_full_path)
