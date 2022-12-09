dn_list = [True] * 10001
dn_list[0] = False

for i in range(1, 10001):
    n = i
    dn = n
    while n != 0:
        dn += n % 10
        n = n // 10

    if dn <= 10000:
        dn_list[dn] = False

for index, flag in enumerate(dn_list):
    if flag:
        print(index)
