"""4.11 Random Node: You are implementing a binary search tree class from scratch, which, in addition
to insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for get Ra ndomNode, and explain how you would implement the rest of the methods.
"""
class BST():
    class Node():
        def __init__(self, value):
            self.value = value
            self.weight = 1
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
            res.append(f'\t'*level + f'({node.value})w{node.weight}')
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
            # upadte weight
            w = lambda node: node.weight if node else 0
            node.weight = w(node.left) + w(node.right) + 1
        r(self.root, value)

from random import uniform
from math import ceil
def get_random_node(bst: BST)-> BST.Node:
    def choose(node):
        if not node: return
        # generate int number between [0, node.weight]
        w = lambda node: node.weight if node else 0
        n = ceil(uniform(0, w(node)))
        # distribute the number in 3 according to the weight
        if n == w(node): return node
        if n <= w(node.left): return choose(node.left)
        else: return choose(node.right)
    return choose(bst.root)

# test
# from random import uniform 
init = [int(uniform(0,100)) for _ in range(10)]
# init = [9,4,14,2,7,12,17]
test = BST(init)
target = test.root.left
# init = [2,1,3]
# target = BST(init)
# target = target.root
print(f'test: {init}\n{test}\n\nget random node: {get_random_node(test).value}')
