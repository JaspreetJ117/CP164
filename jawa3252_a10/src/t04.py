"""
-------------------------------------------------------
Assignment 10, Task 1
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-03-28"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()

a.insert_rear(99)
a.insert_rear(10001)
a.insert_rear(3412)
a.insert_rear(44120)
a.insert_rear(11239)
a.insert_rear(23)

Sorts.gnome_sort(a)

for i in a:
    print(i)
