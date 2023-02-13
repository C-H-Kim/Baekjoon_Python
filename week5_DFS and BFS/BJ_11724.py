import sys
from collections import deque


def bfs(start):
    global visited
    global graph

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (N + 1)
component = 0

for i in range(1, N + 1):
    if visited[i]:
        continue

    bfs(i)
    component += 1

print(component)
