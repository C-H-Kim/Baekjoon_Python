import sys

bit = 0
M = int(sys.stdin.readline())

for _ in range(M):
    opt = list(sys.stdin.readline().split())

    if opt[0] == "all":
        bit = (1 << 20) - 1
    elif opt[0] == "empty":
        bit = 0
    else:
        x = int(opt[1]) - 1

        if opt[0] == "add":
            bit = bit | (1 << x)

        elif opt[0] == "remove":
            bit = bit & ~(1 << x)

        elif opt[0] == "check":
            if bit & (1 << x) == 0:
                print(0)
            else:
                print(1)

        elif opt[0] == "toggle":
            bit = bit ^ (1 << x)
