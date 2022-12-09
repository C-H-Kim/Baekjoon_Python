N = int(input())

if N < 100:
    count = N
else:
    count = 99
    for i in range(100, N + 1):
        a = i // 100
        b = (i % 100) // 10
        c = i % 10

        if a + c == 2 * b:
            count += 1

print(count)
