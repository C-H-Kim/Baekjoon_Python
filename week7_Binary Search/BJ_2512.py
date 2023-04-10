import sys

N = int(sys.stdin.readline())
request_budget = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start = 0
end = max(request_budget)

if sum(request_budget) <= M:
    print(max(request_budget))
else:
    while start <= end:
        mid = (start + end) // 2

        final_budget = 0
        for each_budget in request_budget:
            final_budget += min(mid, each_budget)

        if final_budget > M:
            end = mid - 1
        else:
            start = mid + 1
    print(end)
