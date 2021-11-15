"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""
import random


def sort_bubble(array):
    i = 1
    while i < len(array):
        is_sorted = True
        for j in range(len(array) - i):
            if array[j] < array[j + 1]:
                is_sorted = False
                array[j], array[j + 1] = array[j + 1], array[j]
        if is_sorted:
            break
        i += 1
    return array


if __name__ == '__main__':
    original_array = [random.randint(-100, 100) for _ in range(random.randint(10, 20))]
    sorted_array = sort_bubble(original_array.copy())
    print(original_array, sorted_array, sep='\n')
