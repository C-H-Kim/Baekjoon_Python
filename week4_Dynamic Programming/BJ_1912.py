import sys

N = int(input())
array = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    # 이전까지의 합 + 현재 값 < 현재 값 이라면
    # 이전까지의 연속을 끊고 새로운 연속을 시작하는 것을 의미
    array[i] = max(array[i], array[i] + array[i - 1])

print(max(array))
