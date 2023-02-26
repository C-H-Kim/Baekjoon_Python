import sys
from collections import deque


def bfs(num):
    queue = deque([num])

    while queue:
        v = queue.popleft()
        if v == K:
            break

        for i in [v - 1, v + 1, 2 * v]:
            if 0 <= i <= 100000 and dist[i] == 0:
                dist[i] = dist[v] + 1
                queue.append(i)


N, K = map(int, sys.stdin.readline().split())
dist = [0] * 100001

bfs(N)

print(dist[K])
