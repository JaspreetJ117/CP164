"""
-------------------------------------------------------
Lab 2, Test 2 (Arrays to stack)
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-13"
-------------------------------------------------------
"""
#imports
from utilities import array_to_stack
from Stack_array import Stack

items = [[], [], []]
item = []
stacks = [Stack(), Stack(), Stack()]

for i in range(11):
    items[0].append(i)
    items[1].append(i)

items[0] = items[0][::-1] # to make the last entry 10 just because I felt like it

array_to_stack(stacks[0], items[0])
array_to_stack(stacks[1], item)
array_to_stack(stacks[2], items[1])

last_entry_0 = stacks[0].peek()
last_entry_1 = stacks[1].peek() if not stacks[1].is_empty() else None
last_entry_2 = stacks[2].peek()

print(f"Confirmation for updated stack for stack(0) via last entry: {last_entry_0}")
print(f"Confirmation for updated stack for stack(1) via last entry: {last_entry_1}")
print(f"Confirmation for updated stack for stack(2) via last entry: {last_entry_2}")