import sys
from collections import deque


def bfs(s):
    queue = deque([[s, 0]])
    visited[s] = True
    answer = -1

    while queue:
        v, depth = queue.popleft()
        if v == dest:
            answer = depth
            break

        for i in family[v]:
            if not visited[i]:
                visited[i] = True
                queue.append([i, depth + 1])

    return answer

N = int(sys.stdin.readline())
family = [[] for _ in range(N + 1)]

start, dest = map(int, sys.stdin.readline().split())

M = int(sys.stdin.readline())
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)

for i in range(N + 1):
    family[i].sort()

visited = [False] * (N + 1)

print(bfs(start))
