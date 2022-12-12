from math import sqrt


def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b

    return gcd(b, a % b)


N = int(input())
num_list = [int(input()) for _ in range(N)]
num_list.sort()
interval = []

for i in range(N - 1):
    interval.append(num_list[i + 1] - num_list[i])

G = interval[0]
for i in range(1, len(interval)):
    G = gcd(G, interval[i])

res = []
for i in range(2, int(sqrt(G)) + 1):
    if G % i == 0:
        if i == G // i:
            res.append(i)
        else:
            res.append(i)
            res.append(G // i)

res.append(G)
res.sort()

print(*res)
