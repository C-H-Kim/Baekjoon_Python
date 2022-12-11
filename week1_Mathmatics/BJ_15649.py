N, M = map(int, input().split())

stack = []


def permutation():
    if len(stack) == M:
        print(*stack)
        return

    for i in range(1, N + 1):
        if i not in stack:
            stack.append(i)
            permutation()
            stack.pop()


permutation()
