import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

num_dict = {}
for num in num_list:
    num_dict[num] = 0

ans_list = []
for check in check_list:
    if check in num_dict:
        ans_list.append(1)
    else:
        ans_list.append(0)

print(*ans_list)
