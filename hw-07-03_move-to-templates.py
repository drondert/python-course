"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
   |--templates
   |  |--mainapp
   |        |--base.html
   |        |--index.html
   |  |--authapp
   |        |--base.html
   |        |--index.html

Примечание: исходные файлы необходимо оставить.
Обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён).
Предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.
"""

import os
import shutil

CONFIG_DICTIONARY = {
    'my_project': {
        'settings': {},
        'mainapp': {
            'templates': {
                'mainapp': {}
            }
        },
        'authapp': {
            'templates': {
                'authapp': {}
            }
        }
    }
}


def path_from_dir_gen(iterable, root_folder=''):
    for folder, sub_folder in iterable.items():
        if folder:
            yield os.path.join(root_folder, folder)
            yield from path_from_dir_gen(sub_folder, os.path.join(root_folder, folder))


def create_starter_from_config():
    for full_path in path_from_dir_gen(CONFIG_DICTIONARY):
        dir_full_path = os.path.join(os.getcwd(), full_path)
        if not os.path.exists(dir_full_path):
            os.mkdir(dir_full_path)


if __name__ == '__main__':
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), 'my_project')):
        if files:
            for file in files:
                if file.endswith('.html') and 'templates' in root:
                    try:
                        shutil.copyfile(
                            os.path.join(root, file),
                            os.path.join(os.getcwd(), 'my_project', 'templates', os.path.basename(root), file)
                        )
                    except FileNotFoundError:
                        os.makedirs(os.path.join(os.getcwd(), 'my_project', 'templates', os.path.basename(root)))
                        shutil.copyfile(
                            os.path.join(root, file),
                            os.path.join(os.getcwd(), 'my_project', 'templates', os.path.basename(root), file)
                        )
