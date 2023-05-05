import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col):
    global size
    hall[row][col] = 0 # 방문처리

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if (1 <= nr < N + 1) and (1 <= nc < M + 1):
            if hall[nr][nc]:
                dfs(nr, nc)
                size += 1


def bfs(row, col):
    global size
    queue = deque([[row, col]])
    hall[row][col] = 0 # 방문 처리

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (1 <= nr < N + 1) and (1 <= nc < M + 1):
                if hall[nr][nc]:
                    hall[nr][nc] = 0
                    queue.append([nr, nc])
                    size += 1


N, M, K = map(int, sys.stdin.readline().split())
hall = [[0] * (M + 1) for _ in range(N + 1)]

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    hall[r][c] = 1

max_size = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if hall[i][j] == 1:
            size = 1
            # dfs(i, j)
            bfs(i, j)
            max_size = max(max_size, size)

print(max_size)
