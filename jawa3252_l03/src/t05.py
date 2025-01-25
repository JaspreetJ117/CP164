"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-20"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

pq.insert(30)
pq.insert(10)
pq.insert(20)

while not pq.is_empty():
    highest_priority_value = pq.remove()
    print("Removed:", highest_priority_value)

print()
    
q = Priority_Queue()

q.insert("Mango")
q.insert("Apple")
q.insert("Banana")

while not q.is_empty():
    highest_priority_value1 = q.remove()
    print("Removed:", highest_priority_value1)