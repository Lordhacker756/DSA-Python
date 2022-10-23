from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def reverse_string(self, val):
        for ch in val:
            self.push(ch)

        for i in range(len(val)):
            print(self.container.pop(), end='')


s = Stack()
sent = "We will conquere COVID-19"
s.reverse_string(sent)
