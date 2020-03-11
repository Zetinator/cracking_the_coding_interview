"""2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
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

def return_k(linked: LinkedList, k: int)-> LinkedList:
    """naive approach O(n)
    linear scan to know the number of elements
    and then another linear scan to return n - k
    """
    if not linked.head: return None
    # find lenght, linear scan
    node = linked.head
    counter = 0
    while node:
        counter += 1
        node = node.next
    # return head at counter - k
    node = linked.head
    while node and counter - k > 0:
        node = node.next
        counter -= 1
    tmp = LinkedList()
    tmp.head = node
    return tmp

# test
init = [3,2,3,3,4,5,6,6,7,8,9]
init = [1,1,1,1,1,2,3,4,5,1,1,1,1,6,6,6,7,8,9,10,10,10,10]
t_1 = LinkedList(init)
k = 5
print(f'return_k: test: {t_1}, ans: {return_k(t_1, k)}')
