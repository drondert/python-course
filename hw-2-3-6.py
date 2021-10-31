"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random


def sum_between_minmax(numbers):
    minindex, maxindex = numbers.index(min(numbers)), numbers.index(max(numbers))
    return sum(numbers[minindex + 1:maxindex]) + sum(numbers[maxindex + 1:minindex])


if __name__ == '__main__':
    test_list = [random.randint(0, 50) for _ in range(10)]
    print(test_list)
    print(min(test_list), max(test_list))
    print(sum_between_minmax(test_list))
