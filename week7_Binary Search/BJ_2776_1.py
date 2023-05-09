import sys


def binary_search(num):
    start = 0
    end = len(note1) - 1

    while start <= end:
        mid = (start + end) // 2

        if num >= note1[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return end


T = int(sys.stdin.readline())

for _ in range(T):
    sys.stdin.readline()
    note1 = list(map(int, sys.stdin.readline().split()))
    note1.sort()

    sys.stdin.readline()
    note2 = list(map(int, sys.stdin.readline().split()))

    for check_num in note2:
        if note1[binary_search(check_num)] == check_num:
            print(1)
        else:
            print(0)
