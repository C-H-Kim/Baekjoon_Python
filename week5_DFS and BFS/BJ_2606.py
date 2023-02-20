import sys
from collections import deque


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
                queue.append(i)
                visited[i] = True


N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (N + 1)

#dfs(1)
bfs(1)
print(visited.count(True) - 1)
