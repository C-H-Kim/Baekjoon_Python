import sys
from collections import deque


dx = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, -1, 1, 0, 0]


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if (0 <= nx < H) and (0 <= ny < N) and (0 <= nz < M):
                if box[nx][ny][nz] == 0:
                    box[nx][ny][nz] = box[x][y][z] + 1
                    queue.append([nx, ny, nz])


M, N, H = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
queue = deque([])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append([i, j, k])

bfs()

answer = 0
for row in box:
    for col in row:
        for val in col:
            if val == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(col))

print(answer - 1)
