"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-03-22"
-------------------------------------------------------
"""
# Imports
from functions import insert_words, comparison_total
from Hash_Set_array import Hash_Set

fv = open('gibbon.txt', 'r')
hash_set = Hash_Set(20)

insert_words(fv, hash_set)
total, max_word = comparison_total(hash_set)

print("Using array-based list Hash_Set")
print()
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(max_word.word, max_word.comparisons))
