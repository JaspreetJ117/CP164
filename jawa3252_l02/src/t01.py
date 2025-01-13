"""
-------------------------------------------------------
Lab 2, testing 1 (Stack creation)
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-13"
-------------------------------------------------------
"""

#imports
from Stack_array import Stack

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
source = Stack()

print("Initializing the empty stack")

if source.is_empty():
    print("Source Stack is empty")
    
else: 
    print("Source stack is not empty")

for element in items:
    source.push(element)

if source.is_empty():
    print("Source Stack is empty")
    
else: 
    print("Source stack is not empty")

print(f"Current last item in the source stack: {source.peek()}")
source.push(items[-1]+1)
print(f"Current last item in the source stack: {source.peek()}")
source.pop()
print(f"Current last item in the source stack: {source.peek()}")
