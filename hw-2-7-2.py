"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
import random


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left, right = array[:middle], array[middle:]
    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left, right))


def merge(left, right):
    res = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            res.append(left[0])
            left.remove(left[0])
        else:
            res.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        res += right
    else:
        res += left
    return res


if __name__ == '__main__':
    original_array = [random.uniform(0, 50) for _ in range(15)]
    print(original_array)
    sorted_array = merge_sort(original_array)
    print(sorted_array)
