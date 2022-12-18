import sys

Lside = list(sys.stdin.readline().rstrip())
Rside = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if Lside:
            Rside.append(Lside.pop())
    elif command[0] == 'D':
        if Rside:
            Lside.append(Rside.pop())
    elif command[0] == 'B':
        if Lside:
            Lside.pop()
    else:
        Lside.append(command[1])

Lside.extend(reversed(Rside))
print(''.join(Lside))
