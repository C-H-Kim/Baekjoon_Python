import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = True
    global cnt

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[B].append(A)

maxCnt = 0
ans_list = []

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    cnt = 1
    bfs(i)

    if cnt > maxCnt:
        ans_list.clear()
        ans_list.append(i)
        maxCnt = cnt
    elif cnt == maxCnt:
        ans_list.append(i)

print(*ans_list)
