S = list(input())
stack = []
count = 0

for i in range(len(S)):
    if S[i] == '(':
        stack.append('(')
    else:
        if S[i - 1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)
