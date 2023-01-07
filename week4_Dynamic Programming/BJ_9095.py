answer = [1, 1, 2]

for i in range(3, 12):
    answer.append(answer[i - 1] + answer[i - 2] + answer[i - 3])

T = int(input())
for _ in range(T):
    n = int(input())
    print(answer[n])
