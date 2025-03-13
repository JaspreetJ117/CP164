"""
-------------------------------------------------------
Lab 8, Task 4
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-03-07"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_code_bst, DATA1

bst = BST()

# Fill the BST with Morse code data
fill_code_bst(bst, DATA1)

# Print the BST
print("BST Contents in Inorder:")
for each in bst.inorder():
    print(each)
