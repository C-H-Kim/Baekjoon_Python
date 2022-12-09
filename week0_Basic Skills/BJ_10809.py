check = [-1] * 26
S = input()

for s in S:
    if check[ord(s) - 97] == -1:
        check[ord(s) - 97] = S.index(s)

print(*check)
