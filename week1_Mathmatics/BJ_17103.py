def eratos():
    arr[0] = arr[1] = False

    for i in range(2, int(len(arr) ** 0.5) + 1):
        if not arr[i]:
            continue

        j = i * i
        while j < len(arr):
            arr[j] = False
            j += i


def goldbach(num):
    a = num // 2
    b = num // 2
    count = 0

    while a != num:
        if arr[a] and arr[b]:
            count += 1

        a += 1
        b -= 1

    return count


T = int(input())
arr = [True] * 1000001
eratos()

for _ in range(T):
    N = int(input())

    print(goldbach(N))
