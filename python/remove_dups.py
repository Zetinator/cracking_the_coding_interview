"""2.1 Remove Dups: Write code to remove duplicates from an unsorted li nked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
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

def remove_dups(linked: LinkedList)-> LinkedList:
    """naive buffer solution
    """
    if not linked.head or not linked.head.next: return
    _buffer = set()
    node = linked.head
    while node and node.next:
        _buffer.add(node.value)
        while node and node.next and node.next.value in _buffer:
            node.next = node.next.next
        node = node.next
    return linked

def remove_dups(linked: LinkedList)-> LinkedList:
    """no buffer? no problem, linear scan until the end, per element
    """
    if not linked.head or not linked.head.next: return
    node = linked.head
    while node:
        sentinel = node
        while sentinel and sentinel.next:
            if sentinel.next.value == node.value:
                sentinel.next = sentinel.next.next
            else:
                sentinel = sentinel.next
        node = node.next
    return linked

# test
init = [3,2,3,3,4,5,6,6,7,8,9]
init = [1,1,1,1,1,2,3,4,5,1,1,1,1,6,6,6,7,8,9,10,10,10,10]
t_1 = LinkedList(init)
print(f'remove_dups: test: {t_1}, ans: {remove_dups(t_1)}')
