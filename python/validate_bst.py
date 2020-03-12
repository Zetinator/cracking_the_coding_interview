"""4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
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

def validate_bst(bst: BST)-> bool:
    """using the old trick of keeping track of the valid intervals
    """
    def traverse(node, left=-float('inf'), right=float('inf')):
        if not node: return True
        l = traverse(node.left, left, node.value)
        r = traverse(node.right, node.value, right)
        return left < node.value < right and l and r
    return traverse(bst.root)

# test
from random import uniform 
# init = [int(uniform(0,100)) for _ in range(10)]
init = [49, 16, 35, 24, 76, 69, 57, 75, 62, 70]
test = BST(init)
# changing the value of a node to currupt the tree
test.root.left.right.value = 50
print(f'test: {init}\n{test}\n\ncheck if balanced: {validate_bst(test)}')

