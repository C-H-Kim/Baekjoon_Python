if __name__ == '__main__':
    A, B, C = map(int, input().split())

    if A == B and B == C:
        reward = 10000 + A * 1000
    else:
        if A == B or B == C:
            reward = 1000 + B * 100
        elif C == A:
            reward = 1000 + A * 100
        else:
            reward = max(A, B, C) * 100

    print(reward)
