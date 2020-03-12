"""3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""

class Queue():
    """push -> cheap, pop -> expensive (amortized)
    """
    def __init__(self, x=[]):
        self.in_stack = []
        self.out_stack = []
        for e in x:
            self.push(e)

    def __repr__(self):
        return f'in: {self.in_stack}, out: {self.out_stack}'

    def push(self, value):
        self.in_stack.append(value)

    def pop(self):
        """implement a buffer, when the buffer is empty flush in_stack -> buffer
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if self.out_stack: return self.out_stack.pop()

# test
q = Queue(range(3))
# test push
print(f'after push: stacks: {q}')
for e in range(5):
    q.push(e)
    print(f'push: {e}, queue: {q}')
    print(f'pop: {q.pop()}, queue: {q}')
