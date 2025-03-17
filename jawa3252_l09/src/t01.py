"""
-------------------------------------------------------
Lab 9, Task 1
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-03-13"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Movie import Movie

movie1 = Movie("Dellamorte Dellamore", 1994, "Michele Soavi", 7.2, [3,4,5,8])
movie2 = Movie("Dark City",1998,"Alex Proyas",7.8,[0])
movie3 = Movie("Zulu",1964,"Cy Endfield",7.8,[9])


movies = []

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

hash_table(7, movies)
