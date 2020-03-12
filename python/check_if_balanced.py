"""4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
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

def check_if_balaced(bst: BST)-> bool:
    """using the old trick of keeping track of the valid intervals
    """
    def traverse(node):
        if not node: return (0, True)
        l_height, l_balance = traverse(node.left)
        r_height, r_balance = traverse(node.right)
        height = max(r_height, l_height) + 1
        balance = abs(r_height - l_height) <= 1 and l_balance and r_balance
        return (height, balance)
    total_height, total_balance = traverse(bst.root)
    return total_balance

# test
from random import uniform 
init = [int(uniform(0,100)) for _ in range(10)]
init = [9,4,14,2,7,12,17,1,3,6,8,11,13,16,18,0,5,10,15,19]
test = BST(init)
print(f'test: {init}\n{test}\n\ncheck if balanced: {check_if_balaced(test)}')
