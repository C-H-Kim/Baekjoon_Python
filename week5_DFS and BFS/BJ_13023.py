import sys
sys.setrecursionlimit(10 ** 6)


def dfs(depth, start):
    global result
    visited[start] = True

    if depth == 5:
        result = True
        return

    for v in friend[start]:
        if not visited[v]:
            dfs(depth + 1, v)
            visited[v] = False


N, M = map(int, sys.stdin.readline().split())
friend = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    friend[a].append(b)
    friend[b].append(a)

result = False
visited = [False] * N

for i in range(N):
    dfs(1, i)
    visited[i] = False

    if result:
        break

print(1 if result else 0)
