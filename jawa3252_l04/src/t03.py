"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-28"
-------------------------------------------------------
"""
from List_array import List

my_list = List()

print("Appending elements to the list...")
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(f"List after appends: {[value for value in my_list]}") 

print("\nInserting an element at index 1...")
my_list.insert(1, 15)
print(f"List after insert: {[value for value in my_list]}") 

print("\nRemoving the element '20'...")
removed_value = my_list.remove(20)
print(f"Removed value: {removed_value}") 
print(f"List after removal: {[value for value in my_list]}")  

print("\nAttempting to remove a non-existent element '40'...")
result = my_list.remove(40)
print(f"Result of removal: {result}") 
print(f"List after failed removal attempt: {[value for value in my_list]}") 