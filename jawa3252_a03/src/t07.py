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
from functions import reroute

values_in = [1, 2, 3, 4]
opstring = 'SSXSSXXX'

list = reroute(opstring, values_in)

print(f"Before: {values_in}")
print(f"After: {list}")