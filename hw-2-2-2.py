"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

if __name__ == '__main__':
    uneven = 0
    even = 0
    user_input = input("Введите натуральное число: ")
    if user_input.isdigit() and int(user_input) > 0:
        for num in user_input:
            if int(num) % 2 == 0:
                even += 1
            else:
                uneven += 1
        print(f'Количество четных: {even}\nКоличество нечетных: {uneven}')
    else:
        print(f'{user_input} не натуральное число')
