"""4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
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

def successor(bst: BST, target: int)-> BST.Node:
    """standard binary search, but keeping trak of the next greatest
    if the found node has right children go find the min in that sub-tree
    """
    def find(node, target, parent=None):
        if not node or node.value == target: return (node, parent)
        if target < node.value: return find(node.left, target, node)
        else: return find(node.right, target, parent)
    node, parent = find(bst.root, target)
    # return next greatest
    if not node or not node.right: return parent.value if parent else None
    # go get the min of the right subtree
    node = node.right
    while node.left: node = node.left
    return node.value

# test
from random import uniform 
init = [int(uniform(0,100)) for _ in range(10)]
init = [9,4,14,2,7,12,17,1,3,6,8,11,13,16,18,0,5,10,15,19]
test = BST(init)
target = 19
print(f'test: {init}\n{test}\n\nget successor of {target}: {successor(test, target)}')
