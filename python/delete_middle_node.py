"""2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
"""
class LinkedList():
    class Node():
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self, x=[]):
        self.head = None
        self.tail = None
        for e in x:
            self.append(e)

    def __repr__(self):
        node = self.head
        res = []
        while node:
            res.append(f'({node.value})')
            node = node.next
        return '->'.join(res)

    def append(self, x):
        if not self.head:
            self.head = self.Node(x)
            self.tail = self.head
            return
        self.tail.next = self.Node(x)
        self.tail = self.tail.next

def delete_middle(middle: LinkedList.Node)-> None:
    """naive approach: O(n)
    in python no pointer manipulation means copy from middle -> end, and delete end
    """
    if not middle: return None
    node = middle
    while node and node.next and node.next.next:
        node.value = node.next.value
        node = node.next
    node.next = None

# test
init = [1,2,3,4,5,6,7,8,9]
t_1 = LinkedList(init)
# given the 4th node in the list
node = t_1.head.next.next.next
print(f'delete_middle: test: {t_1}, ans: {delete_middle(node)}{t_1}')
