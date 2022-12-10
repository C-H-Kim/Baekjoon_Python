def is_prime(num):
    arr = [True] * (num + 1)
    arr[0] = arr[1] = False

    for i in range(2, num + 1):
        if arr[i]:
            j = 2

            while i * j <= num:
                arr[i * j] = False
                j += 1

    return arr


M, N = map(int, input().split())

check_prime = is_prime(N)
for i in range(M, N + 1):
    if check_prime[i]:
        print(i)
