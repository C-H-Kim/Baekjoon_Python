import sys
from collections import deque
sys.setrecursionlimit(10**6)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col):
    visited[row][col] = True

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if (0 <= nr < N) and (0 <= nc < N):
            if not visited[nr][nc] and area[nr][nc] > limit:
                dfs(nr, nc)


def bfs(row, col):
    queue = deque([[row, col]])
    visited[row][col] = True

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < N) and (0 <= nc < N):
                if not visited[nr][nc] and area[nr][nc] > limit:
                    visited[nr][nc] = True
                    queue.append([nr, nc])


N = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_list = []
for i in range(N):
    max_list.append(max(area[i]))
max_height = max(max_list)

safezone = []

for limit in range(max_height):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            if not visited[j][k] and area[j][k] > limit:
                # dfs(j, k)
                bfs(j, k)
                count += 1

    safezone.append(count)

print(max(safezone))
