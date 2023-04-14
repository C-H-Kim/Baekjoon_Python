import sys

K, N = map(int, sys.stdin.readline().split())

lan_list = []
for _ in range(K):
    lan_list.append(int(sys.stdin.readline()))

start = 1
end = max(lan_list)

while start <= end:
    mid = (start + end) // 2

    count = 0
    for lan in lan_list:
        count += lan // mid

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
