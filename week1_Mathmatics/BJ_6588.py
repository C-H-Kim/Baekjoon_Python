def is_prime():
    global arr
    arr[0] = arr[1] = False

    for i in range(2, len(arr)):
        if arr[i]:
            j = i
            while i * j < len(arr):
                arr[i * j] = False
                j += 1

    return


arr = [True] * 1000001
is_prime()

while True:
    n = int(input())

    if n == 0:
        break

    a = 0
    b = n
    flag = False
    while True:
        if arr[a] and arr[b]:
            print(f"{n} = {a} + {b}")
            flag = True
            break

        a += 1
        b -= 1
