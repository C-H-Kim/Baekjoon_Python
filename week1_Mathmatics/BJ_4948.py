def is_prime():
    global arr
    arr[0] = arr[1] = False

    for i in range(2, len(arr)):
        if arr[i]:
            j = 2

            while i * j < len(arr):
                arr[i * j] = False
                j += 1


arr = [True] * 246913
is_prime()

while True:
    n = int(input())

    if n == 0:
        break

    count = 0
    for num in range(n + 1, 2 * n + 1):
        if arr[num]:
            count += 1

    print(count)
