import sys

N = sys.stdin.readline().rstrip()
num_list = []

for n in N:
    num_list.append(int(n))

num_list.sort(reverse=True)

print("".join(map(str, num_list)))
