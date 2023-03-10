import sys
from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start_x, start_y):
    queue = deque([[start_x, start_y, 0]])
    visited[start_x][start_y] = True

    while queue:
        row, col, depth = queue.popleft()
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if (0 <= nr < N) and (0 <= nc < M):
                if map[nr][nc] == 'L' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append([nr, nc, depth + 1])

    return depth


N, M = map(int, sys.stdin.readline().split())
map = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
max_cnt = 0

for i in range(N):
    for j in range(M):
        if map[i][j] == 'L':
            visited = [[False] * M for _ in range(N)]
            max_cnt = max(max_cnt, bfs(i, j))

print(max_cnt)
