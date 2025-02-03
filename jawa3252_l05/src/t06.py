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
from functions import bag_to_set

old = [4, 5, 3, 4, 5, 2, 2, 4]

new = bag_to_set(old)

print(f"""
Old List: {old}
New List: {new}
""")