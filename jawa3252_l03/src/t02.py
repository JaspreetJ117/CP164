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

from Queue_array import Queue

q = Queue()

elements = [1, 2, 3]

print("Inserting elements into the queue:")
for element in elements:
    q.insert(element)
    
print(f"Queue now contains: {[val for val in q]}")

if not q.is_empty():
    front_element = q.peek()
    print(f"\nPeeking at the front element: {front_element}")

print("\nRemoving elements from the queue:")
while not q.is_empty():
    removed_element = q.remove()
    print(f"Removed {removed_element} from the queue.")
    if not q.is_empty():
        next_element = q.peek()
        print(f"Next element to be removed: {next_element}")
    else:
        print("The queue is now empty.")
    print(f"Queue now contains: {[val for val in q]}")