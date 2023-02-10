from collections import deque
import sys


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(N + 1):
    graph[i].sort()

dfs_visited = [False] * len(graph)
bfs_visited = [False] * len(graph)

dfs(graph, V, dfs_visited)
print()
bfs(graph, V, bfs_visited)
