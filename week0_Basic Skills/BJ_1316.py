N = int(input())

count = 0
for _ in range(N):
    S = input()
    check = [False] * 26

    if len(S) == 1:
        count += 1
        continue

    i = 0
    while i < len(S):
        if i == 0:
            check[ord(S[i]) - ord('a')] = True
        else:
            if check[ord(S[i]) - ord('a')] and S[i] != S[i - 1]:
                break
            else:
                check[ord(S[i]) - ord('a')] = True
                pass
        i += 1

    if i == len(S):
        count += 1

print(count)
