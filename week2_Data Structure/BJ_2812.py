N, K = map(int, input().split())
num = list(map(int, input()))
stack = []
k = K

for i in range(N):
    while stack:
        if stack[-1] < num[i] and k > 0:
            stack.pop()
            k -= 1
        else:
            break

    stack.append(num[i])

print(''.join(map(str, stack[:N - K])))
