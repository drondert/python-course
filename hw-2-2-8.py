"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

DIGITS = '0123456789'

if __name__ == '__main__':
    digit_to_find = input('Введите цифру: ')
    if digit_to_find in DIGITS and len(digit_to_find) == 1:
        numbers = []
        while True:
            user_numbers = input('Введите число (stop для остановки ввода): ')
            if user_numbers.lower() == 'stop':
                break
            numbers.append(user_numbers)
        if len(numbers) != 0:
            count = 0
            for elem in numbers:
                for digit in elem:
                    if digit_to_find == digit:
                        count += 1
            print(f'Цифра {digit_to_find} попалась {count} раз.')
    else:
        print('Введите одну цифру!')
