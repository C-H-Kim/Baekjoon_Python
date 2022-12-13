import sys
sys.setrecursionlimit(10**9)


def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b

    return gcd(b, a % b)


def multiply(num_list):
    sum = 1
    for num in num_list:
        sum *= num
    return sum


int(input())
A_list = list(map(int, input().split()))

int(input())
B_list = list(map(int, input().split()))

A = multiply(A_list)
B = multiply(B_list)

print(str(gcd(A, B))[-9:])
