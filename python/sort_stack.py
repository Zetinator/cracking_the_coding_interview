"""3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
"""
class Stack():
    def __init__(self, x=[]):
        self.core = []
        for e in x:
            self.push(e)
    def __repr__(self):
        return repr(self.core)
    def __len__(self):
        return len(self.core)
    def push(self, value):
        self.core.append(value)
    def peek(self):
        if self.core: return self.core[-1]
    def pop(self):
        if self.core: return self.core.pop()

def sort_stack(stack: Stack):
    """with just one additional stack we aspire to O(n^2), selection sort
    """
    # additional stack
    tmp = Stack()
    # find length
    n = 0
    while stack:
        tmp.push(stack.pop())
        n += 1
    while tmp:
        stack.push(tmp.pop())
    # balance the content between the 2 stacks, sorting one at the time
    mini = float('inf')
    for i in range(n):
        print(f'<- status: stack: {stack}, tmp: {tmp}')
        for _ in range(n-i):
            mini = min(mini, stack.peek())
            tmp.push(stack.pop())
        print(f'-> status: stack: {stack}, tmp: {tmp}')
        # push the min
        stack.push(mini)
        for _ in range(n-i):
            if tmp.peek() != mini: stack.push(tmp.pop())
            else: tmp.pop()
        # reset minimum
        mini = float('inf')
    return stack

# test
init = [8,5,4,6,7,9,2]
test = Stack(init)
print(f'test: {test}, ans: {sort_stack(test)}')
