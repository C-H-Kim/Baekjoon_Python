import sys

N = int(sys.stdin.readline())
dp = [100001] * 100001

dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, 100001):
    dp[i] = min(dp[i - 2], dp[i - 5]) + 1

if dp[N] >= 100001:
    print(-1)
else:
    print(dp[N])
