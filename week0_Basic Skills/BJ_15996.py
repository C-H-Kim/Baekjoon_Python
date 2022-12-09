N, A = map(int, input().split())
count = 0
num = A
while num <= N:
    count += N // num
    num *= A
print(count)
