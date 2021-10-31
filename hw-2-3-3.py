"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random


def minmax_swap(numbers):
    print(numbers.index(min(numbers)), numbers.index(max(numbers)))
    numbers[numbers.index(min(numbers))], numbers[numbers.index(max(numbers))] = max(numbers), min(numbers)
    return numbers


if __name__ == '__main__':
    test_list = [random.randint(1, 50) for _ in range(10)]
    print(test_list)
    print(minmax_swap(test_list))
