import sys
import heapq

N = int(input())
queue = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if queue:
            print(heapq.heappop(queue)[1])
        else:
            print(0)
    else:
        heapq.heappush(queue, (abs(x), x))
