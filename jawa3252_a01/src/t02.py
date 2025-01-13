"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-10"
-------------------------------------------------------
"""

from functions import list_subtraction

values = [22, 33, 11, 1, 2, 3, 44, 55, 66, 4, 5, 6]

print(f"List before: {values}")
list_subtraction(values, [11, 22, 33, 44, 55, 66])

print(f"List after: {values}")