import sys
from collections import deque


def bfs(start):
    queue = deque([[start, 0]])
    visited[start] = True
    cnt = 0

    while queue:
        v, depth = queue.popleft()
        if depth <= 2:
            cnt += 1
        else:
            break

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append([i, depth + 1])

    return cnt - 1


N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]

M = int(sys.stdin.readline())
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (N + 1)

print(bfs(1))
