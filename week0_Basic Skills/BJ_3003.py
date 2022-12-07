if __name__ == '__main__':
    chess_origin = [1, 1, 2, 2, 2, 8]
    chess_input = list(map(int, input().split()))

    for i in range(6):
        print(chess_origin[i] - chess_input[i], end=" ")
