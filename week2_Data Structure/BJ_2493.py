import sys

N = int(input())
top_list = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        #stack에 있는 탑보다 현재 탑이 더 크다면 stack에서 pop
        #현재 탑보다 작은 탑들은 연산할 필요가 없는 탑을 의미
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
