def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num - 1)


n, m = map(int, input().split())

print(factorial(n) // (factorial(m) * factorial(n - m)))
