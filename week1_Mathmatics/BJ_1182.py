def solution(idx, sum):
    global count

    if idx >= N:
        return

    sum += num_list[idx]

    if sum == S:
        count += 1

    #현재 원소를 포함시키는 경우
    solution(idx + 1, sum)
    #현재 원소를 포함시키지 않는 경우
    solution(idx + 1, sum - num_list[idx])

    return


N, S = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

solution(0, 0)
print(count)
