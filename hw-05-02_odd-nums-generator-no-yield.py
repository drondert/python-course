if __name__ == '__main__':
    odd_to_15 = (num for num in range(1, 16, 2))
    for odd_num in odd_to_15:
        print(odd_num)
