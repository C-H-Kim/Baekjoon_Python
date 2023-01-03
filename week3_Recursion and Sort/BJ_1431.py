def sum_num(string):
    result = 0
    for s in string:
        if s.isdigit():
            result += int(s)
    return result


N = int(input())
serial_list = [input() for _ in range(N)]

serial_list.sort(key=lambda x: (len(x), sum_num(x), x))
for serial in serial_list:
    print(serial)
