import sys
from collections import deque


def bfs(root):
    queue = deque([[root, 1]])
    answer = -1

    while queue:
        v, depth = queue.popleft()
        if v == B:
            answer = depth
            break

        if v * 2 <= B:
            queue.append([v * 2, depth + 1])

        temp = int(str(v) + "1")
        if temp <= B:
            queue.append([temp, depth + 1])

    return answer


A, B = map(int, sys.stdin.readline().split())
print(bfs(A))
