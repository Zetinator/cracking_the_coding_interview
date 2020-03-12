"""4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).
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

class LL():
    class Node():
        def __init__(self, value):
            self.value = value
            self.next = None
    def __init__(self, init=[]):
        self.head = None
        self.tail = None
        for e in init: self.append(e)
    def __repr__(self):
        res = []
        node = self.head
        while node:
            res.append(f'({node.value})')
            node = node.next
        return '->'.join(res)
    def append(self, value):
        if not self.head:
            self.head = self.Node(value)
            self.tail = self.head
            return
        self.tail.next = self.Node(value)
        self.tail = self.tail.next

def list_of_depths(bst: BST)-> dict:
    res = {}
    def r(node, level=0):
        if not node: return
        r(node.left, level+1)
        res.setdefault(level, LL()).append(node.value)
        r(node.right, level+1)
    r(bst.root)
    return res

# test
from random import uniform 
init = [int(uniform(0,100)) for _ in range(10)]
test = BST(init)
print(f'test: \n{test}\n\nlist of depths: {list_of_depths(test)}')
