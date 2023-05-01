import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        if v == K:
            break

        if 0 <= 2 * v <= 100000 and not visited[2 * v]:
            time[2 * v] = time[v]
            visited[2 * v] = True
            queue.append(2 * v)

        for i in [v - 1, v + 1]:
            if 0 <= i <= 100000 and not visited[i]:
                time[i] = time[v] + 1
                visited[i] = True
                queue.append(i)


N, K = map(int, sys.stdin.readline().split())
time = [0] * 100001
visited = [False] * 100001

bfs(N)

print(time[K])
