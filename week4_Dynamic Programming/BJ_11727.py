tile = [1, 1, 3]

for i in range(3, 1001):
    tile.append(tile[i - 1] + tile[i - 2] * 2)

n = int(input())
print(tile[n] % 10007)
