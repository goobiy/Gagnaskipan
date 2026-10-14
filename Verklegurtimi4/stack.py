
class Stack:

    def __init__(self) -> None:

        self.stack: list = []
        self.size = 0


    def push(self, item: object):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Stack is empty")
        self.stack.pop()
        self.size -= 1


    def top(self) -> object:
        return self.stack[self.size -1]

    def is_empty(self) -> bool:
        
        return self.size == 0
    
    def __str__(self):
        return f"{self.stack}"
    
    def matching_par(self,text: str):
        stack = Stack()
        for c in text:
            if c == '(':
                stack.push(c)
            elif c == ')':
                if stack.is_empty():
                    return False
                stack.pop()
        return stack.is_empty()


def reverse_string(s: str) -> str:
    stack = Stack()
    s = s.strip()
    for let in s[::-1]:
        stack.push(let)
    
    return stack

print(reverse_string("hello"))




# a.push(2)
# a.push(3)
# a.push(4)

# print(a)

# a.pop()

# print(a)

# print(a)

# print(a.top())

# print(a.size)

# print(a.is_empty())

# print(a.matching_par("hello"))