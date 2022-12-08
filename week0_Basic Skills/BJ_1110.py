if __name__ == '__main__':
    N = int(input())

    check = -1
    count = 0
    new_num = N

    while N != check:
        units = new_num % 10
        tens = new_num // 10

        temp = tens + units
        temp_units = temp % 10

        check = units * 10 + temp_units
        new_num = check
        count += 1

    print(count)
