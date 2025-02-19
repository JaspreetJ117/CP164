"""
-------------------------------------------------------
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
from copy import deepcopy


class _PQ_Node:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the next node in the priority queue
        Use: node = _PQ_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _next - another priority queue node (_PQ_Node)
        Returns:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = _next


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """

        # Your code here
        is_empty = False
        
        if self._rear is None:
            is_empty = True

        return is_empty

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """

        # Your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is inserted into the priority queue.
        Values are stored in priority order. 
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        # Your code here
        
        node = _PQ_Node(value,None)
        current = self._front
        previous = current
        
        if self._front is None or value < self._front._value:
            node._next = self._front
            self._front = node
            
            if self._rear is None:
                self._rear = node
            
            self._count += 1
            
        elif value > self._rear._value:
            self._rear._next = node
            self._rear = node
            self._count += 1
            
        else:
            while current is not None and value > current._value:            
                previous = current
                current = current._next
                
                
            node._next = current
            previous._next = node
            self._count += 1

        return None

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"


        # Your code here
        
        value = deepcopy(self._front._value)
        next = self._front._next
    
        self._front = None
        self._front = next
        self._count -= 1
        
        if self._front is None:
            self._rear = None

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"


        # Your code here

        return deepcopy(self._front._value)

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """

        target1 = Priority_Queue()
        target2 = Priority_Queue()
        current = self._front
        count = 0

        while current:
            next_node = current._next 
            current._next = None  

            if not count % 2:
                if target1._rear:
                    target1._rear._next = current
                else:
                    target1._front = current
                target1._rear = current
                target1._count += 1

            else:
         
                if target2._rear:
                    target2._rear._next = current
                else:
                    target2._front = current
                target2._rear = current
                target2._count += 1

            current = next_node 
            count += 1


        self._front = None
        self._rear = None
        self._count = 0

        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = pq1.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """

        target1 = Priority_Queue()
        target2 = Priority_Queue()

        current = self._front

        while current:
            next_node = current._next 
            current._next = None  

            if current._value < key:
                if target1._rear:
                    target1._rear._next = current
                else:
                    target1._front = current
                target1._rear = current
                target1._count += 1

            else:
         
                if target2._rear:
                    target2._rear._next = current
                else:
                    target2._front = current
                target2._rear = current
                target2._count += 1

            current = next_node 


        self._front = None
        self._rear = None
        self._count = 0

        return target1, target2

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue. 
        When finished, the contents of source1 and source2 are inserted 
        into target and source1 and source2 are empty. Order is preserved
        with source1 elements having priority over source2 elements with the
        same priority value.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked priority queue (Priority_Queue)
            source2 - a linked priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """

        self._front = None
        self._rear = None
        self._count = 0

        curr1 = source1._front
        curr2 = source2._front

        last = None

        while curr1 is not None and curr2 is not None:
            if curr1._value < curr2._value:
                next_node = curr1
                curr1 = curr1._next
            else:
                next_node = curr2
                curr2 = curr2._next

            if last is None:
                self._front = next_node
            else:
                last._next = next_node

            last = next_node
            self._count += 1

        remaining = curr1 if curr1 is not None else curr2

        while remaining is not None:
            next_node = remaining
            remaining = remaining._next

            if last is None:
                self._front = next_node

            else:
                last._next = next_node

            last = next_node
            self._count += 1

        self._rear = last

        source1._front = None
        source1._rear = None
        source1._count = 0
        source2._front = None
        source2._rear = None
        source2._count = 0

        return


    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty priority queue"

        if self._front is None:
            self._front = source._front
            self._rear = source._rear

        else:
            self._rear._next = source._front
            self._rear = source._rear

        self._count += source._count

        source._front = None
        source._rear = None
        source._count = 0

        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Order is preserved.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty priority queue"


        # Your code here
        node = source._front
        
        if source._front._next is None:
            source._front = source._rear = None

        else:
            node = source._front
            source_next = source._front._next
            source._front = None
            source._front = source_next

        if self._front is None:
            self._front = self._rear = node
                
        else:
            self._rear._next = node
            self._rear = node
        
        node._next = None
        self._rear = node
        source._count -= 1
        self._count += 1

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next