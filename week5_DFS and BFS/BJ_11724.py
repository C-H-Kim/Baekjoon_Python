import sys
from collections import deque
sys.setrecursionlimit(10**6)


def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
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

    #dfs(i)
    bfs(i)

    component += 1

print(component)
