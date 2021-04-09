# Функции не проходили
# def is_integer(n):
#     try:
#         float(n)
#         return True
#     except ValueError:
#         return False

# выглядит очень страшно, но я старался

# импортируем регулярные выражения для последнего задания
import re
# исходный список
initial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']

# проверка (исходный)
print(f'Исходный список: {initial_list}\n'
      f'ID: {id(initial_list)}')

# вместо for используем while (будет меняться условие выхода)
loop_count = len(initial_list) - 1
iterator = 0
while iterator < loop_count:
    # вспомогательная переменная (проверка на наличие '+' или '-')
    has_prefix = initial_list[iterator].startswith(('-', '+'))
    # проверка на число с учетом символов '+' или '-'
    if initial_list[iterator][int(has_prefix):].isdigit():
        # приводим число к нужному виду с сохранением знаков,
        # abs нужен, потому что к отрицательным числам добавляется дополнительный '-'
        initial_list[iterator] = f'{initial_list[iterator][0] if has_prefix else ""}' \
                                 f'{abs(int(initial_list[iterator])):0>2}'
        # вставляем ковычки
        initial_list.insert(iterator, '"')
        initial_list.insert(iterator + 2, '"')
        # увеличиваем текущий и максимальное количество индексов на 2
        iterator += 2
        loop_count += 2
    iterator += 1

# проверка (конечный)
print(f'Сформированный список: {initial_list}\n'
      f'ID: {id(initial_list)}')

# новый список готов, нужно выводить
print(re.sub(pattern=r'" ([+-]?\d+) "', repl=r'"\1"', string=' '.join(initial_list)))
