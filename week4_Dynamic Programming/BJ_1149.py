import sys

N = int(sys.stdin.readline())
houseColor = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    # i번째에서 빨강을 선택하는 경우
    houseColor[i][0] = min(houseColor[i - 1][1], houseColor[i - 1][2]) + houseColor[i][0]
    # i번째에서 초록을 선택하는 경우
    houseColor[i][1] = min(houseColor[i - 1][0], houseColor[i - 1][2]) + houseColor[i][1]
    # i번째에서 파랑을 선택하는 경우
    houseColor[i][2] = min(houseColor[i - 1][0], houseColor[i - 1][1]) + houseColor[i][2]

print(min(houseColor[N - 1]))
