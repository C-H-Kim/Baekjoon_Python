import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
#자신만으로 수열의 길이가 1이기 때문에 1로 초기화
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        #증가 수열이 되려면 마지막에 추가하려는 수가 그 이전의 수들보다 커야 함
        if A[i] > A[j]:
            #그 중 최장이 될 수 있게 max로 더 긴 것을 선택
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
