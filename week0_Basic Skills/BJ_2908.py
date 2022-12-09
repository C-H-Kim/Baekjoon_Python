A, B = map(str, input().split())

A = "".join(reversed(A))
B = "".join(reversed(B))

A = int(A)
B = int(B)

print(max(A, B))
