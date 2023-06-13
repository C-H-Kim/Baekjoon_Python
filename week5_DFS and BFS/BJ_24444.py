import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    order = 1
    visited[start] = order

    while queue:
        vertex = queue.popleft()

        for next in graph[vertex]:
            if visited[next] == 0:
                queue.append(next)
                order += 1
                visited[next] = order


N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

visited = [0] * (N + 1)

bfs(R)

for i in range(1, len(visited)):
    print(visited[i])
