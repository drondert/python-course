"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict

if __name__ == '__main__':
    numbers = {}
    for _ in range(2):  # любое количество
        num = input('Введите шестнадцатеричное число: ')
        numbers[num] = list(num)
    hex_sum, hex_mult = 0, 1
    for k in numbers.keys():
        hex_sum += int(k, 16)
        hex_mult = hex_mult * int(k, 16)
    print(f'Сумма: {list(hex(hex_sum)[2:].upper())}, Произведение: {list(hex(hex_mult)[2:].upper())}')
