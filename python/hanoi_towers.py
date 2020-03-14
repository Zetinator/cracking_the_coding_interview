"""8.6 Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (Le., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using Stacks.
"""
def hanoi(disks: int)-> int:
    """the classics, recursive solution
    https://www.youtube.com/watch?v=8lhxIOAfDss
    """
    class Tower():
        def __init__(self, t=[], name='kim'): self.tower=t; self.name=name
    # set 3 towers
    t_1 = Tower([e for e in reversed(range(disks))], 'A')
    t_2 = Tower([], 'B')
    t_3 = Tower([], 'C')
    def move(main, tmp, target):
        print(f'move next disk: {main.tower[-1]} from: {main.name} -> {target.name}')
        target.tower.append(main.tower.pop())
        print(f'status: {main.name}:{main.tower}, {tmp.name}:{tmp.tower}, {target.name}:{target.tower}')
    def r(n, main, tmp, target):
        if n == 0: return
        r(n-1, main, target, tmp)
        move(main, tmp, target)
        r(n-1, tmp, main, target)
    return r(disks, t_1, t_2, t_3)

# test
test = 4
print(f'solve hanoi with {test} disks, set of movements:')
hanoi(test)
