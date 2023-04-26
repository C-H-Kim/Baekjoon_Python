import sys

N = int(sys.stdin.readline())
dp = [[0, 0, 0] for _ in range(N + 1)]

dp[1][0] = 1    # 아무것도 선택하지 않은 경우
dp[1][1] = 1    # 왼쪽을 선택한 경우
dp[1][2] = 1    # 오른쪽을 선택한 경우

for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[N]) % 9901)
