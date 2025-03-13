"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
Author: Jaspreet Jawanda
ID:     169083252
Email:   jawa3252@mylaurier.ca
__updated__ = '2025-03-1'
-------------------------------------------------------
"""

from Priority_Queue_linked import Priority_Queue

pq1 = Priority_Queue()
pq2 = Priority_Queue()

for value in [5, 3, 9, 1, 4]:
    pq1.insert(value)

for value in [8, 2, 6, 7, 0]:
    pq2.insert(value)

print("Removed value from pq1:", pq1.remove())

print("Peeked value in pq1:", pq1.peek())

print("Is pq1 empty?", pq1.is_empty())

print("Length of pq1:", len(pq1))

target1, target2 = pq2.split_alt()
print("Values in target1 after split_alt:", list(target1))
print("Values in target2 after split_alt:", list(target2))

for value in [8, 2, 6, 7, 0]:
    pq2.insert(value)

key = 5
target3, target4 = pq2.split_key(key)
print("Values in target3 after split_key with key = 5:", list(target3))
print("Values in target4 after split_key with key = 5:", list(target4))

combined_pq = Priority_Queue()
combined_pq.combine(pq1, target4)
print("Values in combined_pq after combining pq1 and target4:", list(combined_pq))

print("Iterating through combined_pq:")
for value in combined_pq:
    print(value)
