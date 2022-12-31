N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))

num_list.sort()
print("\n".join(map(str, num_list)))
