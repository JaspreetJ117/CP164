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
my_list.append("yellow")

first_item = my_list.peek()
print("First item (peeked):", first_item)

removed_item = my_list.remove("green")
print("Removed item:", removed_item)