import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.empty():
            return -1
        pop_data = self.head.data
        self.head = self.head.next

        return pop_data

    def size(self):
        count = 0
        temp_node = self.head
        while temp_node is not None:
            count += 1
            temp_node = temp_node.next

        return count

    def empty(self):
        flag = False
        if self.head is None:
            flag = True

        return flag

    def top(self):
        if self.empty():
            return -1

        return self.head.data


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
