from math import sqrt
import sys


def is_prime():
    global arr
    arr[0] = arr[1] = False

    for i in range(2, int(sqrt(len(arr))) + 1):
        if not arr[i]:
            continue

        j = i * i
        while j < len(arr):
            arr[j] = False
            j += i

    return


arr = [True] * 1000001
is_prime()

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    a = 0
    b = n

    while True:
        if arr[a] and arr[b]:
            print(f"{n} = {a} + {b}")
            break

        a += 1
        b -= 1
