import sys

N = int(sys.stdin.readline())
member_list = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    member_list.append([age, name])

member_list.sort(key=lambda x: x[0])

for i in range(N):
    print(*member_list[i])
