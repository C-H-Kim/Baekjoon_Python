import sys
from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    queue = deque([[row, col]])
    visited[row][col] = True
    movement_coord = [[row, col]]

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < N) and (0 <= nc < N) and not visited[nr][nc]:
                if L <= abs(graph[r][c] - graph[nr][nc]) <= R:
                    visited[nr][nc] = True
                    queue.append([nr, nc])
                    movement_coord.append([nr, nc])

    return movement_coord


N, L, R = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
day = 0

while True:
    visited = [[False] * N for _ in range(N)]
    movement_flag = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                movement_country = bfs(i, j)

                if len(movement_country) > 1:
                    movement_flag = True

                    avg_population = sum([graph[x][y] for x, y in movement_country]) // len(movement_country)
                    for x, y in movement_country:
                        graph[x][y] = avg_population

    if not movement_flag:
        break

    day += 1

print(day)
