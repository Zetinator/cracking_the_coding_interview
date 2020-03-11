"""2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
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

def loop_detection(linked: LinkedList)-> LinkedList.Node:
    """O(n), tortoise and hare
    """
    if not linked.head: return
    # set-up hare - tortoise
    step_t = lambda node: node.next if node else False
    step_h = lambda node: node.next.next if node and node.next else False
    hare = step_h(linked.head)
    tortoise = step_t(linked.head)
    # find cycle
    while step_h(hare) and step_t(tortoise):
        if hare is tortoise: break
        hare = step_h(hare)
        tortoise = step_t(tortoise)
    # find beginning of cycle
    hare = linked.head
    while step_h(hare) and step_t(tortoise):
        if hare is tortoise: return hare
        hare = step_t(hare)
        tortoise = step_t(tortoise)
    return None

# test
init = [1,2,3,4,5,6,7,8,9]
t_1 = LinkedList(init)
node = t_1.head.next
t_1.tail.next = node
print(f'loop_detection: test: {init} cycle on: {node.value}, ans: {loop_detection(t_1).value}')
