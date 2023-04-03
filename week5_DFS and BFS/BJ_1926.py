import sys
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, col):
    queue = deque([[row, col]])
    paper[row][col] = 0
    area = 1

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if paper[nx][ny] == 1:
                    paper[nx][ny] = 0
                    queue.append([nx, ny])
                    area += 1

    return area


N, M = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count = 0
max_area = 0

for i in range(N):
    for j in range(M):
        if paper[i][j] == 1:
            max_area = max(max_area, bfs(i, j))
            count += 1

print(count)
print(max_area)
