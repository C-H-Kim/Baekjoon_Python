import sys
sys.setrecursionlimit(10 ** 6)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col, num):
    global answer

    if len(num) == 6:
        if num not in answer:
            answer.add(num)
        return

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if (0 <= nr < 5) and (0 <= nc < 5):
            dfs(nr, nc, num + num_board[nr][nc])


num_board = [list(map(str, sys.stdin.readline().split())) for _ in range(5)]

answer = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, num_board[i][j])

print(len(answer))
