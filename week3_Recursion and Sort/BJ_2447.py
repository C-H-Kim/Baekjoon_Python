def star(x, y, n, blank):
    global arr
    if blank:
        for i in range(x, x + n):
            for j in range(y, y + n):
                arr[i][j] = " "
        return

    if n == 1:
        arr[x][y] = "*"
        return

    count = 0
    for i in range(x, x + n, n // 3):
        for j in range(y, y + n, n // 3):
            count += 1
            if count == 5:
                star(i, j, n // 3, True)
            else:
                star(i, j, n // 3, False)


N = int(input())
arr = [["-"] * N for _ in range(N)]

star(0, 0, N, False)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end="")
    print()
