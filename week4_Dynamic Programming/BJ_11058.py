N = int(input())
dp = [i for i in range(102)]

for i in range(6, 101):
    dp[i] = max(dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4)

print(dp[N])
