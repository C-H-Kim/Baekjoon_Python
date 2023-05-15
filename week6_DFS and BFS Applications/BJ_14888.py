import sys
sys.setrecursionlimit(10 ** 6)


def dfs(depth, result, add, sub, mul, div):
    global max_result, min_result
    if depth == N:
        max_result = max(result, max_result)
        min_result = min(result, min_result)

        return

    if add != 0:
        dfs(depth + 1, result + operand[depth], add - 1, sub, mul, div)
    if sub != 0:
        dfs(depth + 1, result - operand[depth], add, sub - 1, mul, div)
    if mul != 0:
        dfs(depth + 1, result * operand[depth], add, sub, mul - 1, div)
    if div != 0:
        dfs(depth + 1, int(result / operand[depth]), add, sub, mul, div - 1)


N = int(sys.stdin.readline())
operand = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

max_result = -1e9
min_result = 1e9

dfs(1, operand[0], operator[0], operator[1], operator[2], operator[3])

print(max_result)
print(min_result)
