N = int(input())
num_list = list(map(int, input().split()))
v = int(input())
count = 0

for i in num_list:
    if v == i:
        count += 1

print(count)
