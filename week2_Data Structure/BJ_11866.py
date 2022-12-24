from collections import deque

N, K = map(int, input().split())
dq = deque([i for i in range(1, N + 1)])
answer = []

while dq:
    count = 0
    while count < K - 1:
        dq.append(dq.popleft())
        count += 1
    answer.append(dq.popleft())

print("<", end='')
for i in range(N - 1):
    print(f"{answer[i]}, ", end='')
print(f"{answer[-1]}>")
