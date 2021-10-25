"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def digits_sum(num):
    if num % 10 == 0:
        return num // 10
    else:
        return digits_sum(num // 10) + num % 10


if __name__ == '__main__':
    biggest_sum = (0, 0)
    while True:
        user_input = input('Введите натуральное число (или stop для отмены): ')
        if user_input.isdigit() and int(user_input) == float(user_input):
            sum_to_compare = digits_sum(int(user_input))
            if biggest_sum[1] < sum_to_compare:
                biggest_sum = int(user_input), sum_to_compare
        elif user_input.lower() == 'stop':
            if biggest_sum != (0, 0):
                print(f'Наибольшее число - {biggest_sum[0]} с суммой {biggest_sum[1]}')
                break
