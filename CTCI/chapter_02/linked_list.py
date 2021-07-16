"""
LinkedList and LinkedListNode classes.
"""

import random

class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)
 
 
# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)
    def add_multiple(self, values):
        for v in values:
            self.add(v)
    def add(self, value):
        if self.head is None:
            # add to head
            self.head = LinkedListNode(value)
            self.tail = self.head
        else:
            # add to tail
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail
    def __len__(self):
        i = 0
        node = self.head
        while node != None:
            i += 1
            node = node.next
        return i

    def __str__(self):
        values = [str(x) for x in self.values()]
        return " -> ".join(values)

    def values(self):
        node = self.head
        values = []
        while node != None:
            values.append(node.value)
            node = node.next
        return values

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    @classmethod
    def generate(cls, k, min_value, max_value):
        return cls(random.choices(range(min_value, max_value), k=k))