C = int(input())

for _ in range(C):
    score = list(map(int, input().split()))
    N = score.pop(0)

    average = sum(score) / N
    count = 0
    for i in score:
        if i > average:
            count += 1

    print(f"{round(count / N * 100, 3):.3f}%")
