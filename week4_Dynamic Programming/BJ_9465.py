import sys

T = int(input())
for _ in range(T):
    N = int(input())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    dp = A[:]

    if N == 1:
        print(max(A[0][0], A[1][0]))
        continue

    dp[0][1] = A[0][1] + A[1][0]
    dp[1][1] = A[1][1] + A[0][0]

    for c in range(2, N):
        dp[0][c] = max(dp[1][c - 1], dp[1][c - 2]) + A[0][c]
        dp[1][c] = max(dp[0][c - 1], dp[0][c - 2]) + A[1][c]

    print(max(dp[0][N - 1], dp[1][N - 1]))
