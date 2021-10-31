"""
8.
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

9.
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

MATRIX_ROWS = 5
MATRIX_COLUMNS = 4


def create_matrix_manual():
    matrix = []
    for rows in range(MATRIX_ROWS):
        matrix.append([])
        for columns in range(MATRIX_COLUMNS):
            matrix[rows].append(input(f'Строка {rows + 1}, столбец {columns + 1}: '))
    return matrix


def create_matrix_random():
    matrix = []
    for rows in range(MATRIX_ROWS):
        matrix.append([])
        for columns in range(MATRIX_COLUMNS):
            matrix[rows].append(random.randint(-50, 50))
    return matrix


def string_matrix(matrix):
    return '\n'.join([''.join(['{:5}'.format(elem) for elem in row]) for row in matrix])


def sum_matrix_rows(matrix):
    for rows in matrix:
        rows.append(sum(rows))
    return matrix


def find_max_of_min_per_column(matrix):
    return max([min(row) for row in matrix])


if __name__ == '__main__':
    matrix = create_matrix_random()
    print(string_matrix(matrix))
    matrix = sum_matrix_rows(matrix)
    print(string_matrix(matrix))
    print(find_max_of_min_per_column(matrix))
