import sys
from collections import deque

T = int(input())

for _ in range(T):
    opt_list = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')

    dq = deque(arr)
    if n == 0:
        dq = []
    r_count = 0
    flag = True

    for opt in opt_list:
        if opt == 'R':
            r_count += 1
        elif opt == 'D':
            if len(dq) == 0:
                flag = False
                print("error")
                break
            else:
                if r_count % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()

    if flag:
        if r_count % 2 == 0:
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")
