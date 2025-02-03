"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""

from Queue_array import Queue
from utilities import array_to_queue
from copy import deepcopy

q1 = Queue()
q2 = Queue()
source = []
source_copy = []

for i in range(1, 11):
    source.append(i)

source_copy = deepcopy(source)

array_to_queue(q1, source)    
array_to_queue(q2, source_copy)

print("Test 1:")
if q1.__eq__(q2):
    print("queue1 and queue2 are equal.")
else:
    print("queue1 and queue2 are not equal.")
    
q2.remove()
q2.insert(6)

print()
print("Test 2:")
if q1.__eq__(q2):
    print("queue1 and queue2 are equal.")
else:
    print("queue1 and queue2 are not equal.")



