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
from utilities import priority_queue_test, pq_to_array, array_to_pq 
from Movie_utilities import read_movie
from copy import deepcopy

movies = []
testing_movies = []
temp_list = []

file = open("movies.txt", "r")
pq = Priority_Queue()

for line in file:
    movies.append(read_movie(line))
testing_movies = deepcopy(movies)

print("Moving items from list to priority queue:")
array_to_pq(pq, testing_movies)
print(f"All items moved to priority queue. List is now empty: {len(testing_movies) == 0}")

print("\nMoving items from priority queue back to list:")
pq_to_array(pq, temp_list)
print(f"All items moved back to list. Priority queue is now empty: {pq.is_empty()}")
print(f"Items in list: {len(temp_list)}")

print()

priority_queue_test(movies)