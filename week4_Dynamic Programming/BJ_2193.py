count = [0, 1, 1]

for i in range(3, 91):
    count.append(count[i - 1] + count[i - 2])

N = int(input())
print(count[N])
