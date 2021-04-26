import itertools
import json
import pprint


def file_lines_count(file):
    i = 0
    for i, line in enumerate(file):
        pass
    file.seek(0)
    return i + 1


with open('users.csv', encoding='utf-8-sig') as file_users, open('hobbies.csv', encoding='utf-8-sig') as file_hobbies:
    if file_lines_count(file_users) < file_lines_count(file_hobbies):
        exit(1)
    user_hobby = {}
    for line_user, line_hobbies in itertools.zip_longest(file_users.readlines(), file_hobbies.readlines()):
        user_hobby[line_user.strip()] = line_hobbies.strip() if line_hobbies is not None else None

with open('user_hobby.json', 'w') as file_dictionary:
    file_dictionary.write(json.dumps(user_hobby))

# проверка
with open('user_hobby.json') as file_dictionary:
    user_hobby = json.load(file_dictionary)
pprint.pprint(user_hobby)
