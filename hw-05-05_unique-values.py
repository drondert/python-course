from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

if __name__ == '__main__':
    start = perf_counter()
    result = list(filter(lambda val: src.count(val) == 1, src))
    print(f'filter()\n'
          f'{result}\n'
          f'Время исполнения: {perf_counter() - start}')

    start = perf_counter()
    result = list((val for val in src if src.count(val) == 1))
    print(f'Генератор\n'
          f'{result}\n'
          f'Время исполнения: {perf_counter() - start}')

    start = perf_counter()
    result = []
    for val in src:
        if src.count(val) == 1:
            result.append(val)
    print(f'"Вручную"\n'
          f'{result}\n'
          f'Время исполнения: {perf_counter() - start}')
