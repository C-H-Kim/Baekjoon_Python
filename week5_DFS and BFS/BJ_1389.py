import sys
from collections import deque


def bfs(start, dest):
    queue = deque([[start, 0]])
    visited[start] = True
    answer = 0

    while queue:
        v, depth = queue.popleft()
        if v == dest:
            answer = depth
            break

        for i in relation[v]:
            if not visited[i]:
                visited[i] = True
                queue.append([i, depth + 1])

    return answer


N, M = map(int, sys.stdin.readline().split())
relation = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    relation[A].append(B)
    relation[B].append(A)

sum_list = []

for i in range(1, N + 1):
    sum = 0
    for j in range(1, N + 1):
        visited = [False] * (N + 1)
        if i != j:
            sum += bfs(i, j)
        else:
            continue

    sum_list.append(sum)

print(sum_list.index(min(sum_list)) + 1)
