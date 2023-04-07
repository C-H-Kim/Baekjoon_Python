import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(row, col):
    global area
    graph[row][col] = 0

    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if graph[nx][ny] == 1:
                dfs(nx, ny)
                area += 1


def bfs(row, col):
    global area
    queue = deque([[row, col]])
    graph[row][col] = 0

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if (0 <= nx < M) and (0 <= ny < N):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append([nx, ny])
                    area += 1


M, N, K = map(int, sys.stdin.readline().split())
graph = [[1] * N for _ in range(M)]

for _ in range(K):
    col1, row1, col2, row2 = map(int, sys.stdin.readline().split())

    for i in range(row1, row2):
        for j in range(col1, col2):
            graph[i][j] = 0

area_num = 0
area_list = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            area = 1

            # dfs(i, j)
            bfs(i, j)

            area_list.append(area)
            area_num += 1

area_list.sort()
print(area_num)
print(*area_list)
