import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

count = {}
for num in num_list:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

del_duplicated = list(set(num_list))
del_duplicated.sort()

ans_list = []
for check_num in check_list:
    start = 0
    end = len(del_duplicated) - 1
    flag = False

    while start <= end:
        mid = (start + end) // 2

        if del_duplicated[mid] > check_num:
            end = mid - 1
        elif del_duplicated[mid] < check_num:
            start = mid + 1
        else:
            ans_list.append(count[check_num])
            flag = True
            break

    if not flag:
        ans_list.append(0)

print(*ans_list)
