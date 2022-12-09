remainder = [False] * 42

for _ in range(10):
    remainder[int(input()) % 42] = True

count = 0
for flag in remainder:
    if flag:
        count += 1

print(count)
