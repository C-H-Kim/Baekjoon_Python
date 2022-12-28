import sys

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0


def cut(x, y, n):
    global board, white, blue
    pivot = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != pivot:
                cut(x, y, n // 2)#1사분면
                cut(x, y + n // 2, n // 2)#2사분면
                cut(x + n // 2, y, n // 2)#3사분면
                cut(x + n // 2, y + n // 2, n // 2)#4사분면
                return

    if pivot == 0:
        white += 1
    else:
        blue += 1


cut(0, 0, N)
print(white)
print(blue)
