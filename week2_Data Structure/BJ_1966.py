from collections import deque


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dq = deque(list(map(int, input().split())))

    count = 1
    while dq:
        maximum = max(dq)
        now = dq.popleft()

        #현재 선택한 문서의 중요도가 제일 높고 Queue의 제일 앞에 있는 경우
        if now == maximum and M == 0:
            print(count)
            break
        else:
            #현재 선택한 문서가 Queue의 제일 앞에 있지만 제일 높은 중요도가 아닌 경우
            if now != maximum:
                dq.append(now)
            #현재 선택한 문서의 중요도가 제일 높지만 Queue의 제일 앞에 있지 않은 경우
            elif M != 0:
                count += 1

            M -= 1
            if M < 0:
                M = len(dq) - 1
