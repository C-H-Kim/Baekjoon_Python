import math
import sys

N = int(sys.stdin.readline())
sqrt_N = int(math.sqrt(N)) + 1

dp = [i for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(2, sqrt_N):
        # min 보다는 if문이 낫다. min의 경우는 반드시 실행해야 해서 if문 보다 시간이 더 걸린다.
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1

print(dp[N])
