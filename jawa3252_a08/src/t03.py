"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawnada
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-03-15"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import fill_letter_bst
from functions import letter_table
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()

fill_letter_bst(bst, DATA1)

letter_table(bst)
