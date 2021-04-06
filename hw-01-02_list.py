sum_result_base = 0
sum_result_plus_17 = 0

for number in [number ** 3 for number in range(1000) if number % 2 == 1]:
    sum_numeral = 0
    for letter in str(number):
        sum_numeral += int(letter)
    if sum_numeral % 7 == 0:
        sum_result_base += number
    number += 17
    sum_numeral = 0
    for letter in str(number):
        sum_numeral += int(letter)
    if sum_numeral % 7 == 0:
        sum_result_plus_17 += number

print("Сумма чисел из списка, сумма цифр которых делится нацело на 7: %d" % sum_result_base)
print("Сумма чисел (плюс 17) из списка, сумма цифр которых делится нацело на 7: %d" % sum_result_plus_17)
