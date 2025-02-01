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

from Queue_circular import Queue 

q = Queue()

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("Inserting elements into the queue:")
for element in elements:
    print(f"Inserting {element} into the queue.")
    q.insert(element)
    print(f"Queue now contains: {[val for val in q]}")
