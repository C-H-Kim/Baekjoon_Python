import sys
from collections import deque


def bfs(start):
    queue = deque([[start, 0]])
    visited[start] = True
    # S와 G가 같은 경우 0이라는 답이 나올 수 있어 ans을 0이 아닌 나올 수 없는 값으로 default setting 해야한다.
    ans = -1

    while queue:
        v, depth = queue.popleft()
        if v == G:
            ans = depth
            break

        for cur_floor in [v + U, v - D]:
            if (0 < cur_floor <= F) and not visited[cur_floor]:
                visited[cur_floor] = True
                queue.append([cur_floor, depth + 1])

    return ans


F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [False] * (F + 1)

answer = bfs(S)

if answer == -1:
    print("use the stairs")
else:
    print(answer)
