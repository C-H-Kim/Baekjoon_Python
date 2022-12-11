def is_prime():
    global arr
    arr[0] = arr[1] = False

    for i in range(2, len(arr)):
        if arr[i]:
            j = 2
            while i * j < len(arr):
                arr[i * j] = False
                j += 1

    return


arr = [True] * 10001
is_prime()

T = int(input())

for _ in range(T):
    n = int(input())
    a = n // 2
    b = n // 2

    while True:
        if arr[a] and arr[b]:
            print(a, b)
            break

        a -= 1
        b += 1
