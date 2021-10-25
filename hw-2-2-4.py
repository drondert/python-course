"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def sequence_sum(n):
    if n == 1:
        return 1
    else:
        return sequence_sum(n - 1) + (-0.5) ** (n - 1)


if __name__ == '__main__':
    user_input = input('Введите количество элементов: ')
    if user_input.isdigit() and int(user_input) > 0:
        print(f'Сумма элементов ряда: {sequence_sum(int(user_input))}')
    else:
        print(f'Введите натуральное число.')
