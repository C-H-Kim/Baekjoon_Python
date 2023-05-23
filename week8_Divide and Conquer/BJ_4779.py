import sys


def solution(x, n, blank):
    global arr
    if blank:
        for i in range(x, x + 3 ** n):
            arr[i] = " "
        return

    if n == 0:
        return

    count = 0
    for i in range(x, x + 3 ** n, 3 ** (n - 1)):
        count += 1
        if count == 2:
            solution(i, n - 1, True)
        else:
            solution(i, n - 1, False)


while True:
    try:
        N = int(sys.stdin.readline())

        arr = ['-' for i in range(3 ** N)]
        solution(0, N, False)

        for a in arr:
            print(a, end="")
        print()

    except:
        break
