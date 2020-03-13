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
    """
    # set 3 towers
    t_1, t_2, t_3 = [e for e in reversed(range(disks))], [], []
    def move_next(main, tmp, target):
        if not main: return
        print(f'----------------------------------------------------MOVE')
        print(f'status: main:{main}, tmp:{tmp}, target:{target}')
        print(f'move next disk: {main[-1]} from: main -> target')
        target.append(main.pop())
        print(f'status: main:{main}, tmp:{tmp}, target:{target}')
        # call spread
        spread_left(tmp, main, target)
        return
    def spread_right(main, tmp, target):
        if not main: return
        print(f'--------------------------------------------------SPREAD(right)')
        print(f'status: main:{main}, tmp:{tmp}, target:{target}')
        print(f'move: {main[-1]} from: main -> tmp')
        tmp.append(main.pop())
        print(f'status: main:{main}, tmp:{tmp}, target:{target}')
        print(f'move: {main[-1]} from: main -> target')
        target.append(main.pop())
        print(f'status: main:{main}, tmp:{tmp}, target:{target}')
        print(f'move: {tmp[-1]} from: tmp -> target')
        target.append(tmp.pop())
        print(f'status: main:{main}, tmp:{tmp}, target:{target}')
        # call next move
        move_next(main, target, tmp)
        return
    def spread_left(main, tmp, target):
        if not main: return
        print(f'--------------------------------------------------SPREAD(left)')
        print(f'status: main:{main}, tmp:{tmp}, target:{target}')
        print(f'move: {main[-1]} from: main -> tmp')
        tmp.append(main.pop())
        print(f'status: main:{main}, tmp:{tmp}, target:{target}')
        print(f'move: {main[-1]} from: main -> target')
        target.append(main.pop())
        print(f'status: main:{main}, tmp:{tmp}, target:{target}')
        print(f'move: {tmp[-1]} from: tmp -> target')
        target.append(tmp.pop())
        print(f'status: main:{main}, tmp:{tmp}, target:{target}')
        # call next move
        move_next(tmp, target, main)
        return
    return spread_right(t_1, t_2, t_3)

# test
test = 4
print(f'solve hanoi with {test} disks, set of movements:')
hanoi(test)
