import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

M = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

ans_list = []
for check_num in check_list:
    start = 0
    end = len(num_list) - 1
    flag = False

    while start <= end:
        mid = (start + end) // 2

        if num_list[mid] > check_num:
            end = mid - 1
        elif num_list[mid] < check_num:
            start = mid + 1
        else:
            ans_list.append(1)
            flag = True
            break

    if not flag:
        ans_list.append(0)

print(*ans_list)
