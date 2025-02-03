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
from List_array import List
from Movie_utilities import read_movies
from copy import deepcopy
from Movie import Movie

fh = open("movies.txt", "r", encoding="utf-8")

movies = read_movies(fh)
movie_list = List()
for movie in movies:
    movie_list.append(movie)

# Test __getitem__
if len(movie_list) > 0:
    print("Get item:", movie_list[0])

# Test clean
movie_list.clean()
print("List after clean:", [str(movie) for movie in movie_list])

# Test combine
list1 = List()
list1.append(movies[0])
list2 = List()
list2.append(movies[1])
movie_list.combine(list1, list2)
print("List after combine:", [str(movie) for movie in movie_list])

# Test intersection
list1 = deepcopy(movie_list)
list2 = deepcopy(movie_list)
list1.intersection(list1, list2)
print("List after intersection:", [str(movie) for movie in movie_list])

# Test prepend
movie_list.prepend(Movie("CP104", 2024, "Dr Shera", 9.9, [1, 2, 3, 4]))
print("List after prepend:", [str(movie) for movie in movie_list])

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
list1 = List()
list2 = List()
list1.append(movies[0])
list2.append(movies[1])
movie_list.union(list1, list2)
print("List after union:", [str(movie) for movie in movie_list])

# Test __eq__
list1 = List()
list1.append(movies[0])
list2 = List()
list2.append(movies[0])
print("List1 equal List2:", list1 == list2)

# Test __iter__
for movie in movie_list:
    print(movie)
