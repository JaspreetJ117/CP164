"""
-------------------------------------------------------
Array version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
from copy import deepcopy


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: target = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._values = []

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """

        # Your code here
        contain = False
        i = 0
        
        while i < len(self._values):
            if self._values[i] == key:
                contain = True
                i = len(self._values)
            else:
                i+=1
                        
        return contain

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of source.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of source (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'

        return deepcopy(self._values[i])

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in source.
        -------------------------------------------------------
        """
        # Your code here
        
        return len(self._values)

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        # Your code here

        return

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(Sorted_List) to len(Sorted_List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        # Your code here
        valid = False
        
        if i >= -len(self._values) and i < len(self._values):
            valid = True
        
        return valid


    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from source.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            source contains one and only one of each value formerly present
            in source. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        i = 0

        while i < len(self._values) - 1:
            if self._values[i] == self._values[i + 1]:
                self._values[i+1].pop()
            else:
                i += 1

        return self._values

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here

        return

    def copy(self):
        """
        ---------------------------------------------------------
        Copies the contents of this list to another sorted list.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a sorted list containing a copy of the contents 
                of source (Sorted_List)
        -------------------------------------------------------
        """
        # Your code here

        return

        
    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in source.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in source (int)
        -------------------------------------------------------
        """
        count = 0

        for value in self._values:
            if value == key:
                count += 1

        return count

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # Your code here
        value = None
        i = 0 
        
        while i<len(self._values):
            if self._values[i] == key:
                value = deepcopy(self._values)
                i = len(self._values)
            else:
                i += 1
        
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        # Your code here
        i = None
        y = 0
        
        while y<len(self._values):
            if self._values[y] == key:
                i = y
                y = len(self._values)
            else:
                y += 1
        
        return i

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in source.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        low = 0
        high = len(self._values)

        while low < high:
            mid = (low + high) // 2

            if self._values[mid] < value:
                low = mid + 1
            else:
                high = mid

        self._values.insert(low, value)

        return

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        self._values = []

        for value in source1._values:
            if value in source2._values and value not in self._values:
                self._values.append(value)

        return None

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Sorted_Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (Sorted_Lists)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # Your code here

        return self._values == target._values

    def max(self):
        """
        -------------------------------------------------------
        Returns the maximum value in source.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'

        # Your code here

        value = deepcopy(self._values[-1])

        return value

    def min(self):
        """
        -------------------------------------------------------
        Returns the minimum value in source.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'

        # Your code here

        value = deepcopy(self._values[0])

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'

        # Your code here
        peek = deepcopy(self._value[0])
        
        return peek

    def pop(self, *args):
        """
        Removes and returns the value from the sorted linked list.
        - If no index is provided, removes the last element.
        - If an index is provided, removes the element at that position.
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"
    
        # If popping the first element
        if len(args) == 0 or args[0] == self._count - 1:
            value = self._rear._value
            if self._front == self._rear:  # Only one element in the list
                self._front = None
                self._rear = None
            else:
                current = self._front
                while current._next is not self._rear:
                    current = current._next
                current._next = None
                self._rear = current
    
        else:  # Popping at a specific index
            i = args[0]
            assert 0 <= i < self._count, "Index out of range"
    
            if i == 0:  # Removing first element
                value = self._front._value
                self._front = self._front._next
                if self._front is None:  # If list becomes empty
                    self._rear = None
            else:  # Removing from the middle
                current = self._front
                previous = None
                for _ in range(i):
                    previous = current
                    current = current._next
                value = current._value
                previous._next = current._next
                if current == self._rear:
                    self._rear = previous
    
        self._count -= 1
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in source
        that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None

        for i, val, in enumerate(self._values):
            if val == key:
                value = self._values.pop(i)

        return value


    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first item in source.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'

        # Your code here

        return self._values.pop(0)

    def remove_many(self, key):
        """
        ---------------------------------------------------------
        Removes all values that match key in source.
        Use: source.remove_many(key)
        ---------------------------------------------------------
        Parameters:
            key - the key to match (?)
        Returns:
            None
        ---------------------------------------------------------
        """
        # Your code here
        self._values = [value for value in self._values if value != key]
        return

    def split(self):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. source becomes empty.
        Use:  target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (Sorted_List)
            target2 - a new List with <= 50% of the original List (Sorted_List)
        -------------------------------------------------------
        """
        midpoint = len(self._values) // 2
        target1 = Sorted_List()
        target2 = Sorted_List()

        for i in self._values[midpoint:]:
            target1.insert(self._values.pop(0))

        for i in self._values[:midpoint]:
            target2.insert(self._values.pop(0))

        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        source is empty after the function executes.
        (iterative version)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List)
            target2 - the odd indexed elements of the list (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()

        target1._values = self._values[::2]
        target2._values = self._values[1::2]
        self._values = []

        return target1, target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        # Your code here

        return

    def split_key(self, key):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains all values < key,
        target2 all values >= key. source becomes empty. source is
        empty at end.
        Use:  target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new Sorted List with values < key (Sorted_List)
            target2 - a new Sorted List with values >= key (Sorted_List)
        -------------------------------------------------------
        """
        # Your code here
        target1 = Sorted_List()
        target2 = Sorted_List()
        
        while len(self._values) > 0:
            if self._values[0] < key:
                target1._values.append(self._values.pop(0))
            else:
                target2._values.append(self._values.pop(0))

        return target1, target2
    
    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values = []
        i = j = 0

        while i < len(source1._values) and j < len(source2._values):
            if source1._values[i] < source2._values[j]:
                if source1._values[i] not in self._values:
                    self._values.append(source1._values[i])
                i += 1

            elif source1._values[i] > source2._values[j]:
                if source2._values[j] not in self._values:
                    self._values.append(source2._values[j])
                j += 1

            else:
                if source1._values[i] not in self._values:
                    self._values.append(source1._values[i])
                i += 1
                j += 1

        while i < len(source1._values):
            if source1._values[i] not in self._values:
                self._values.append(source1._values[i])
            i += 1

        while j < len(source2._values):
            if source2._values[j] not in self._values:
                self._values.append(source2._values[j])
            j += 1

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

