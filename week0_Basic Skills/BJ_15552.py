import sys

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
