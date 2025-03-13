"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-09-04"
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to None since it must be added to the rear
        of the queue.
        Use: node = _Queue_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = None


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        is_empty = False
        
        if self._front is None:
            is_empty = True
        
        return is_empty 

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        is_empty = False
        
        if self._rear is None:
            is_empty = True
        
        return is_empty

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        new_node = _Queue_Node(value)
        
        if self._front is None:
            self._front = self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
        self._count += 1
        
        return None

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        # your code here
        next_value = self._front._next
        current = deepcopy(self._front._value)
        self._front = None
        self._front = next_value
        
        if bool(self._count - 1) is False:
            self._rear = None
        
        self._count -= 1
        
        return current

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        # your code here
        return deepcopy(self._front._value)

    def _move_front_to_rear(self, source):
        """
        Moves the front node from the source queue to the rear of the target queue.
        """
        assert source._front is not None, "Cannot move the front of an empty queue"
    
        front_source = source._front
        front_next = source._front._next  
    
        source._front = front_next
        if source._front is None:  
            source._rear = None
        
        source._count -= 1
    
        front_source._next = None
    
        if self._rear is None:  
            self._front = self._rear = front_source
        else:
            self._rear._next = front_source
            self._rear = front_source
    
        self._count += 1
        
        return None


    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - a linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        if self._front is not None:
            self._rear._next = source._front
            self._rear = source._rear
            self._count += source._count
        else:
            self._front = source._front
            self._rear = source._rear
            self._count += source._count

        source._front = source._rear = None
        source._count = 0
        
        return None


    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked queue (Queue)
            source2 - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = self._rear = None
        self._count = 0
    
       
        current1 = source1._front
        current2 = source2._front
        count = 0
    
        while current1 or current2:
            if (count % 2 == 0 and current1) or not current2:  # Take from source1 if possible
                node = current1
                current1 = current1._next
            else:  
                node = current2
                current2 = current2._next
    
            if self._rear is None:  
                self._front = self._rear = node
            else:
                self._rear._next = node
                self._rear = node
    
            self._count += 1
            count += 1
    
        if self._rear:
            self._rear._next = None
    
        source1._front = source1._rear = None
        source1._count = 0
    
        source2._front = source2._rear = None
        source2._count = 0
        
        return None

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        # your code here
        target1 = Queue()
        target2 = Queue()
        current = self._front
        count = 0
        
        while current:
            if bool(count % 2) is False: 
                if target1._front is None:
                    target1._front = target1._rear = current
                    target1._count += 1
                else:
                    target1._rear._next = current
                    target1._rear = current
                    target1._count += 1
            else:
                if target2._front is None:
                    target2._front = target2._rear = current
                    target2._count += 1
                else:
                    target2._rear._next = current
                    target2._rear = current
                    target2._count += 1
                    
            count += 1
            current = current._next
            
        if target1._rear:
            target1._rear._next = None
        if target2._rear:
            target2._rear._next = None
            
        self._front = self._rear = None
        self._count = 0
                
        return target1, target2

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        equals = False
        
        if self._count is target._count:
            
            equals = True
            current_self = self._front
            currnet_target = target._front
            
            if bool(self._count) is True:
                while equals and current_self._next and currnet_target._next:
                    
                    if current_self._value is not currnet_target._value:
                        equals = False
                        
                    else:
                        current_self = current_self._next
                        currnet_target = currnet_target._next
        
        return equals

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
