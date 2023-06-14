import sys
from collections import deque


dr = [-2, -2, 0, 2, 2, 0]
dc = [-1, 1, 2, 1, -1, -2]


def bfs(r1, c1):
    queue = deque([[r1, c1, 0]])
    visited[r1][c1] = 0

    while queue:
        r, c, depth = queue.popleft()

        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]

            if (0 <= nr < N) and (0 <= nc < N):
                if visited[nr][nc] == -1:
                    queue.append([nr, nc, depth + 1])
                    visited[nr][nc] = depth + 1


N = int(sys.stdin.readline())
R1, C1, R2, C2 = map(int, sys.stdin.readline().split())

visited = [[-1] * N for _ in range(N)]
bfs(R1, C1)

print(visited[R2][C2])
