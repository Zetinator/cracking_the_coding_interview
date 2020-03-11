"""2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
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

def intersection(linked_1: LinkedList, linked_2: LinkedList)-> LinkedList.Node:
    if not linked_1.head or not linked_2.head: return
    # find length(linked_1 + linked_2)
    n = 0
    tail_1 = linked_1.head
    while tail_1.next:
        n += 1
        tail_1 = tail_1.next
    tail_2 = linked_2.head
    while tail_2.next:
        n += 1
        tail_2 = tail_2.next
    # glue 1->2 and 2->1
    tail_1.next = linked_2.head
    tail_2.next = linked_1.head
    # traverse linked_1 and linked_2 until intersection appears
    node_1, node_2 = linked_1.head, linked_2.head
    for _ in range(2*n):
        if node_1 is node_2: return node_1
        node_1 = node_1.next
        node_2 = node_2.next
    return None

# test
init = [6,1]
t_1 = LinkedList(init)
init = [2,9]
t_2 = LinkedList(init)
init = [69,117, 42]
t_3 = LinkedList(init)
# bind
t_1.tail.next = t_3.head
t_1.tail = t_3.tail
t_2.tail.next = t_3.head
t_2.tail = t_3.tail
print(f'intersection: test: {t_1} vs {t_2}, ans: {intersection(t_1, t_2).value}')
