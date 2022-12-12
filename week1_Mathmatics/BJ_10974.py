def permutation():
    if len(stack) == N:
        print(*stack)
        return

    for i in range(1, N + 1):
        if i not in stack:
            stack.append(i)
            permutation()
            stack.pop()


N = int(input())
stack = []

permutation()
