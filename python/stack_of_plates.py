"""3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.
"""
class SetOfStacks():
    def __init__(self, max_stack_size: int, x=[]):
        self.core = []
        self.max = max_stack_size
        for e in x:
            self.push(e)

    def __repr__(self):
        return repr(self.core)

    def pop_at(self, index: int):
        if not self.core: return
        if not index < len(self.core): return
        if not self.core[index]: return
        return self.core[index].pop()

    def pop(self):
        if not self.core: return
        while self.core and not self.core[-1]: self.core.pop()
        if self.core: return self.core[-1].pop()

    def push(self, value):
        if not self.core: self.core = [[value]]; return
        if len(self.core[-1]) == self.max: self.core.append([value])
        else: self.core[-1].append(value)

    def peek(self):
        if self.core[n_stack]: return self.core[n_stack][-1]

# test
multi_stack = SetOfStacks(5, range(24))
# test push
print(f'after push: stacks: {multi_stack}')
# test pop_at
for _ in range(6):
    print(f'after pop_at(2): {multi_stack.pop_at(2)}, stack: {multi_stack}')
# test pop
for i in range(20):
    multi_stack.pop()
    print(f'after pop: stacks: {multi_stack}')
