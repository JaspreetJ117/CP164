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
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
for value in [10, 5, 20, 15, 5, 30]:
    pq.insert(value)

key = 15

higher_than_key, lower_or_equal_to_key = pq.split_key(key)

print("Original Priority Queue (should be empty):")
for value in pq:
    print(value, end=' ')
print()

print("Priority Queue with values higher than key:")
for value in higher_than_key:
    print(value, end=' ')
print()

print("Priority Queue with values lower than or equal to key:")
for value in lower_or_equal_to_key:
    print(value, end=' ')
print()