"""
Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.

Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
"""
import cProfile
DIVIDERS = range(2, 10)


def count_divisible_first(l_bound, u_bound):  # O(n)
    div_count = {}  # O(1)
    for divider in DIVIDERS:  # O(N)
        if l_bound % divider == 0:  # O(1)
            div_count[divider] = (int(u_bound / divider) - int(l_bound / divider)) + 1  # O(1)
        else:
            div_count[divider] = (int(u_bound / divider) - int(l_bound / divider))  # O(1)
    return div_count


"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 hw-2-4-1.py:13(count_divisible_first)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def count_divisible_second(l_bound, u_bound):  # O(N^2)
    div_count = {}  # O(1)
    for divider in DIVIDERS:  # O(N)
        div_count[divider] = 0  # O(1)
        for num in range(l_bound, u_bound + 1):  # O(N)
            if num % divider == 0:  # O(1)
                div_count[divider] = div_count[divider] + 1  # O(N)
    return div_count


"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   12.497   12.497 <string>:1(<module>)
        1   12.497   12.497   12.497   12.497 hw-2-4-1.py:23(count_divisible_second)
        1    0.000    0.000   12.497   12.497 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


if __name__ == '__main__':
    cProfile.run('print(count_divisible_first(2, 10000000))')
    cProfile.run('print(count_divisible_second(2, 10000000))')
