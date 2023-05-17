import sys


def quadtree(x, y, n):
    global answer
    pivot = video[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if video[i][j] != pivot:
                answer.append("(")

                quadtree(x, y, n // 2)
                quadtree(x, y + n // 2, n // 2)
                quadtree(x + n // 2, y, n // 2)
                quadtree(x + n // 2, y + n // 2, n // 2)

                answer.append(")")
                return

    if pivot == 0:
        answer.append(0)
    else:
        answer.append(1)


N = int(sys.stdin.readline())
video = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

answer = []
quadtree(0, 0, N)

for char in answer:
    print(char, end="")
