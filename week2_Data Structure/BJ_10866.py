import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_front(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node
        self.length += 1

    def push_back(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node
        self.length += 1

    def pop_front(self):
        if self.length == 0:
            print(-1)
        else:
            pop_data = self.head.data
            self.head = self.head.next

            self.length -= 1
            print(pop_data)

    def pop_back(self):
        if self.length == 0:
            print(-1)
        else:
            pop_data = self.tail.data
            self.tail = self.tail.prev

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

    def print(self):
        if self.length == 0:
            print('empty Deque')
            return
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next


N = int(input())
dq = Deque()

for _ in range(N):
    opt_list = list(map(str, sys.stdin.readline().split()))
    opt = opt_list[0]

    if opt == 'push_front':
        dq.push_front(opt_list[1])
    elif opt == 'push_back':
        dq.push_back(opt_list[1])
    elif opt == 'pop_front':
        dq.pop_front()
    elif opt == 'pop_back':
        dq.pop_back()
    elif opt == 'size':
        dq.size()
    elif opt == 'empty':
        dq.empty()
    elif opt == 'front':
        dq.front()
    else:
        dq.back()
