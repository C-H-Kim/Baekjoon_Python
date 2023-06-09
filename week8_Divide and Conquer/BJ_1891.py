import sys
sys.setrecursionlimit(10 ** 6)


def find_coord(idx, r, c, size):
    global row, col, num
    if size == 1:
        row, col = r, c
        return

    size = size // 2
    if num[idx] == '1':
        find_coord(idx + 1, r, c + size, size)
    elif num[idx] == '2':
        find_coord(idx + 1, r, c, size)
    elif num[idx] == '3':
        find_coord(idx + 1, r + size, c, size)
    elif num[idx] == '4':
        find_coord(idx + 1, r + size, c + size, size)


def make_sol(r, c, size, ans):
    if size == 1:
        print(ans)
        return

    size = size // 2
    if (0 <= r < size) and (size <= c < size * 2):
        make_sol(r, c - size, size, ans + '1')
    elif (0 <= r < size) and (0 <= c < size):
        make_sol(r, c, size, ans + '2')
    elif (size <= r < size * 2) and (0 <= c < size):
        make_sol(r - size, c, size, ans + '3')
    elif (size <= r < size * 2) and (size <= c < size * 2):
        make_sol(r - size, c - size, size, ans + '4')


d, num = map(str, sys.stdin.readline().split())
d = int(d)
x, y = map(int, sys.stdin.readline().split())

row, col = 0, 0
find_coord(0, row, col, 2 ** d)

row -= y
col += x

if (0 <= row < 2 ** d) and (0 <= col < 2 ** d):
    make_sol(row, col, 2 ** d, '')
else:
    print(-1)
