import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)


def dfs(cur_v, cur_color):
    visited[cur_v] = True
    color[cur_v] = cur_color

    for next_v in graph[cur_v]:
        if not visited[next_v]:
            temp_result = dfs(next_v, cur_color * -1)
            if not temp_result:
                return False

        elif color[next_v] == color[cur_v]:
            return False

    return True


def bfs(start, start_color):
    queue = deque([start])
    visited[start] = True
    color[start] = start_color

    while queue:
        cur_v = queue.popleft()

        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                color[next_v] = color[cur_v] * -1
                queue.append(next_v)

            elif color[next_v] == color[cur_v]:
                return False

    return True


T = int(sys.stdin.readline())

for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())

        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (V + 1)
    color = [0] * (V + 1)
    biFlag = True

    for i in range(1, V + 1):
        if not visited[i]:
            biFlag = dfs(i, 1)
            # biFlag = bfs(i, 1)

            if not biFlag:
                break

    print("YES" if biFlag else "NO")
