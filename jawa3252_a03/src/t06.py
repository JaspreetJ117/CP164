"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-22"
-------------------------------------------------------
"""
from functions import postfix

test_expressions = [
    "12 5 -",                
    "4 5 + 12 * 2 3 * -",    
    "7 2 + 3 /"              
]

for expr in test_expressions:
    result = postfix(expr)
    print(f"'{expr}' evaluates to {result}")