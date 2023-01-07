tile = [0, 1, 2]

for i in range(3, 1001):
    tile.append(tile[i - 1] + tile[i - 2])

n = int(input())
print(tile[n] % 10007)
