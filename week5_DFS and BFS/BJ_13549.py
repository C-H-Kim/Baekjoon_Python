import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    visit[start] = True

    while queue:
        v = queue.popleft()
        if v == K:
            break

        if 0 <= 2 * v <= 100000 and not visit[2 * v]:
            time[2 * v] = time[v]
            visit[2 * v] = True
            queue.append(2 * v)

        for i in [v - 1, v + 1]:
            if 0 <= i <= 100000 and not visit[i]:
                time[i] = time[v] + 1
                visit[i] = True
                queue.append(i)


N, K = map(int, sys.stdin.readline().split())
time = [0] * 100001
visit = [False] * 100001

bfs(N)

print(time[K])
