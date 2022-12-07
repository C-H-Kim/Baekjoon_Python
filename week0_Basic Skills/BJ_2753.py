if __name__ == '__main__':
    year = int(input())

    if year % 4 == 0:
        if year % 400 == 0 :
            flag = True
        elif year % 100 == 0:
            flag = False
        else:
            flag = True
    else:
        flag = False

    if flag:
        print(1)
    else:
        print(0)
