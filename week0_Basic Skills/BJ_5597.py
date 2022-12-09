student = [False] * 31
student[0] = True

for _ in range(28):
    n = int(input())
    student[n] = True

for index, flag in enumerate(student):
    if not flag:
        print(index)
