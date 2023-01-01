import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(len(arr)):
    while arr[i] > 0:
        sys.stdout.write(str(i) + "\n")
        arr[i] -= 1
