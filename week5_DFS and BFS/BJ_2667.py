import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(row, col):
    global house_cnt
    graph[row][col] = -1

    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if (0 <= nx < N) and (0 <= ny < N):
            if graph[nx][ny] == 1:
                dfs(nx, ny)
                house_cnt += 1


def bfs(row, col):
    global house_cnt
    queue = deque([[row, col]])
    graph[row][col] = -1

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if (0 <= nx < N) and (0 <= ny < N):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = -1
                    queue.append([nx, ny])
                    house_cnt += 1


N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
house = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_cnt = 1
            # dfs(i, j)
            bfs(i, j)
            house.append(house_cnt)

house.sort()
print(len(house))
for cnt in house:
    print(cnt)
