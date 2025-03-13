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
my_list.append(1)
my_list.append(3)
my_list.append(5)
my_list.append(7)

previous_node, current_node, index = my_list._linear_search(5)

print("Previous Node Value:", previous_node._value if previous_node else None)
print("Current Node Value:", current_node._value if current_node else None)
print("Index of Node with Value 5:", index)