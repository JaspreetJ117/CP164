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
from Queue_circular import Queue
from utilities import array_to_queue
from functions import queue_combine

q1 = Queue()
q2 = Queue()
target = Queue()
source1 = []
source2 = []

for i in range(1, 11):
    if i < 5:
        source1.append(i)
    else:
        source2.append(i)
        
        
array_to_queue(q1, source1)    
array_to_queue(q2, source2)

target = queue_combine(q1, q2)

print(target.peek())