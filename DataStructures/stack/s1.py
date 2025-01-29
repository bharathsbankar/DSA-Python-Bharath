#deque implements linked list implicitly
from collections import deque
class Stack:
    def __init__(self,size=10):
        self.max=size
        self.stack = deque()

    def push(self, data):
        if len(self.stack)<self.max:
            self.stack.append(data)
            print(data," pushed")
        else:
            print("stack overflow")

    def pop(self):
        if len(self.stack)!=0:
            return f"{self.stack.pop()} is popped"
        else:
            return "stack underflow"

    def peek(self):
        return self.stack[-1] if self.length()!=0 else "empty stack"

    def length(self):
        return len(self.stack)


    def is_empty(self):
        return len(self.stack)==0

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':
    a=Stack(4)
    print("peek element", a.peek())
    a.push(14)
    print("peek element", a.peek())
    a.push(24)
    a.push(34)
    a.push(44)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a)