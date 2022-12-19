import sys

N = int(input())
top_list = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        #현재 타워보다 큰 타워가 있을 때까지 stack을 탐색
        if top_list[stack[-1]] < top_list[i]:
            stack.pop()
        #현재 타워보다 큰 타워가 있다면 해당 위치를 answer에 push
        else:
            answer.append(stack[-1] + 1)
            break

    #stack을 다 탐색해도 현재 타워보다 큰 타워가 없다는 것을 의미
    if not stack:
        answer.append(0)
    stack.append(i)

print(*answer)
