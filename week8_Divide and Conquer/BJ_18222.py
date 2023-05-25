import sys


def thue_morse(k):
    if k == 0:
        return 0
    elif k % 2 == 0:
        return thue_morse(k // 2)
    else:
        return 1 - thue_morse(k // 2)


K = int(sys.stdin.readline())
print(thue_morse(K - 1))
