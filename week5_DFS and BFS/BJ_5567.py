import sys


def dfs(start, depth):
    visited[start] = True

    if depth == 2:
        return

    for i in graph[start]:
        if not visited[i]:
            depth += 1
            dfs(i, depth)


N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]

M = int(sys.stdin.readline())
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (N + 1)

print(graph)
