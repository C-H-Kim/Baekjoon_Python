import sys


def binary_search(char_power):
    start = 0
    end = len(power_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if char_power > power_list[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return end + 1


N, M = map(int, sys.stdin.readline().split())

name_list = []
power_list = []

for _ in range(N):
    name, power = sys.stdin.readline().split()
    power = int(power)

    # 같은 전투력이면 먼저 입력된 칭호 하나만 저장
    # 전투력 상한값은 비내림차순으로 주어지기 때문에 list의 top만 보면 된다.
    if power_list and power_list[-1] == power:
        continue

    name_list.append(name)
    power_list.append(power)

for _ in range(M):
    char_power = int(sys.stdin.readline())
    result = binary_search(char_power)

    print(name_list[result])
