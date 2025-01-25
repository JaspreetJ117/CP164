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

source = Stack()

for i in range(10):
    source.push(i+1)

target1, target2 = source.split_alt()

while not target1.is_empty():
    value = target1.pop()
    print(f"Target 1: {value}")

print()

while not target2.is_empty():
    value = target2.pop()
    print(f"Target 2: {value}")
