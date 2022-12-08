if __name__ == '__main__':
    N = int(input())

    for i in range(1, N + 1):
        for _ in range(N - i, 0, -1):
            print(" ", end='')

        for _ in range(i):
            print("*", end='')

        print()
