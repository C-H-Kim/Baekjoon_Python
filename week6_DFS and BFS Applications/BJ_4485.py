import sys
from collections import deque
INF = int(1e9)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start_x, start_y):
    queue = deque([[start_x, start_y]])

    while queue:
        row, col = queue.popleft()
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if (0 <= nr < N) and (0 <= nc < N):
                if cost[nr][nc] > graph[nr][nc] + cost[row][col]:
                    cost[nr][nc] = graph[nr][nc] + cost[row][col]
                    queue.append([nr, nc])


test_case = 0
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    test_case += 1

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cost = [[INF] * N for _ in range(N)]
    cost[0][0] = graph[0][0]

    bfs(0, 0)

    print(f"Problem {test_case}: {cost[N - 1][N - 1]}")
