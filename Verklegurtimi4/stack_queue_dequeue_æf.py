
class Stack:
    
    def __init__(self) -> None:

        self.data = []
    
        
    def is_empty(self) -> bool:
        return len(self.data) == 0

    def top(self) -> object:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[-1]

    def pop(self) -> None:
        if self.is_empty():
            raise IndexError("Stack is empty")
        self.data.pop()


    def push(self, item: object) -> None:
        self.data.append(item)





class Queue:

    def __init__(self, capacity):

        self.data = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    def is_full(self)-> bool:
        return self.size == self.capacity
    
    def is_empty(self) -> bool:
        return self.size == 0

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[self.head]
    
    def enqueue(self, item: object):
        if self.is_full():
            raise IndexError("Queue is full")
        
        self.data[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        front_value = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return front_value
    



    class Dequeue:

        def __init__(self, capacity):

            self.capacity = capacity
            self.data = [None] * capacity
            self.tail = 0
            self.head = 0
            self.size = 0


        def append(self, item: object):
            if self.size != self.capacity:

                self.data[self.tail] = item
                self.tail = (self.tail + 1) % self.capacity
                self.size += 1
                
            else:
                self.data[self.head] = None
                self.data[self.tail] = item
                self.tail = (self.tail + 1) % self.capacity
        
        def appendleft(self, item: object):
            if self.size != self.capacity:

                self.data

        # óklárað