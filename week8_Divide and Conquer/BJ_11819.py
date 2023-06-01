import sys
sys.setrecursionlimit(10 ** 6)


def user_pow(a, b, c):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        x = user_pow(a, b // 2, c)
        if b % 2 == 0:
            return mod_calc(x, x, c)
        else:
            return mod_calc(mod_calc(x, x, c), a, c)


def mod_calc(num1, num2, mod):
    return (num1 * num2) % mod


A, B, C = map(int, sys.stdin.readline().split())
print(user_pow(A % C, B, C))
