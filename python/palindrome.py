"""2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
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

def palindrome(linked: LinkedList)-> bool:
    """naive approach: O(n)
   linear scan to find the lenght, then the middle
   push from middle to end in a stack and then
   compare from start to middle against the pops of the stack
   """
    if not linked.head: return
    # find lenght
    node = linked.head 
    counter = 0
    while node:
        counter += 1
        node = node.next
    # find middle
    middle = counter//2
    if counter%2 != 0: middle += 1
    # push into the stack
    node = linked.head
    counter = 1
    stack = []
    while node:
        if counter > middle:
            stack.append(node.value)
        node = node.next
        counter += 1
    # linear scan of the list against the stack
    node = linked.head
    while stack:
        if node.value != stack.pop(): return False
        node = node.next
    return True

# test
init = [7,6,1,1,6,7]
init = [7,6,1,3,1,6,7]
t_1 = LinkedList(init)
print(f'palindrome: test: {t_1}, ans: {palindrome(t_1)}')
