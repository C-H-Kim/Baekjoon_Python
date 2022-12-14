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

    def size(self):
        return len(self.items)

    def empty(self):
        return not self.items

    def top(self):
        if not self.empty():
            return self.items[-1]
        else:
            return -1


stack = Stack()
N = int(input())

for _ in range(N):
    opt_list = list(map(str, sys.stdin.readline().split()))
    opt = opt_list[0]

    if opt == 'push':
        val = opt_list[1]
        stack.push(val)
    elif opt == 'pop':
        print(stack.pop())
    elif opt == 'size':
        print(stack.size())
    elif opt == 'empty':
        if stack.empty():
            print(1)
        else:
            print(0)
    elif opt == 'top':
        print(stack.top())
    else:
        pass
