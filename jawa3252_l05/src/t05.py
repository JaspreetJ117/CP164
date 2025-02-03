"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-02-02"
-------------------------------------------------------
"""

from functions import is_palindrome

test_strings = ["A man, a plan, a canal: Panama", "racecar", "hello", "No 'x' in Nixon"]

for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' is a palindrome: {result}")