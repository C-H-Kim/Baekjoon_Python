def dfs(start):
    if len(stack) == M:
        print(*stack)
        return

    for i in range(start, N + 1):
        stack.append(i)
        dfs(i + 1)
        stack.pop()


N, M = map(int, input().split())
stack = []
dfs(1)
