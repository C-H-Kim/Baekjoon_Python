from collections import deque
import sys

N, M = map(int, input().split())
pos_list = list(map(int, sys.stdin.readline().split()))
dq = deque([i for i in range(1, N + 1)])

count = 0
for num in pos_list:
    while True:
        if dq[0] == num:
            dq.popleft()
            break
        else:
            if dq.index(num) < len(dq) / 2:
                while dq[0] != num:
                    dq.append(dq.popleft())
                    count += 1
            else:
                while dq[0] != num:
                    dq.appendleft(dq.pop())
                    count += 1

print(count)
