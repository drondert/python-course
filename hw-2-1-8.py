"""
Определить, является ли год, который ввел пользователем, високосным или невисокосным.
"""

if __name__ == '__main__':
    year = input('Введите год: ')
    if year.isnumeric():
        year = int(year)
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print(f'{year} високосный.')
        else:
            print(f'{year} невисокосный.')
    else:
        print('Неправильный ввод.')
