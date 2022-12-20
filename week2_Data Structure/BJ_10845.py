import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            print(-1)
        else:
            pop_data = self.head.data
            self.head = self.head.next
            self.length -= 1
            print(pop_data)

    def size(self):
        print(self.length)

    def empty(self):
        if self.length == 0:
            print(1)
            return
        print(0)

    def front(self):
        if self.length == 0:
            print(-1)
            return
        print(self.head.data)

    def back(self):
        if self.length == 0:
            print(-1)
            return
        print(self.tail.data)


N = int(input())
queue = Queue()

for _ in range(N):
    opt_list = list(map(str, sys.stdin.readline().split()))
    opt = opt_list[0]

    if opt == 'push':
        queue.push(opt_list[1])
    elif opt == 'pop':
        queue.pop()
    elif opt == 'size':
        queue.size()
    elif opt == 'empty':
        queue.empty()
    elif opt == 'front':
        queue.front()
    else:
        queue.back()
