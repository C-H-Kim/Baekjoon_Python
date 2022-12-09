c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
S = input()

for cro in c:
    S = S.replace(cro, "*")

print(len(S))
