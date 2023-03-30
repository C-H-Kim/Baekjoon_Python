import sys
from collections import deque


dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs(row, col):
    queue = deque([[row, col, 0]])
    visited[row][col] = True

    while queue:
        r, c, depth = queue.popleft()
        if r == dest_x and c == dest_y:
            return depth

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < I) and (0 <= nc < I) and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append([nr, nc, depth + 1])


T = int(sys.stdin.readline())
for _ in range(T):
    I = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split())
    dest_x, dest_y = map(int, sys.stdin.readline().split())

    visited = [[False] * I for _ in range(I)]

    print(bfs(start_x, start_y))
