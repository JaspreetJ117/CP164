"""
-------------------------------------------------------
Lab 2, Stack Abstract Data Type
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-12"
-------------------------------------------------------
"""
# Imports 
from copy import deepcopy

class Stack:
    
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a Python list.
        Use: s = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []
        
    def is_empty(self):
        """
        -------------------------------------------------------
        Checks if the list is empty or not
        Use: s.is_empty()
        -------------------------------------------------------
        Returns:
            A boolean value, True if empty or false if not
        -------------------------------------------------------
        """
        is_empty = False
        
        if self._values == []:
            is_empty = True
            
        return is_empty
    
    def push(self, value):
        """
        -------------------------------------------------------
        Adds an item to the top of the stack
        Use: s.push(value)
        -------------------------------------------------------
        Parameters:
            Value - a data element 
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        
        return None
    
    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = s.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of the stack
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty stack"

        value = self._values[-1]
        self._values.pop()
        
        return value
    
    def peek(self):
        """
        -------------------------------------------------------
        Peek, finds value on the top of the stack. the value is 
        not changed and is only copied and returned to user
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            Value - the value at the top of the stack
        -------------------------------------------------------
        """
        value = deepcopy(self._values[-1])
        
        return value
    
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        
        i = 0
        target1 = Stack()
        target2 = Stack()
        
        while self._values:
            i += 1
            value = self._values.pop()
            
            if i%2 == 0:
                target1._values.append(value)
            
            else:
                target2._values.append(value)
                
        return target1, target2
     
    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        
        self._values.reverse()

        return None
        
        