num_list = list(map(int, input().split()))

while num_list != [1, 2, 3, 4, 5]:
    for i in range(len(num_list) - 1):
        if num_list[i] > num_list[i + 1]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
            print(*num_list)
