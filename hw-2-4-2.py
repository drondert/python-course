"""
Написать два алгоритма нахождения i-го по счёту простого числа.


Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
"""
import cProfile
from math import log


#  DFT_RANGE = 1000
#  Не смог сделать свою реализацию
def prime_ubound(n):  # O(N)
    ubound = 100  # O(1)
    while n > ubound / log(ubound):  # O(N)
        ubound += 100  # O(1)
    return ubound


def find_i_prime_with_er(n):  # O(NlogN)
    u_bound = prime_ubound(n)  # O(N)
    numbers = [i for i in range(2, u_bound)]  # O(N)
    for i in numbers:  # O(N)
        if i != 0:  # O(1)
            for j in range(2 * i, u_bound, i):  # O(NlogN)
                numbers[j - 2] = 0  # O(1)
    numbers = [num for num in numbers if num != 0]  # O(N)
    return numbers[n]


def find_i_prime_without_er(n):
    u_bound = prime_ubound(n)  # O(N)
    numbers = [i for i in range(3, u_bound + 1)]  # O(N)
    primes = []
    for i in numbers:
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes[n]


if __name__ == '__main__':
    cProfile.run('find_i_prime_with_er(10000)')
    cProfile.run('find_i_prime_without_er(10000)')
