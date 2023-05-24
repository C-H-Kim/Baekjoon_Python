import sys


def solution(start, end, k):
    if k == 1:
        flavor[start:end + 1] = sorted(flavor[start:end + 1])
        return

    mid = (start + end) // 2
    solution(start, mid, k // 2)
    solution(mid + 1, end, k // 2)


N = int(sys.stdin.readline())
flavor = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())

solution(0, N - 1, K)

print(*flavor)
