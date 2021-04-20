list_of_prices = [7, 2.09, 8.70, 99.56, 0.97, 2.37, 5, 17.82, 7.52, 100.79, 5, 3.46, 2.68, 5.94]

# A Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
for price in list_of_prices:
    print(f'{price:.0f} руб {price % 1 * 100:0>2.0f} коп')
print(f'\n')

# B Вывести цены, отсортированные по возрастанию, новый список не создавать
print(id(list_of_prices))
list_of_prices.sort()
print(id(list_of_prices))

for price in list_of_prices:
    print(price)
print(f'\n')

# C Создать новый список, содержащий те же цены, но отсортированные по убыванию
list_of_prices_sorted_reversed = sorted(list_of_prices, reverse=True)

for price in list_of_prices_sorted_reversed:
    print(price)
print(f'\n')

# D Вывести цены пяти самых дорогих товаров
# привел к изначальному (был отсортирован в B)
list_of_prices = [7, 2.09, 8.70, 99.56, 0.97, 2.37, 5, 17.82, 7.52, 100.79, 5, 3.46, 2.68, 5.94]

for price in sorted(list_of_prices)[-5:]:
    print(price)
