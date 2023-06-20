import sys


def dfs(pNode):
    global parent_list
    parent_list[pNode] = -2

    for i in range(len(parent_list)):
        if parent_list[i] == pNode:
            dfs(i)


N = int(sys.stdin.readline())
parent_list = list(map(int, sys.stdin.readline().split()))
R = int(sys.stdin.readline())

dfs(R)
count = 0
for i in range(len(parent_list)):
    if parent_list[i] != -2 and i not in parent_list:
        count += 1

print(count)
