import sys
sys.setrecursionlimit(10 ** 6)


def solution(n, x):
    if n == 0:
        return x

    # n이 1이상일 때
    if x == 1:
        return 0
    # 절반 밑으로 먹었을 때
    elif x <= total[n - 1] + 1:
        return solution(n - 1, x - 1)
    # 딱 절반을 먹었을 때
    elif x == 1 + total[n - 1] + 1:
        return patty[n - 1] + 1
    # 절반과 전체 사이로 먹었을 때
    elif x < total[n]:
        return patty[n - 1] + 1 + solution(n - 1, x - (1 + total[n - 1] + 1))
    # 전체 다 먹었을 때
    else:
        return patty[n]


N, X = map(int, sys.stdin.readline().split())

# 인덱스 : 레벨 / 원소 : 해당 레벨 햄버거의 번과 패티 개수
total = [1] * 51
# 인덱스 : 레벨 / 원소 : 해당 레벨 햄버거의 패티 개수
patty = [1] * 51

for i in range(1, N + 1):
    total[i] = 1 + total[i - 1] + 1 + total[i - 1] + 1
    patty[i] = patty[i - 1] + 1 + patty[i - 1]

print(solution(N, X))
