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
from Sorts_List_linked import Sorts
from List_linked import List

lst = List()

lst.append(99)
lst.append(10001)
lst.append(3412)
lst.append(44120)
lst.append(11239)
lst.append(23)

Sorts.radix_sort(lst)

for i in lst:
    print(i)
