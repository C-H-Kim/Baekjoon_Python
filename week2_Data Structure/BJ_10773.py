import sys

K = int(sys.stdin.readline())
stack = []

for _ in range(K):
    N = int(sys.stdin.readline())
    if N != 0:
        stack.append(N)
    else:
        try:
            stack.pop()
        except:
            pass

print(sum(stack))
