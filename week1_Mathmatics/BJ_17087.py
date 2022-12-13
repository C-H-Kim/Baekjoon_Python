def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b

    return gcd(b, a % b)


N, S = map(int, input().split())
pos_list = list(map(int, input().split()))

diff = []
for pos in pos_list:
    diff.append(abs(S - pos))

G = diff[0]
for i in range(1, N):
    G = gcd(G, diff[i])

print(G)
