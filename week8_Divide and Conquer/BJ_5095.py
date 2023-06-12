import sys
sys.setrecursionlimit(10 ** 6)


def divide(a, p):
    if p == 1:
        return a
    else:
        x = divide(a, p // 2)
        if p % 2 == 0:
            return mul_matrix(x, x)
        else:
            return mul_matrix(a, mul_matrix(x, x))


def mul_matrix(matrix1, matrix2):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += matrix1[i][k] * matrix2[k][j]
            temp[i][j] = temp[i][j] % M

    return temp


while True:
    N, M, P = map(int, sys.stdin.readline().split())

    if N == 0 and M == 0 and P == 0:
        break

    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    result = divide(A, P)

    for row in result:
        for elem in row:
            print(elem % M, end=" ")
        print()
    print()
