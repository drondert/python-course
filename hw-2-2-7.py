"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def sequence_sum(n):
    if n == 1:
        return 1
    else:
        return sequence_sum(n - 1) + n


if __name__ == '__main__':
    user_input = input('Введите натуральное число (количество элементов в ряде): ')
    if user_input.isdigit() and int(user_input) == float(user_input):
        user_input = int(user_input)
        print(f'Сумма по формуле n * (n + 1) / 2 = {user_input} * ({user_input} + 1) / 2 = {user_input * (user_input + 1) / 2}',
              f'Сумма ряда: {sequence_sum(user_input)}')
    else:
        print('Некорректный ввод!')
