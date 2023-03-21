import sys

T = int(sys.stdin.readline())
for _ in range(T):
    dp = [[0] * 30 for _ in range(30)]
    for i in range(1, 30):
        for j in range(1, 30):
            if i == 1:
                dp[i][j] = j
            elif i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

    N, M = map(int, sys.stdin.readline().split())
    print(dp[N][M])
