import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < N) and (0 <= nc < M):
                if box[nr][nc] == 0:
                    box[nr][nc] = box[r][c] + 1
                    queue.append([nr, nc])


M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = deque([])

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])

bfs()

max_list = []
for i in range(N):
    max_list.append(max(box[i]))

if any(0 in l for l in box):
    print(-1)
else:
    print(max(max_list) - 1)
