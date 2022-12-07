if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())

    units = num2 % 10
    tens = (num2 % 100) // 10
    hundreds = num2 // 100
    res = num1 * num2

    print(num1 * units)
    print(num1 * tens)
    print(num1 * hundreds)
    print(res)
