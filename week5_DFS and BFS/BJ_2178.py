import sys
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_x, start_y):
    queue = deque([[start_x, start_y, 1]])
    maze[start_x][start_y] = -1

    while queue:
        row, col, depth = queue.popleft()
        if row == N - 1 and col == M - 1:
            break

        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if maze[nx][ny] == 1:
                    maze[nx][ny] = -1
                    queue.append([nx, ny, depth + 1])

    return depth


N, M = map(int, sys.stdin.readline().split())

maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

print(bfs(0, 0))
