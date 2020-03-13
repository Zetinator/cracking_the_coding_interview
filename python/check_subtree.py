"""4.10 Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorith m to determine if T2 is a subtree of Tl .
A tree T2 is a subtree ofTi if there exists a node n in Ti such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
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

def check_subtree(bst: BST, target: BST)-> bool:
    def find_node(node, target):
        """standard binary search tree, search
        """
        if not node: return
        if node.value == target.value: return node
        if target.value < node.value: return find_node(node.left, target)
        else: return find_node(node.right, target)
    node = find_node(bst.root, target)
    if not node: return False
    def traverse(n1, n2):
        if not n1 and not n2: return True
        if not n1 or not n2 or n1.value != n2.value: return False
        return traverse(n1.left, n2.left) or traverse(n1.right, n2.right)
    return traverse(node, target)

# test
# from random import uniform 
# init = [int(uniform(0,100)) for _ in range(10)]
init = [9,4,14,2,7,12,17]
test = BST(init)
target = test.root.left
# init = [2,1,3]
# target = BST(init)
# target = target.root
print(f'test: {init}\n{test}\n\nis subtree?: {check_subtree(test, target)}')
