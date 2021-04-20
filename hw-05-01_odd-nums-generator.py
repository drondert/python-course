def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


if __name__ == '__main__':
    odd_to_15 = odd_nums(15)
    for number in odd_to_15:
        print(number)
