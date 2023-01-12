import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
dp = A.copy()

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))
