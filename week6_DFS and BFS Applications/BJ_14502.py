import sys
from collections import deque
import copy


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if origin_map[i][j] == 0:
                origin_map[i][j] = 1
                make_wall(count + 1)
                origin_map[i][j] = 0


def bfs():
    global result

    queue = deque()
    test_map = copy.deepcopy(origin_map)
    for i in range(N):
        for j in range(M):
            if test_map[i][j] == 2:
                queue.append([i, j])

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if (0 <= nr < N) and (0 <= nc < M):
                if test_map[nr][nc] == 0:
                    test_map[nr][nc] = 2
                    queue.append([nr, nc])

    safe_zone = 0
    for i in range(N):
        for j in range(M):
            if test_map[i][j] == 0:
                safe_zone += 1

    result = max(result, safe_zone)


N, M = map(int, sys.stdin.readline().split())
origin_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0
make_wall(0)

print(result)
