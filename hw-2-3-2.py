"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
то во второй массив надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""


def return_even_indexes(numbers):
    index_list = []
    for index, number in enumerate(numbers):
        if number % 2 == 0:
            index_list.append(index)
    return index_list


if __name__ == '__main__':
    test_list = [2, 4, 1, 3, 8, 10, 7, 5]
    print(test_list)
    print(return_even_indexes(test_list))
