"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random


def two_min_1(numbers):
    numbers.sort()
    return numbers[:2]


def two_min_2(numbers):
    return [numbers.pop(numbers.index(min(numbers))), numbers.pop(numbers.index(min(numbers)))]


if __name__ == '__main__':
    test_list = [random.randint(1, 50) for _ in range(10)]
    print(test_list)
    print(two_min_1(test_list))
    print(two_min_2(test_list))
