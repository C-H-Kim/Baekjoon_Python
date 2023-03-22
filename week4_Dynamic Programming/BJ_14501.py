import sys

N = int(sys.stdin.readline())
T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N + 1):
    T[i], P[i] = map(int, sys.stdin.readline().split())

dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])   # 이전까지의 최대값(dp)를 가져오기 위함
    done_date = i + T[i] - 1        # 시작일 포함
    if done_date <= N:
        dp[done_date] = max(dp[done_date], dp[i - 1] + P[i])    # dp[i]는 해당 일을 하지 않는 것을 의미해 dp[i - 1]가 되어야 한다.

print(max(dp))
