"""
-------------------------------------------------------
Lab 10, Task 2
-------------------------------------------------------
Author:  Jaspreet Jawnada
ID:      169083252
Email:   Jawa3252@mylaurier.ca
__updated__ = "2025-03-16"
-------------------------------------------------------
"""
# Imports
from test_Sorts_List_linked import test_sort
from Sorts_List_linked import Sorts

print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)

for name, func in SORTS:
    test_sort(name, func)

"""
test_sort(SORTS[0][0], SORTS[0][1])
test_sort(SORTS[1][0], SORTS[1][1])
test_sort(SORTS[2][0], SORTS[2][1])
test_sort(SORTS[3][0], SORTS[3][1])
test_sort(SORTS[4][0], SORTS[4][1])
"""