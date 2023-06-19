import sys
from collections import deque


def bfs(idx):
    queue = deque([[idx, 0]])
    visited[idx] = True
    answer = -1

    while queue:
        index, depth = queue.popleft()
        # print(index, depth)

        if index == N - 1:
            answer = depth
            break

        for i in range(1, A[index] + 1):
            if index + i >= N or visited[index + i]:
                continue
            queue.append([index + i, depth + 1])
            visited[index + i] = True

    return answer


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
visited = [False] * N

print(bfs(0))
