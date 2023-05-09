import sys


def binary_search(num):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if num == note1[mid]:
            return 1
        elif num > note1[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    note1 = list(map(int, sys.stdin.readline().split()))
    note1.sort()

    sys.stdin.readline()
    note2 = list(map(int, sys.stdin.readline().split()))

    for check_num in note2:
        print(binary_search(check_num))
