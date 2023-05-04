import sys
sys.setrecursionlimit(10 ** 5)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col, depth):
    global max_depth
    visited_alpha[board[row][col]] = True
    max_depth = max(max_depth, depth)

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if (0 <= nr < R) and (0 <= nc < C):
            if not visited_alpha[board[nr][nc]]:
                dfs(nr, nc, depth + 1)
                visited_alpha[board[nr][nc]] = False


R, C = map(int, sys.stdin.readline().split())
board = [list(map(lambda a: ord(a) - 65, sys.stdin.readline().rstrip())) for _ in range(R)]
visited_alpha = [False] * 26

max_depth = 0

dfs(0, 0, 1)

print(max_depth)

# set과 in 연산자를 이용한 방법
# def dfs(row, col, depth):
#     global max_depth
#     visited_alpha.add(board[row][col])
#     max_depth = max(max_depth, depth)
#
#     for i in range(4):
#         nr = row + dr[i]
#         nc = col + dc[i]
#
#         if (0 <= nr < R) and (0 <= nc < C):
#             if board[nr][nc] not in visited_alpha:
#                 dfs(nr, nc, depth + 1)
#                 visited_alpha.remove(board[nr][nc])
#
#
# R, C = map(int, sys.stdin.readline().split())
# board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
#
# visited_alpha = set()

# ord()와 dictionary를 이용한 방법
# def dfs(row, col, depth):
#     global max_depth
#     visited_alpha[ord(board[row][col])] = True
#     max_depth = max(max_depth, depth)
#
#     for i in range(4):
#         nr = row + dr[i]
#         nc = col + dc[i]
#
#         if (0 <= nr < R) and (0 <= nc < C):
#             if not visited_alpha[ord(board[nr][nc])]:
#                 dfs(nr, nc, depth + 1)
#                 visited_alpha[ord(board[nr][nc])] = False
#
#
# R, C = map(int, sys.stdin.readline().split())
# board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
#
# visited_alpha = dict()
# for line in board:
#     for char in line:
#         if ord(char) not in visited_alpha:
#             visited_alpha[ord(char)] = False
