"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

a-z 97-122
A-Z 65-90
"""

if __name__ == '__main__':
    first_letter = input('Введите первую букву: ').lower()
    second_letter = input('Введите вторую букву: ').lower()
    if len(first_letter + second_letter) == 2:
        if ord(first_letter) in range(97, 123) and ord(second_letter) in range(97, 123):
            print(f'Порядковый номер {first_letter}: {ord(first_letter) - 96}')
            print(f'Порядковый номер {second_letter}: {ord(second_letter) - 96}')
            print(f'Количество букв между {first_letter} и {second_letter}: {abs(ord(first_letter) - ord(second_letter)) - 1}')
        else:
            print('Введены не латинские буквы')
    else:
        print('Количество введенных символов превышает 2')
