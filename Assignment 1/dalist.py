import collections
from fixarray import FixedSizeArray
from collections.abc import Iterable



class DAList:
    """
    -Dynamic array (mimicking most of Python's list behavior).
    """

    ##############################################################################################################
    # Part 1 section
    ##############################################################################################################

    def __init__(self, capacity: int = 4) -> None:
        """
        Constructor
        Time complexity: O(1)
        :param capacity:
        """
        self.data = FixedSizeArray(capacity)
        self.capacity = self.data.capacity()

    def __len__(self) -> int:
        """
        Returns the number of elements in the array ( ... = len(A))
        Time Complexity: O(n)
        :return: number of elements
        """

        counter = 0
        for i in self.data:
            if i is None:
                continue
            counter += 1
        return counter

    def __getitem__(self, index: int) -> object:
        """
        Accessing an element at given index (... = A[index]).
        Time complexity: O(n)
        :param index
        :return Element at index (exception if index is out of range)
        """

        if index < 0:
            index = len(self) + index

        if index >= len(self):
            raise IndexError("Index out of range")
        elif index < 0:
            raise IndexError("Index out of range")
        elif self.data[index] is None:
            raise IndexError("Nothing there cuh")
        return self.data[index]
    
    def __setitem__(self, index: int ,value: object) -> None:
        """
        Updating an element at given index (A[index] = value).
        Time complexity: O(n)
        :param index:
        """

        if index < 0:
            index = len(self) + index

        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        
        self.data[index] = value

    def double_the_array(self) -> None:
        '''
        Doubles the capacity of the array
        time complexity: O(n)
        '''

        new_array = FixedSizeArray(self.capacity * 2)
        for i in range(len(self)):
            new_array[i] = self.data[i]

        self.data = new_array
        self.capacity = self.data.capacity()

    def __str__(self) -> str:
        """
        Returns a string representation of the array, e.g, [1, 2, 3] (str(A))
        Time complexity: O(n^2)
        :return: string representation
        """

        return "[" + ", ".join(str(x) for x in self) + "]"

    def __delitem__(self, index: int) -> None:
        """
        Delete an element at given index (del A[index]).
        Time complexity: O(n)
        :param index
        """

        if index < 0:
            index = len(self) + index
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")


        for i in range(index, len(self) - 1):
            self.data[i] = self.data[i + 1]
        self.data[len(self) - 1] = None

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: O(1)
        :return self
        """

        self.__index = 0
        return self

    def __next__(self) -> object:
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: O(n)
        :return the element at index self.__index (exception if out of range)
        """

        if self.__index >= len(self):
            raise StopIteration
        elem = self.data[self.__index]
        self.__index += 1
        return elem

    def clear(self) -> None:
        """
        Clears the array. Ensure you clear the references to the cleared object (such that the garbage collector
        can reclaim them).
        Time complexity: O(n)
        """

        for i in range(len(self)):
            self.data[i] = None


    def count(self, value: object) -> int:
        """
        Counts the number of times an element 'value' appears in the list.
        Time complexity: O(n)
        :return: number of times value appears
        """

        counter = 0
        for i in self.data:
            if i == value:
                counter += 1
        return counter


    def index(self, value: object) -> int:
        """
        Returns the index of the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n)
        :param value: The value to look for
        :return:  index of first occurrence in list
        """

        for i in range(len(self)):
            if self.data[i] == value:
                return i
        raise ValueError(f"{value} is not in list")


    def insert(self, index: int, value: object) -> None:
        """
        Inserts the element 'value' at position index in the array (shifting the subsequent items).
        Time complexity: O(n)
        :param index: position where to append the element.
        :param value: element to append
        """

        if index < 0:
            index = len(self) + index
            if index < 0:
                index = 0

        if index > len(self):
            raise IndexError("Index out of range")


        if len(self) == self.capacity:
            self.double_the_array()

        for i in range(len(self), index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value

    def reverse(self):
        """
        Reverses the array 'in place', e.g. [1, 2, 3] becomes [3, 2, 1].
        Time complexity: O(n)
        """

        n = len(self)
        for i in range(n // 2):
            j = (n - 1 - i)
            self.data[i], self.data[j] = self.data[j], self.data[i]

        return self
    
    ##############################################################################################################
    # Part 2 section
    ##############################################################################################################

    def append(self, value: object) -> None:
        """
        Appends the element 'value' to the end of the array. Doubles the capacity of the array
        if it is already full before inserting an element.
        Time complexity: O(n)
        :param value: element to append
        """

        if len(self) == self.capacity:
            self.double_the_array()
        self.data[len(self)] = value

    def copy(self):
        """
        Returns a shallow copy of the array.
        Time complexity: O(n^2)
        :return: copy of array
        """

        copied_list = DAList(self.capacity)

        for i in range(len(self)):
            
            copied_list.append(self.data[i])
            
        return copied_list

    def extend(self, iterable: collections.abc.Iterable) -> None:
        """
        Extends the array with the elements from iterable.
        Time complexity: O(n^2)
        :param iterable: An iterable object (e.g., a list)
        """

        for i in iterable:
            self.append(i)

    def pop(self, index: int) -> object:
        """
        Remove the element at a given index from the array
        Time complexity: O(n)
        :param index: position of element to remove
        """

        if index < 0:
            index = len(self) + index
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        
        value = self.data[index]
        self.__delitem__(index)
        return value


    def remove(self, value: object) -> None:
        """
        Removes the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n)
        :param value: The value to remove
        """

        for i in range(self.__len__()):
            if self.data[i] == value:
                self.__delitem__(i)
                return
            
        raise ValueError(f"{value} is not in list")