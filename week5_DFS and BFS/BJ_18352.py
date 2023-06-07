import sys
from collections import deque


def bfs(start):
    global answer_list
    queue = deque([[start, 0]])
    visited[start] = True

    while queue:
        v, depth = queue.popleft()
        if depth == K:
            answer_list.append(v)

        for next in cities[v]:
            if not visited[next]:
                visited[next] = True
                queue.append([next, depth + 1])


N, M, K, X = map(int, sys.stdin.readline().split())

cities = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    cities[A].append(B)

visited = [False] * (N + 1)
answer_list = []

bfs(X)

if answer_list:
    answer_list.sort()
    for answer in answer_list:
        print(answer)
else:
    print(-1)
