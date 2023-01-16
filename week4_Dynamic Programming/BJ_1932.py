import copy
import sys

N = int(sys.stdin.readline())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

dp = copy.deepcopy(A)

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + A[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + A[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + A[i][j]

print(max(dp[N - 1]))
