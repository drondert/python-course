"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ОС: Windows 7 SP1 (x64)
Python 3.7.4
"""
from math import log
from guppy import hpy
from sys import getsizeof


def prime_ubound(n):
    ubound = 100
    while n > ubound / log(ubound):
        ubound += 100
    return ubound


def find_i_prime_with_er(n):
    h = hpy()
    u_bound = prime_ubound(n)
    numbers = [i for i in range(2, u_bound)]
    for i in numbers:
        if i != 0:
            for j in range(2 * i, u_bound, i):
                numbers[j - 2] = 0
    numbers = [num for num in numbers if num != 0]
    print(h.heap(), '\n', f' u_bound = {getsizeof(u_bound)}', f'numbers = {getsizeof(numbers)}')
    return numbers[n]


"""
Partition of a set of 36767 objects. Total size = 2504208 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  10380  28   682955  27    682955  27 str
     1   9136  25   370236  15   1053191  42 tuple
     2   4636  13   253018  10   1306209  52 bytes
     3   2387   6   201216   8   1507425  60 types.CodeType
     4    446   1   171332   7   1678757  67 type
     5   2200   6   158400   6   1837157  73 function
     6    446   1   133628   5   1970785  79 dict of type
     7     96   0    84420   3   2055205  82 dict of module
     8    240   1    61560   2   2116765  85 dict (no owner)
     9   1122   3    49368   2   2166133  86 types.WrapperDescriptorType
<116 more rows. Type e.g. '_.more' to view.> 
  u_bound = 14 numbers = 1656
"""


def find_i_prime_without_er(n):
    h = hpy()
    u_bound = prime_ubound(n)
    numbers = [i for i in range(3, u_bound + 1)]
    primes = []
    for i in numbers:
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    print(h.heap(), '\n', f'u_bound = {getsizeof(u_bound)}', f'numbers = {getsizeof(numbers)}', f'primes = {getsizeof(primes)}')
    return primes[n]


"""
Partition of a set of 38637 objects. Total size = 2540298 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  10380  27   682955  27    682955  27 str
     1   9136  24   370236  15   1053191  41 tuple
     2   4636  12   253018  10   1306209  51 bytes
     3   2387   6   201216   8   1507425  59 types.CodeType
     4    446   1   171332   7   1678757  66 type
     5   2200   6   158400   6   1837157  72 function
     6    446   1   133628   5   1970785  78 dict of type
     7     96   0    84420   3   2055205  81 dict of module
     8    240   1    61560   2   2116765  83 dict (no owner)
     9   1122   3    49368   2   2166133  85 types.WrapperDescriptorType
<116 more rows. Type e.g. '_.more' to view.> 
 u_bound = 14 numbers = 10528 primes = 1656
"""

if __name__ == '__main__':
    print(find_i_prime_with_er(300))
    print(find_i_prime_without_er(300))
