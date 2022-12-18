import sys

n = int(sys.stdin.readline())
stack = []
output = []
cur = 1
flag = True

for _ in range(n):
    num = int(sys.stdin.readline())

    while cur <= num:
        stack.append(cur)
        output.append('+')
        cur += 1

    if stack[-1] == num:
        stack.pop()
        output.append('-')
    else:
        print('NO')
        flag = False
        break

if flag:
    for i in output:
        print(i)
