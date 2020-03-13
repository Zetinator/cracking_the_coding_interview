"""4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
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

from itertools import permutations
def bst_sequences(bst: BST)-> list:
    """get insertion order fron the tree
    and then compute permutations per level -> level: [2**i-1, 2**(i+1)-1]
    """
    # get the original in-order sequence from the bst
    in_order = [bst.root.value]
    def bfs(root):
        frontier = [root]
        while frontier:
            _next = []
            for node in frontier:
                if node.left: _next.append(node.left); in_order.append(node.left.value)
                if node.right: _next.append(node.right); in_order.append(node.right.value)
            frontier = _next
    bfs(bst.root)
    # spawn the permutations
    res = []
    def permutate(s, level=0, current=()):
        if not s:
            res.append(current)
            # print(f'flush: ->res: {res}')
            return
        to_permute = in_order[2**level-1:2**(level+1)-1]
        for e in permutations(to_permute, len(to_permute)):
            permutate(to_permute, level+1, current+e)
    permutate(in_order)
    return res

# test
# from random import uniform 
# init = [int(uniform(0,100)) for _ in range(10)]
init = [9,4,14,2,7,12,17]
init = (9, 14, 4, 17, 12)
init = [2,1,3]
test = BST(init)
print(f'test: {init}\n{test}\n\nget sequences: {bst_sequences(test)}')
