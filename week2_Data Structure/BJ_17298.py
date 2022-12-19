N = int(input())
num_list = list(map(int, input().split()))
stack = []
answer = [-1] * N

for i in range(N):
    while stack:
        if num_list[stack[-1]] < num_list[i]:
            answer[stack[-1]] = num_list[i]
            stack.pop()
        else:
            break

    stack.append(i)

print(*answer)
