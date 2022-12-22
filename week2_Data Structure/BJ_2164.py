from collections import deque

N = int(input())
dq = deque()

for i in range(1, N + 1):
    dq.append(i)

while True:
    if len(dq) == 1:
        break

    dq.popleft()
    temp = dq.popleft()
    dq.append(temp)

print(*dq)
