"""
Определить, какое число в массиве встречается чаще всего.
"""

import collections
import random

if __name__ == '__main__':
    test_list = [random.randint(1, 10) for _ in range(20)]
    print(test_list)
    print(collections.Counter(test_list))
