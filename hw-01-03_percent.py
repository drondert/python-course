# 1 процент
# 2 3 4 процента
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 процентов
# 20+ не включаем

try:
    percent_number = int(input("Введите количество процентов до 20: "))
    if percent_number < 20:
        if percent_number == 1:
            percent_format = "%d процент"
        elif percent_number < 5:
            percent_format = "%d процента"
        else:
            percent_format = "%d процентов"
        print(percent_format % percent_number)
    else:
        print("Число больше 20")
except ValueError:
    print("Вы ввели не число")
