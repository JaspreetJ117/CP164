"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-03-05"
-------------------------------------------------------
"""

#imports 
from List_linked import List
from Movie_utilities import read_movies

from copy import deepcopy

def print_linked(linked_list):
    temp_linked = deepcopy(linked_list)
    temp_list = []
    for i in range(linked_list._count):
        temp_list.append(temp_linked.pop())
        
    temp_list = temp_list[::-1]
    
    for movie in temp_list:
        print(movie)
    
    temp_linked = None
    temp_list = None


#create movie list and List ADT
fv = open("movies.txt", "r")
movies = read_movies(fv)
movies_linked = List()
movies_combine_test = List()
movies_empty = List()
movies_empty_clean = List()

# append
for movie in movies:
    movies_linked.append(movie)
    
print()
    
# clean
movies_linked.clean()
print_linked(movies_linked) # should remove the first three

print() 

#combine
for movie in movies:
    movies_combine_test.append(movie)

movies_combine_test.clean()
 
movies_empty.combine(movies_linked, movies_combine_test)
print_linked(movies_empty)
print()

#intersection
for movie in movies:
    movies_linked.append(movie)
for movie in movies:
    movies_combine_test.append(movie)
movies_empty_clean.intersection(movies_linked,movies_combine_test)
print_linked(movies_empty_clean)
print()

#prepend
movies_empty_clean.prepend(movies[-1])
print_linked(movies_empty_clean)
print()

#remove_front
movies_empty_clean.remove_front()
print_linked(movies_empty_clean)
print()

#remove_many
movies_empty.remove_many(movies[-1])
print_linked(movies_empty)
print()

#split
movies_linked, movies_combine_test = movies_empty_clean.split()
print_linked(movies_linked)
print_linked(movies_combine_test)
print()

#split_alt
list1 = List()
list2 = List()
list1, list2 = movies_empty.split_alt()
print_linked(list1)
print_linked(list2)
print()

#Unions
list1.union(list2, movies_linked)
print_linked(list1)