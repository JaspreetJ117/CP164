"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-02-15"
-------------------------------------------------------
"""
from List_linked import List

my_list = List()
my_list.append("red")
my_list.append("green")
my_list.append("blue")

item_at_index_1 = my_list[1]
print("Item at index 1:", item_at_index_1)

my_list[1] = "yellow"
print("New item at index 1:", my_list[1])
