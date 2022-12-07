if __name__ == '__main__':
    score = int(input())

    if score >= 90:
        res = 'A'
    elif score >= 80:
        res = 'B'
    elif score >= 70:
        res = 'C'
    elif score >= 60:
        res = 'D'
    else:
        res = 'F'

    print(res)
