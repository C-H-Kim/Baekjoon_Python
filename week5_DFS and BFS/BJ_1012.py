import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, col):
    queue = deque([[row, col]])
    graph[row][col] = -1

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = -1
                    queue.append([nx, ny])


T = int(input())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
