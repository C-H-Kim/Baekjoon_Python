import sys
from collections import deque
sys.setrecursionlimit(10**6)


def dfs(root):
    for v in tree[root]:
        if visited[v] == 0:
            visited[v] = root
            dfs(v)


def bfs(root):
    queue = deque([root])

    while queue:
        parent = queue.popleft()
        for v in tree[parent]:
            if visited[v] == 0:
                visited[v] = parent
                queue.append(v)


N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    i, j = map(int, sys.stdin.readline().split())
    tree[i].append(j)
    tree[j].append(i)

visited = [0] * (N + 1)

#dfs(1)
bfs(1)

for i in range(2, N + 1):
    print(visited[i])
