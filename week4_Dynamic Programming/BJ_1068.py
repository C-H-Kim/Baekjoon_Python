import sys


def dfs(rNode):
    global parent_list
    # 해당 노드의 부모 노드를 -2로 변경함으로써 제거된 것을 표시
    parent_list[rNode] = -2

    for i in range(len(parent_list)):
        # 현재 참조하고 있는 노드의 부모의 노드가 제거할 노드와 같다면 재귀
        if parent_list[i] == rNode:
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
