"""4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
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

def lca(bst: BST, value_1: int, value_2: int)-> BST.Node:
    """traverse while together, when splitted return ancestor
    """
    def traverse(node):
        if not node: return
        if value_1 < node.value and value_2 < node.value:
            return traverse(node.left)
        elif value_1 > node.value and value_2 > node.value:
            return traverse(node.right)
        else: return node
    return traverse(bst.root)

# test
from random import uniform 
init = [int(uniform(0,100)) for _ in range(10)]
init = [9,4,14,2,7,12,17,1,3,6,8,11,13,16,18,0,5,10,15,19]
test = BST(init)
value_1, value_2 = 7, 1
print(f'test: {init}\n{test}\n\nget ancestor of {value_1} and {value_2}: {lca(test, value_1, value_2).value}')
