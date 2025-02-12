"""
-------------------------------------------------------
Array version of the Deque ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
from copy import deepcopy


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: deque = Deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._values = []

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        # Your code here

        return  len(self._values)

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Deques are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a deque (Deque)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        
        equals = True
        i = 0
        
        if len(self._values) == len(target._values):
            while i < len(self._values) and self._values[i] == target._values[i]:
                i += 1
            if i == len(self._values):
                equals = True
        
        return equals

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(deque) to len(deque) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        # Your code here
        
        return -len(self._values) <= i < len(self._values)

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps values of two nodes within a deque. l has taken the place of r, 
        r has taken the place of l.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - an index of a deque value (int)
            r - an index of a deque value (int)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(l) and self._is_valid_index(
            r), "indices to swap must be valid"

        # Your code here

        self._values[l], self._values[r] = deepcopy(self._values[r]), deepcopy(self._values[l])
    
        return None

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        
        value = deepcopy(value)
        
        self._values.insert(0, value)

        return None

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here

        value = deepcopy(value)
        self._values.append(value)
        
        return None

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        # Your code here
        
        is_empty = False
        
        if self._values == []:
            is_empty =  True
        
        return is_empty

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty deque'

        # Your code here
        
        value = deepcopy(self._values[0])

        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty deque'

        # Your code here

        value = deepcopy(self._values[-1])

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty deque'

        # Your code here

        value = deepcopy(self._values.pop(0))
        
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty deque'

        # Your code here

        value = deepcopy(self._values.pop())
        
        return value


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for value in deque:
        -------------------------------------------------------
        Returns:
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

