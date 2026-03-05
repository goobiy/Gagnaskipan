

class Node:

    def __init__(self):

        self.data = None
        self.next = None


class LL:

    def __init__(self):

        self.head = None
        self.tail = None


    def push_front(self, value):
        new_node = Node()
        new_node.next = self.head

        self.head = new_node

        new_node.data = value

    def pop_front(self):
    
        pass

    def push_back(self, value):
        new_node = Node()
        new_node.data = value
        print(new_node.data)
        print(self.tail)
        if self.tail is not None:
            old_tail = self.tail
            old_tail.next = new_node

        self.tail = new_node
        new_node.next = None

    def pop_back(self):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        return current_node.data
    
    def all_values(self, node: Node):
        current_node = node
        
        if current_node == self.head:   # check if its the head

            while current_node is not None: # iterates to the last node
                print(current_node.data, end=" ")
                current_node = current_node.next



linked_list = LL()


linked_list.push_front(213213)
linked_list.push_front(4)
linked_list.push_front("Gummsi")
linked_list.push_front([1,2,3])
linked_list.all_values(linked_list.head)
print("-"*64)

linked_list.push_back("gommi")

linked_list.all_values(linked_list.head)