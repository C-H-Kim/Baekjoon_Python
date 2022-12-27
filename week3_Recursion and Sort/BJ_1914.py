def hanoi(n, start, by, end):
    if n == 0:
        return

    hanoi(n - 1, start, end, by)
    print(start, end)
    hanoi(n - 1, by, start, end)


N = int(input())
K = 2 ** N - 1

print(K)
if N <= 20:
    hanoi(N, 1, 2, 3)
