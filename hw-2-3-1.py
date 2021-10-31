"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

DIVIDERS = range(2, 10)


def count_divisible(l_bound, u_bound):
    div_count = {}
    for divider in DIVIDERS:
        if l_bound % divider == 0:
            div_count[divider] = (int(u_bound / divider) - int(l_bound / divider)) + 1
        else:
            div_count[divider] = (int(u_bound / divider) - int(l_bound / divider))
    return div_count


if __name__ == '__main__':
    print(count_divisible(2, 99))
