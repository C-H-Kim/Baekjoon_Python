import sys

N = int(input())
wine = [int(sys.stdin.readline()) for _ in range(N)]
dp = wine[:]

if N == 1:
    print(dp[0])
elif N == 2:
    print(dp[0] + dp[1])
else:
    dp[1] += dp[0]
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])

    for i in range(3, N):
        dp[i] = max(wine[i] + dp[i - 2], wine[i] + wine[i - 1] + dp[i - 3], dp[i - 1])

    print(dp[N - 1])
