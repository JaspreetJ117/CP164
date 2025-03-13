"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-02-27"
-------------------------------------------------------
"""

from List_linked import List

list1 = List()
list2 = List()

# Add some values to list1.
for value in [1, 3, 5, 7]:
    list1.append(value)

# Add some values to list2, some of which overlap with list1.
for value in [2, 4, 5, 6, 7]:
    list2.append(value)

# Create a new list to perform the union.
union_list = List()

# Perform the union operation using the recursive function.
union_list.union_r(list1, list2)

# Display the resulting union list.
print("Union of list1 and list2:")
current = union_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()