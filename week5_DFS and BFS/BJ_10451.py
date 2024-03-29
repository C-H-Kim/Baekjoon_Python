import sys
from collections import deque

def dfs(v):
    visited[v] = True
    next = graph[v]

    if not visited[next]:
        dfs(next)


def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        next = graph[queue.popleft()]

        if not visited[next]:
            visited[next] = True
            queue.append(next)


T = int(input())

for _ in range(T):
    cycle = 0
    N = int(input())
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (N + 1)

    for i in range(1, N + 1):
        if not visited[i]:
            #dfs(i)
            bfs(i)
            cycle += 1

    print(cycle)
