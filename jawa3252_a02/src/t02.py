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
from Movie_utilities import get_by_rating, read_movies

fv = open("movies.txt", "r")
movies = read_movies(fv)

rated_movies = get_by_rating(movies, 8)

for each in rated_movies:
    print(each)
    print()