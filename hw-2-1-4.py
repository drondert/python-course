"""
Написать программу, которая генерирует в указанных пользователем границах:
    - случайное целое число;
    - случайное вещественное число;
    - случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

a-z 97-122
A-Z 65-90
"""
import random
import string

if __name__ == '__main__':
    l_bound = input('Введите нижнюю границу диапазона (число или латинскую букву): ')
    u_bound = input('Введите верхнюю границу диапазона (число или латинскую букву): ')
    if not (l_bound.isnumeric() or u_bound.isnumeric()):
        if len(l_bound + u_bound) == 2:
            l_bound = l_bound.lower()
            u_bound = u_bound.lower()
            if l_bound in string.ascii_lowercase and u_bound in string.ascii_lowercase:
                print(random.choice(string.ascii_lowercase[string.ascii_lowercase.find(l_bound):string.ascii_lowercase.find(u_bound) + 1]))
            else:
                print('Введите латинские буквы!')
        else:
            print('Введите только один символ для границы диапазона!')
    elif 1:
        pass
