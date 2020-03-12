"""3.1 Three in One: Describe how you could use a single array to implement three stacks.
"""
class MultiStack():
    def __init__(self):
        self.single_array = [[],[],[]]

    def __repr__(self):
        return repr(self.single_array)

    def pop(self, n_stack):
        return self.single_array[n_stack].pop()

    def push(self, n_stack, value):
        self.single_array[n_stack].append(value)

    def peek(self, n_stack):
        if self.single_array[n_stack]: return self.single_array[n_stack][-1]

# test
push = [1,2,3,4,5,6,7,8,9]
multi_stack = MultiStack()
# test push
for i,e in enumerate(push):
    multi_stack.push(i%3, e)
print(f'after push: stacks: {multi_stack}')
# test pop
for i in range(3):
    multi_stack.pop(i)
print(f'after pop: stacks: {multi_stack}')
