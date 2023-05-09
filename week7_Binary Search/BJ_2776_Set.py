import sys

T = int(sys.stdin.readline())

for _ in range(T):
    sys.stdin.readline()
    note1 = set(map(int, sys.stdin.readline().split()))

    sys.stdin.readline()
    note2 = list(map(int, sys.stdin.readline().split()))

    for check_num in note2:
        if check_num in note1:
            print(1)
        else:
            print(0)
