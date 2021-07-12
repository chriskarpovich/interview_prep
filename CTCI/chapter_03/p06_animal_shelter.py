"""
Animal shelter with dogs and cats, first in first out (FIFO) basis. People must adopt either the oldest (based on arrival time) of the
dogs and cats in the shelter, and select whether they prefer a dog or a cat and receive the oldest animal of that type.
They cannot select which specific animal they would like. Create the data structures to maintain this system and implement 
operations such as enqueue, dequeueAny, dequeueDog, dequeueCat.
"""
import sys, os
sys.path.append('..')
from chapter_02.linked_list import LinkedList, LinkedListNode
import time

class Animal:
    def __init__(self, name):
        self.time_admitted = time.time()
        self.name = name

class Cat(Animal):
    pass


class Dog(Animal):
    pass

class AnimalShelter(LinkedList):
    def __init__(self, animals=None):
        super().__init__(values=animals)

    def enqueue(self, animal):
        super().add(value=animal)

    def dequeueAny(self):
        # dequeue by head (FIFO)
        node = self.head
        # check if head is none
        if node == None:
            return None
        self.head = self.head.next
        # check if head now is none and change tail
        if self.head == None:
            self.tail = None
        return node.value
        
    def dequeueDog(self):
        node = self.head
        if node == None:
            return None
        prev = None
        while node != None:
            if isinstance(node.value, Dog):
                # dequeue dog
                if self.head == node:
                    self.head = node.next
                else:
                    prev.next = node.next
                return node.value
            prev = node
            node = node.next
        return None
    def dequeueCat(self):
        node = self.head
        if node == None:
            return None
        prev = None
        while node != None:
            if isinstance(node.value, Cat):
                # dequeue cat
                if self.head == node:
                    self.head = node.next
                else:
                    prev.next = node.next
                return node.value
            prev = node
            node = node.next
        return None
        
    

def test_enqueue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("Fluffy"))
    animal_shelter.enqueue(Dog("Sparky"))
    animal_shelter.enqueue(Cat("Sneezy"))
    assert len(animal_shelter) == 3
    print(animal_shelter.dequeueCat().name)
    print(animal_shelter.dequeueDog().name)
    print(animal_shelter.dequeueCat().name)
if __name__ == "__main__":
    test_enqueue()
    