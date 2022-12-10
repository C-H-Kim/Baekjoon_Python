def is_prime():
    arr = [True] * 1001
    arr[0] = arr[1] = False

    for i in range(2, 1001):
        if arr[i]:
            j = 2
            while i * j <= 1000:
                arr[i * j] = False
                j += 1

    return arr


int(input())
num_list = list(map(int, input().split()))

check_prime = is_prime()
count = 0

for num in num_list:
    if check_prime[num]:
        count += 1

print(count)
