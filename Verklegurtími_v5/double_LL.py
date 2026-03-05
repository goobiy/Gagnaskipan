
class Node:

    def __init__(self, data= None, next= None, previous= None):
        self.next = next
        self.previous = previous
        self.data = data


class DLL_Deque:

    def __init__(self):
        self.head = Node()
        self.tail= Node()
        self.head.next = self.tail
        self.tail.previous = self.head
        self.current = self.tail
        self.size = 0

    def _move_to_previous(self):    # insert implem
        if self.current != self.head:
            self.current = self.current.previous
    
    def move_to_next(self): # insert implem
        if self.current != self.tail:
            self.current= self.current.next

    def move_to_pos(self, pos): # insert implem
        if pos > self.size or pos < 0:
            return
        self.current = self.head.next
        for _ in range(pos):
            self.current = self.current.next

    def add_front(self, value):
        new_node = Node(value, next= self.tail, previous= self.head.previous)

        if self.head.data is None:  # breyta next í previous    horfa á þetta sem head sem afgreiðslukassa og næsta stak er next
            self.head.previous = new_node
            self.tail.next = new_node
        
        else:
            self.head.previous = new_node
            self.size += 1


    def add_last(self, value):
        new_node = Node(value, next= self.tail.next, previous= self.head)

        if self.head.data is None:  # breyta í if self.head.previous = self.tail
            self.tail.next = new_node
            self.head.previous = new_node

        else:
            self.tail.next = new_node
            self.size += 1
    def current_pointer(self):
        pass

    def get_item(self):
        pass

    def remove_front(self):
        pass

    def remove_last(self):
        pass