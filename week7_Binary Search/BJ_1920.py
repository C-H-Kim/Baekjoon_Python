import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

for num in num_list:
    start = 0
    end = N - 1
    flag = False

    while start <= end:
        mid = (start + end) // 2
        if A[mid] > num:
            end = mid - 1
        elif A[mid] < num:
            start = mid + 1
        else:
            print(1)
            flag = True
            break

    if not flag:
        print(0)
