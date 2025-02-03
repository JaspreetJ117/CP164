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
from Sorted_List_array import Sorted_List
from Movie_utilities import read_movies
from copy import deepcopy

fh = open("movies.txt", "r", encoding="utf-8")

movies = read_movies(fh)
movie_list = Sorted_List()
for movie in movies:
    movie_list.insert(movie)

# Test __getitem__
if len(movie_list) > 0:
    print("Get item:", movie_list[0])

# Test clean
movie_list.clean()
print("List after clean:", [str(movie) for movie in movie_list])

# Test combine
list1 = Sorted_List()
list1.insert(movies[0])
list2 = Sorted_List()
list2.insert(movies[1])
movie_list.combine(list1, list2)
print("List after combine:", [str(movie) for movie in movie_list])

# Test intersection
list1 = deepcopy(movie_list)
list2 = deepcopy(movie_list)
list1.intersection(list1, list2)
print("List after intersection:", [str(movie) for movie in movie_list])

# Test remove_front
if not movie_list.is_empty():
    movie_list.remove_front()
print("List after remove_front:", [str(movie) for movie in movie_list])

# Test remove_many
if len(movie_list) > 0:
    movie_list.remove_many(movie_list[0])
print("List after remove_many:", [str(movie) for movie in movie_list])

# Test split
if len(movie_list) > 0:
    list1, list2 = movie_list.split()
    print("List 1 after split:", [str(movie) for movie in list1])
    print("List 2 after split:", [str(movie) for movie in list2])

# Test split_alt
if len(movie_list) > 0:
    list1, list2 = movie_list.split_alt()
    print("List 1 after split_alt:", [str(movie) for movie in list1])
    print("List 2 after split_alt:", [str(movie) for movie in list2])

# Test union
list1 = Sorted_List()
list2 = Sorted_List()
list1.insert(movies[0])
list2.insert(movies[1])
movie_list.union(list1, list2)
print("List after union:", [str(movie) for movie in movie_list])

# Test __eq__
list1 = Sorted_List()
list1.insert(movies[0])
list2 = Sorted_List()
list2.insert(movies[0])
print("List1 equal List2:", list1 == list2)

# Test __iter__
for movie in movie_list:
    print(movie)
