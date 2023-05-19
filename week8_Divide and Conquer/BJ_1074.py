import sys

sys.setrecursionlimit(10 ** 6)


def solution(x, y, n):
    global order

    if x == r and y == c:
        print(order)
        exit(0)

    if n == 1:
        order += 1
        return

    if not(x <= r < x + n and y <= c < y + n):
        order += n * n
        return

    solution(x, y, n // 2)  # 1사분면
    solution(x, y + n // 2, n // 2)  # 2사분면
    solution(x + n // 2, y, n // 2)  # 3사분면
    solution(x + n // 2, y + n // 2, n // 2)  # 4사분면


N, r, c = map(int, sys.stdin.readline().split())

order = 0
line = 2 ** N
solution(0, 0, line)
