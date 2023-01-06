padovan = [0, 1, 1]

for i in range(3, 101):
    padovan.append(padovan[i - 2] + padovan[i - 3])

T = int(input())

for _ in range(T):
    print(padovan[int(input())])
