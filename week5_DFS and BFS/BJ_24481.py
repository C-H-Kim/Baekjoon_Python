import sys
sys.setrecursionlimit(10 ** 6)


def dfs(start, depth):
    visited[start] = depth

    for next in graph[start]:
        if visited[next] == -1:
            dfs(next, depth + 1)


N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

for vertex in graph:
    vertex.sort()

dfs(R, 0)

for i in range(1, N + 1):
    print(visited[i])
