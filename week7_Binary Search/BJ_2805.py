import sys

N, M = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(tree_list)

while start <= end:
    mid = (start + end) // 2

    take = 0
    for tree in tree_list:
        if tree > mid:
            take += (tree - mid)

    if take >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
