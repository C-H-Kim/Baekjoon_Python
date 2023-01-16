import sys

N = int(input())
stair = [0] * 300
dp = [0] * 300

for i in range(N):
    stair[i] = int(sys.stdin.readline().rstrip())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
for i in range(3, N):
    # stair[i] + dp[i - 2] : 마지막의 전 계단을 밟지 않는 경우
    # stair[i] + stair[i - 1] + dp[i - 3] : 마지막의 전 계단을 밟는 경우
    dp[i] = max(stair[i] + dp[i - 2], stair[i] + stair[i - 1] + dp[i - 3])

print(dp[N - 1])
