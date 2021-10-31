"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random


def find_max_negative(numbers):
    return min([abs(num) for num in numbers if num < 0]) * -1


if __name__ == '__main__':
    test_list = [random.randint(-50, 50) for _ in range(20)]
    print(test_list)
    print(find_max_negative(test_list))
