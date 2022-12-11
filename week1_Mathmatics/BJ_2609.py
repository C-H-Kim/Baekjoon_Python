def gcd(n, m):
    if n < m:
        n, m = m, n
    if n % m == 0:
        return m

    return gcd(m, n % m)


N, M = map(int, input().split())
G = gcd(N, M)

print(G)
print(N * M // G)
