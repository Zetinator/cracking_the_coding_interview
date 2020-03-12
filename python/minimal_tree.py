"""4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algo-
rithm to create a binary search tree with minimal height.
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

def minimal_tree(array: list):
    """the array is sorted just use binary search, to create the tree recursively
    """
    bst = BST()
    def build(l, r):
        if l == r: bst.insert(array[l]); return
        m = (l+r)//2
        # insert into the tree
        bst.insert(array[m])
        # build recursively
        build(l, m)
        build(m+1, r)
    build(0, len(array)-1)
    return bst

# test
# from random import uniform
# bst = BST([int(uniform(0,100)) for _ in range(20)])
# print(f'bst: \n{bst}')
test = [e for e in range(20)]
print(f'test: {test}, minimal_tree: \n{minimal_tree(test)}')
