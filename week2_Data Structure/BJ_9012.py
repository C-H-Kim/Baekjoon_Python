import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            return -1

    def empty(self):
        return not self.items

    def top(self):
        return self.items[-1]


T = int(input())

for _ in range(T):
    S = sys.stdin.readline()
    stack = Stack()

    flag = True
    for s in S:
        if s == '(':
            stack.push('(')
        elif s == ')':
            if stack.pop() == -1:
                flag = False
                break
        else:
            pass

    if flag and stack.empty():
        print("YES")
    else:
        print("NO")
