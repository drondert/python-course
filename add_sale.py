import sys

sale_value = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as file_bakery:
    file_bakery.write(f'{sale_value}\n')
