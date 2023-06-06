import sys


def solution(cur, mid, n):
    # S(k) = S(k - 1) + 중간 + S(k - 1)
    prev = (cur - mid) // 2

    # N이 첫 번째 S(k - 1)에 있을 경우
    if n <= prev:
        return solution(prev, mid - 1, n)
    # N이 중간에 있을 경우
    elif n <= prev + mid:
        # N이 S(k - 1) + "m"인 경우
        if n == prev + 1:
            return "m"
        else:
            return "o"
    # N이 두 번째 S(k - 1)에 있을 경우
    else:
        return solution(prev, mid - 1, n - prev - mid)


N = int(sys.stdin.readline())

total = 3
k = 0
while N > total:
    k += 1
    # S(k) = S(k - 1) + "moo" + "o" * k + S(k - 1) 이기 때문
    total = total * 2 + k + 3

print(solution(total, k + 3, N))
