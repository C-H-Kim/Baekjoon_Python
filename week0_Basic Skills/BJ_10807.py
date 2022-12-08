N = int(input())
num_list = list(map(int, input().split()))
v = int(input())
count = 0

for i in range(N):
    if v == num_list[i]:
        count += 1

print(count)
