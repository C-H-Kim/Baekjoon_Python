import sys


def dfs(v):
    visited[v] = True
    next = graph[v]

    if not visited[next]:
        dfs(next)


T = int(input())

for _ in range(T):
    cycle = 0
    N = int(input())
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (N + 1)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cycle += 1

    print(cycle)
