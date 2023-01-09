X = int(input())
answer = [0] * (X + 1)

for i in range(2, X + 1):
    #1을 빼는 연산
    answer[i] = answer[i - 1] + 1

    if i % 3 == 0:
        #1을 빼는 것과 3으로 나누는 것 중 최소가 되는 것을 고른다.
        answer[i] = min(answer[i], answer[i // 3] + 1)
    if i % 2 == 0:
        #1을 빼는 것과 2로 나누는 것 중 최소가 되는 것을 고른다.
        answer[i] = min(answer[i], answer[i // 2] + 1)

print(answer[X])
