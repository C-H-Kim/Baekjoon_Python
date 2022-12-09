S = input()
count = 0

for s in S:
    if s >= 'W':
        count += 10
    elif s >= 'T':
        count += 9
    elif s >= 'P':
        count += 8
    elif s >= 'M':
        count += 7
    elif s >= 'J':
        count += 6
    elif s >= 'G':
        count += 5
    elif s >= 'D':
        count += 4
    elif s >= 'A':
        count += 3
    else:
        pass

print(count)
