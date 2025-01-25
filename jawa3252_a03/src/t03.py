"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-22"
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_reverse

source = Stack()
source_list = []

for i in range(10):
    source.push(i+1)
    
stack_reverse(source)

while not source.is_empty():
    value = source.pop()
    source_list.append(value)
    print(value)