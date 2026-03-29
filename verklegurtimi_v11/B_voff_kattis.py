

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
    n, k = map(int, input().split())
    times = list(map(int, input().split()))

    heap = PQMinList()
    heap.push(times[0])

    for i in range(1, n):
        a = times[i]

        if heap.peek() <= a - k:
            heap.pop()
        heap.push(a)

    print(heap.size())

main()