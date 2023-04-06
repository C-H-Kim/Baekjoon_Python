import sys
from collections import deque


def bfs(start):
    depth_list = [0] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in relation[v]:
            if not visited[i]:
                depth_list[i] = depth_list[v] + 1
                visited[i] = True
                queue.append(i)

    return sum(depth_list)


N, M = map(int, sys.stdin.readline().split())
relation = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    relation[A].append(B)
    relation[B].append(A)

sum_list = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    sum_list.append(bfs(i))

print(sum_list.index(min(sum_list)) + 1)
