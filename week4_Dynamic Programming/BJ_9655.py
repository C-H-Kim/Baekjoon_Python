import sys

N = int(sys.stdin.readline())
dp = [False] * 1001
dp[1], dp[2], dp[3] = True, False, True

for i in range(4, 1001):
    if dp[i - 1] or dp[i - 3]:
        dp[i] = False
    else:
        dp[i] = True

print("SK" if dp[N] else "CY")
