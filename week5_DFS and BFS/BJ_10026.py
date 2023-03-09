import sys
from collections import deque
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(row, col):
    visited[row][col] = True
    cur_color = paint[row][col]

    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if (0 <= nx < N) and (0 <= ny < N):
            if not visited[nx][ny]:
                if paint[nx][ny] == cur_color:
                    dfs(nx, ny)


def bfs(row, col):
    queue = deque([[row, col]])
    visited[row][col] = True
    cur_color = paint[row][col]

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if (0 <= nx < N) and (0 <= ny < N):
                if not visited[nx][ny]:
                    if paint[nx][ny] == cur_color:
                        visited[nx][ny] = True
                        queue.append([nx, ny])


N = int(sys.stdin.readline())
paint = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

not_weakness_count = 0
color_weakness_count = 0

# 적록색약이 아닌 사람이 봤을 때 구역의 개수
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            # bfs(i, j)
            not_weakness_count += 1

# R와 G을 하나의 색으로 통일
for i in range(N):
    for j in range(N):
        if paint[i][j] == 'G':
            paint[i][j] = 'R'

# 방문 여부 초기화
visited = [[False] * N for _ in range(N)]

# 적록색약인 사람이 봤을 때 구역의 개수
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            # bfs(i, j)
            color_weakness_count += 1

print(not_weakness_count, color_weakness_count)
