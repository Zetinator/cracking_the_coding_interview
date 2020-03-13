"""4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative) . Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
"""
class BST():
    class Node():
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    def __init__(self, init=[]):
        self.root = None
        for e in init:
            self.insert(e)
    def __repr__(self):
        res = []
        def traverse(node, level=0):
            if not node: return
            traverse(node.right, level+1)
            res.append(f'\t'*level + f'({node.value})')
            traverse(node.left, level+1)
        traverse(self.root)
        return '\n'.join(res)
    def insert(self, value):
        if not self.root: self.root = self.Node(value); return
        def r(node, value):
            if not node: return
            if value == node.value: return
            if value < node.value:
                if node.left: r(node.left, value)
                else: node.left = self.Node(value)
            else:
                if node.right: r(node.right, value)
                else: node.right = self.Node(value)
        r(self.root, value)

def path_with_sum(bst: BST)-> int:
    """well traverse the tree keeping track of the current sum
    and we ask for the remainder... same trick as find the sum in the array #Google
    """
    tracker = set()
    path_with_sum.res = 0
    def traverse(node, current_sum=0):
        if not node: return
        # keep track of the current_sum while we explore
        current_sum += node.value
        tracker.add(current_sum)
        # ask for the remainder
        remainder = current_sum - target
        if remainder in tracker: path_with_sum.res += 1
        # propagate dfs
        traverse(node.left, current_sum)
        traverse(node.right, current_sum)
        # delete path from tracker as we backtrack
        tracker.remove(current_sum)
    traverse(bst.root)
    return path_with_sum.res

# test
# from random import uniform 
# init = [int(uniform(0,100)) for _ in range(10)]
test = BST()
test.root = BST.Node(10)
test.root.left = BST.Node(5)
test.root.left.left = BST.Node(3)
test.root.left.right = BST.Node(1)
test.root.left.right.right = BST.Node(2)
test.root.left.left.left = BST.Node(3)
test.root.left.left.right = BST.Node(-2)
test.root.right = BST.Node(-3)
test.root.right.right = BST.Node(11)
target = 8
print(f'test: \n{test} \n\nnumber of paths with sum {target}: {path_with_sum(test)}')
