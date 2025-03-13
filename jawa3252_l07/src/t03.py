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

my_list = List()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)

# Display the original list.
print("Original List:")
current = my_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()

# Split the list using the recursive method.
even_list, odd_list = my_list.split_alt_r()

# Display the even-indexed elements.
print("Even List:")
current = even_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()

# Display the odd-indexed elements.
print("Odd List:")
current = odd_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()