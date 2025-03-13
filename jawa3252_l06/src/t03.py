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
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(20)
my_list.append(40)

count_20 = my_list.count(20)
print("The value '20' appears", count_20, "times in the list.")

max_value = my_list.max()
print("The maximum value in the list is:", max_value)

min_value = my_list.min()
print("The minimum value in the list is:", min_value)