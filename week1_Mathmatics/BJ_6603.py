def combination(start):
    global stack

    if len(stack) == 6:
        print(*stack)
        return

    for i in range(start, k):
        stack.append(num_list[i])
        combination(i + 1)
        stack.pop()


while True:
    num_list = list(map(int, input().split()))
    k = num_list.pop(0)

    if k == 0:
        break

    stack = []
    combination(0)
    print()
