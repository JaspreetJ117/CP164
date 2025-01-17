"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-14"
-------------------------------------------------------
"""

#imports
from Movie_utilities import get_by_genre, read_movies

fv = open("movies.txt", "r")
movies = read_movies(fv)

numbers = 1
lister = get_by_genre(movies, numbers)

for each in lister:
    print(each)
    print()