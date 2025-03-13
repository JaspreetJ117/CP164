"""
-------------------------------------------------------
Lab 8, Task 6
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-03-07"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_code_bst, decode_morse, DATA1

bst = BST()

# Step 2: Fill the BST with Morse code data sorted by Morse code
fill_code_bst(bst, DATA1)

# Step 3: Decode a Morse code string into English text
morse_code = "... --- ..."
decoded_text = decode_morse(bst, morse_code)
print(f"Morse Code: {morse_code}")
print(f"Decoded Text: {decoded_text}")
