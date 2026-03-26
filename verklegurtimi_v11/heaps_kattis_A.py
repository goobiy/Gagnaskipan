

class PQMinList:

    def __init__(self):
        self._data = []

    def _parent(self, num: int):
        return (num -1) // 2
    
    def _left_child(self, num: int):
        return 2*num + 1

    def _right_child(self, num: int):
        return 2*num + 2

    def _heapify_up(self, num: int):
        while num > 0:
            p = self._parent(num)
            if self._data[p] > self._data[num]:
                self._data[p], self._data[num] = self._data[num], self._data[p]
                num = p
            else:
                break
    
    def _heapify_down(self, num: int):
        n = len(self._data)

        while True:
            smallest = num
            l, r = self._left_child(num), self._right_child(num)

            if l < n and self._data[l] < self._data[smallest]:
                smallest = l
            if r < n and self._data[r] < self._data[smallest]:
                smallest = r
            if smallest == num:
                break
            self._data[num], self._data[smallest] = self._data[smallest], self._data[num]
            num = smallest

    def push(self, element: int) -> None:
        self._data.append(element)
        self._heapify_up((len(self._data)-1))

    def pop(self) -> int:
        if not self._data:
            raise IndexError("pop from empty PQ")
        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        value = self._data.pop()
        if self._data:
            self._heapify_down(0)
        return value

    def peek(self) -> int:
        if not self._data:
            raise IndexError("peek from empty PQ")
        return self._data[0]

    def size(self) -> int:
        return len(self._data)

    def copy(self) -> "PQMinList":
        mh = PQMinList()
        mh._data = self._data[:]  # shallow copy is sufficient as we are only working with
        return mh                 # non-mutable data (int).
    


def main():
    q = int(input())
    instances: dict[int, PQMinList] = {}

    for _ in range(q):
        parts = input().split()
        iid  = int(parts[0])
        op   = parts[1]

        if iid not in instances:
            instances[iid] = PQMinList()

        heap = instances[iid]

        if op == 'a':
            src_id = int(parts[2])
            if src_id not in instances: # fix á kattis
                instances[src_id] = PQMinList()
            instances[iid] = instances[src_id].copy()
        elif op == '+':                     # push
            heap.push(int(parts[2]))
        elif op == '-':                     # pop
            heap.pop()
        elif op == 'p':                     # peek
            print(heap.peek())
        elif op == 's':                     # size
            print(heap.size())

main()