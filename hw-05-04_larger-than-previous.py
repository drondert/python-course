from time import perf_counter
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]


def larger_than_previous_gen(source_list):
    for iterator, enum in enumerate(source_list[1:]):
        if enum > source_list[iterator]:
            yield enum


if __name__ == '__main__':
    start = perf_counter()
    result = larger_than_previous_gen(src)
    print(f'Генератор\n'
          f'Размер: {sys.getsizeof(result)}\n'
          f'Скорость: {perf_counter() - start}')

    start = perf_counter()
    result = [num_2 for num_1, num_2 in zip(src, src[1:]) if num_2 > num_1]
    print(f'List Comprehension\n'
          f'Размер: {sys.getsizeof(result)}\n'
          f'Скорость: {perf_counter() - start}')

    start = perf_counter()
    result = []
    for iterator in range(1, len(src)):
        if src[iterator] > src[iterator - 1]:
            result.append(src[iterator])
    print(f'Формирование списка\n'
          f'Размер: {sys.getsizeof(result)}\n'
          f'Скорость: {perf_counter() - start}')
