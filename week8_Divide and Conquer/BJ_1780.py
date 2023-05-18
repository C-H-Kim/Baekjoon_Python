import sys


def cut(x, y, n):
    global minus, zero, plus
    pivot = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != pivot:
                next = n // 3

                cut(x, y, next)
                cut(x, y + next, next)
                cut(x, y + next * 2, next)

                cut(x + next, y, next)
                cut(x + next, y + next, next)
                cut(x + next, y + next * 2, next)

                cut(x + next * 2, y, next)
                cut(x + next * 2, y + next, next)
                cut(x + next * 2, y + next * 2, next)

                return

    if pivot == -1:
        minus += 1
    elif pivot == 0:
        zero += 1
    else:
        plus += 1


N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

minus = 0
zero = 0
plus = 0

cut(0, 0, N)

print(minus)
print(zero)
print(plus)
