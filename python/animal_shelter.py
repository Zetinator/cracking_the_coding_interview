"""3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked List data structure.
"""
class Queue():
    class Node():
        def __init__(self, x):
            self.value = x
            self.next = None
    def __init__(self, x=[]):
        self.head = None
        self.tail = None
        for e in x:
            self.enqueue(e)
    def __len__(self):
        return 0 if not self.head else 1
    def __repr__(self):
        res, node = [], self.head
        while node:
            res.append(str(node.value))
            node = node.next
        return '->'.join(res)
    def enqueue(self, value):
        if not self.head:
            self.head = self.Node(value)
            self.tail = self.head
            return
        self.tail.next = self.Node(value)
        self.tail = self.tail.next
    def peek(self):
        if not self.head: return None
        return self.head.value
    def dequeue(self):
        if not self.head: return None
        tmp = self.head
        self.head = self.head.next
        return tmp.value

class AnimalShelter():
    def __init__(self, init=[]):
        self.dogs = Queue()
        self.cats = Queue()
        self.all = Queue()
        self.history = Queue()
        for node in init:
            self.enqueue(node)
    def __repr__(self):
        return f'all: {self.all}\n dogs: {self.dogs}\n cats: {self.cats}'
    def enqueue(self, node):
        race, name = node
        self.all.enqueue(node)
        if race == 'dog': self.dogs.enqueue(node)
        else: self.cats.enqueue(node)
    def dequeue_any(self):
        if not self.all: return
        # lazy propagation, after dequeueing from cats and dogs
        while self.history and self.all.peek() == self.history.peek():
            self.history.dequeue()
            self.all.dequeue()
        # actual dequeue any
        node = self.all.dequeue()
        race, name = node
        if race == 'dog':
            self.dogs.dequeue()
        else: self.cats.dequeue()
        return node
    def dequeue_dog(self):
        node = self.dogs.dequeue()
        self.history.enqueue(node)
        return node
    def dequeue_cat(self):
        node = self.cats.dequeue()
        self.history.enqueue(node)
        return node
# test
import random
race = ('dog', 'cat')
shelter = AnimalShelter()
for i in range(5):
    node = (random.choice(race), f'{i:04}')
    shelter.enqueue(node)
print(f'shelter: {shelter}')
