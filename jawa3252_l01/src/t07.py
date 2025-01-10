"""
-------------------------------------------------------
Testing read_movie which takes in a "|" seperated 
in movie.txt and its parameters and creates and object
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-10"
-------------------------------------------------------
"""
from Movie_utilities import read_movies

fv = open("movies.txt", "r")
movie = read_movies(fv)

for each in movie:
    print(each)
    print()

