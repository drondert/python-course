"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

if __name__ == '__main__':
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))
        c = int(input('Введите число: '))
        middle = a
        if not (a == b or a == c or b == c):
            if a < b < c or c < b < a:
                middle = b
            elif a < c < b or b < c < a:
                middle = c
            print(f'Среднее: {middle}')
        else:
            print('Есть дубликаты чисел')
    except ValueError:
        print('Введено не число.')
