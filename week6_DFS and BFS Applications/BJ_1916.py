import heapq
import sys
INF = int(1e8)


def dijkstra(s):
    pq = []
    heapq.heappush(pq, [0, s])
    distance[s] = 0

    while pq:
        dist, node = heapq.heappop(pq)
        if distance[node] < dist:
            continue

        for weight, next_node in graph[node]:
            next_dist = dist + weight
            if distance[next_node] > next_dist:
                heapq.heappush(pq, [next_dist, next_node])
                distance[next_node] = next_dist


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    S, E, D = map(int, sys.stdin.readline().split())
    graph[S].append([D, E])

start, end = map(int, sys.stdin.readline().split())

dijkstra(start)

print(distance[end])
