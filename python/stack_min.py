"""3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""
class StackMin():
    """no heap?
    prepare to have O(n) refresh when popping the current min
    """
    def __init__(self, x=[]):
        self.core = []
        self.min = float('inf')
        for e in x:
            self.push(e)

    def __repr__(self):
        return repr(self.core)

    def push(self, value):
        self.min = min(self.min, value)
        self.core.append(value)

    def peek(self):
        if self.core: return self.core[-1]

    def pop(self):
        """if min is popped search linear for the new one, amortized
        """
        if not self.core: return
        tmp = self.core.pop()
        if tmp == self.min: 
            self.min = min(self.core)
        return tmp

# test
push = [8,5,3,4,6,1,7]
stack_min = StackMin(push)
print(f'pushinng: {push}, stack: {stack_min}, min: {stack_min.min}')
stack_min.pop();
stack_min.pop();
print(f'popping min: stack:{stack_min.min}')
