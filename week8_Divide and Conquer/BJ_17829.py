import sys


def solution(x, y, n):
    if n == 2:
        temp = []
        for i in range(x, x + n):
            for j in range(y, y + n):
                temp.append(matrix[i][j])
        temp.sort(reverse=True)

        return temp[1]

    left_top = solution(x, y, n // 2)
    right_top = solution(x, y + n // 2, n // 2)
    left_bottom = solution(x + n // 2, y, n // 2)
    right_bottom = solution(x + n // 2, y + n // 2, n // 2)

    result = [left_top, right_top, left_bottom, right_bottom]
    result.sort(reverse=True)

    return result[1]


N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = solution(0, 0, N)
print(answer)
