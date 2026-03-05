import ctypes

class Queue:

    def __init__(self, maxlen: int):
        
        if maxlen <= 0:
            raise ValueError("Capacity must be > 0")
        self.maxlen = maxlen
        self.size = 0
        self.last = 0   # index of current insert position
        self.first = 0  # index of current first elem
        self.__array = (ctypes.py_object * self.maxlen)()
        for i in range(self.maxlen):
            self.__array[i] = None



    def is_empty(self) -> bool:
        return self.size == 0

    def front(self) -> object:
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self.__array[self.first]
    
    def is_full(self) -> bool:
        return self.size == self.maxlen
    

    def enqueue(self, item: object) -> None:
        if self.is_full():
            raise IndexError("Queue is full")
        
        self.__array[self.last] = item
        self.last = (self.last + 1) % self.maxlen
        self.size += 1


    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        
        value = self.__array[self.first]
        self.__array[self.first] = None
        self.first = (self.first + 1) % self.maxlen
        self.size -= 1
        return value

    def __str__(self):
        """O(n)"""
        items = []
        idx = self.first
        for _ in range(self.size):
            items.append(self.__array[idx])
            idx = (idx + 1) % self.maxlen
        return "[" + ", ".join(str(x) for x in items) + "]"


a = Queue(4)

print(a)

a.enqueue(2)
print(a)
a.enqueue(3)
a.enqueue(6)
a.enqueue(10)
print(a)
a.dequeue()
print(a)
a.enqueue(20)
print(a)
a.dequeue()
print(a)
a.enqueue(100)
print(a)