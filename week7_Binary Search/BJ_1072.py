import sys

X, Y = map(int, sys.stdin.readline().split())
Z = (Y * 100) // X

if Z >= 99:
    print(-1)
else:
    start = 1
    end = X
    ans = 0

    while start <= end:
        mid = (start + end) // 2

        if (Y + mid) * 100 // (X + mid) > Z:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1

    print(ans)
