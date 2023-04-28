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
            dist[2 * v] = dist[v]
            visit[2 * v] = True
            queue.append(2 * v)

        for i in [v - 1, v + 1]:
            if 0 <= i <= 100000 and not visit[i]:
                dist[i] = dist[v] + 1
                visit[i] = True
                queue.append(i)


N, K = map(int, sys.stdin.readline().split())
dist = [0] * 100001
visit = [False] * 100001

bfs(N)

print(dist[K])
