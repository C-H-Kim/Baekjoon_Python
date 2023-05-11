import sys

X = int(sys.stdin.readline())
count = 0

for i in range(7):
    if X & (1 << i):
        count += 1

print(count)
