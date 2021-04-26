import sys


def file_lines_count(file):
    i = 0
    for i, line in enumerate(file):
        pass
    file.seek(0)
    return i + 1


user_input = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as file_bakery:
    try:
        if len(user_input) > 1:
            file_start = int(user_input[0])
            file_end = int(user_input[1])
        elif len(user_input) == 0:
            file_start = 0
            file_end = file_lines_count(file_bakery)
        else:
            file_start = int(user_input[0])
            file_end = file_lines_count(file_bakery)

        for idx, file_line in enumerate(file_bakery):
            if file_start <= idx + 1 <= file_end:
                print(file_line.strip())
    except ValueError:
        print('Введено не число!')
