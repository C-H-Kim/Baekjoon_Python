def permutation():
    global stack

    if len(stack) == M:
        print(*stack)
        return

    for i in range(1, N + 1):
        if i not in stack:
            stack.append(i)
            permutation()
            stack.pop()


N, M = map(int, input().split())
stack = []

permutation()
