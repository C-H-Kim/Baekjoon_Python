import sys
from collections import deque
sys.setrecursionlimit(10**6)


dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def dfs(row, col):
    graph[row][col] = -1

    for i in range(8):
        nx = row + dx[i]
        ny = col + dy[i]
        if (0 <= nx < h) and (0 <= ny < w):
            if graph[nx][ny] == 1:
                dfs(nx, ny)


def bfs(row, col):
    queue = deque([[row, col]])
    graph[row][col] = -1

    while queue:
        r, c = queue.popleft()
        for i in range(8):
            nx = r + dx[i]
            ny = c + dy[i]
            if (0 <= nx < h) and (0 <= ny < w):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = -1
                    queue.append([nx, ny])


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                # dfs(i, j)
                bfs(i, j)
                cnt += 1

    print(cnt)
