"""
-------------------------------------------------------
Lab 3, Testing 3 (Stack to Array)
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-13"
-------------------------------------------------------
"""

#imports
from Stack_array import Stack
from utilities import stack_to_array

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

target = []

stack_to_array(stack, target)

print("Is the stack empty after transferring to array?", stack.is_empty())  # Should be True

print("Elements in the target array:", target)