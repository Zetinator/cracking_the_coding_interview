"""2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
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

def partition(linked_1: LinkedList, linked_2: LinkedList)-> LinkedList:
    """naive approach: O(n)
   linear scan -> stack and then read the number from the stack
   make the sum and instert the result in a list
   """
    if not linked_1.head or not linked_2.head: return
    # read first number
    stack = []
    node = linked_1.head 
    while node:
        stack.append(str(node.value))
        node = node.next
    n1 = int(''.join(stack))
    # read second number
    stack = []
    node = linked_2.head 
    while node:
        stack.append(str(node.value))
        node = node.next
    n2 = int(''.join(stack))
    # sum both numbers
    n1 += n2
    res = reversed(list(str(n1)))
    # return dummie LinkedList class
    tmp = LinkedList(res)
    return tmp

# test
init = [6,1,7]
t_1 = LinkedList(init)
init = [2,9,5]
t_2 = LinkedList(init)
print(f'partition: test: {t_1} + {t_2}, ans: {partition(t_1, t_2)}')
