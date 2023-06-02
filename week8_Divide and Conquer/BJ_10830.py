import sys
sys.setrecursionlimit(10 ** 6)


def divide(a, b):
    if b == 1:
        return a
    else:
        x = divide(a, b // 2)
        if b % 2 == 0:
            return mul_matrix(x, x)
        else:
            return mul_matrix(a, mul_matrix(x, x))


def mul_matrix(matrix1, matrix2):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += matrix1[i][k] * matrix2[k][j]
            temp[i][j] = temp[i][j] % 1000

    return temp


N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = divide(A, B)

for row in result:
    for elem in row:
        print(elem % 1000, end=" ")
    print()
