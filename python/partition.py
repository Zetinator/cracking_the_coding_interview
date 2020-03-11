"""2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x . lf x is contained within the list, the values of x only need
to be after the elements less than x (see below) . The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
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

def partition(linked: LinkedList)-> LinkedList:
    """naive approach: O(n)
    2 linked lists:
        - lower than k
        - greater than k
    linear scan through the original list, appending in lower and greater
    then bind lower and greater and return new head
    """
    if not linked.head: return
    lower = LinkedList()
    greater = LinkedList()
    node = linked.head
    # modified merge algorithm
    while node and node.value:
        if node.value < k:
            lower.append(node.value)
        else:
            greater.append(node.value)
        node = node.next
    # bind lower -> greater
    lower.tail.next = greater.head
    return lower

# test
init = [3,5,8,5,10,2,1]
t_1 = LinkedList(init)
k = 5
print(f'partition: test: {t_1}, ans: {partition(t_1)}')
