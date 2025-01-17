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
from Movie import Movie
from Movie_utilities import genre_counts, read_movies

fv = open("movies.txt", "r")
movie = read_movies(fv)
    
count = genre_counts(movie)

for i in range(len(Movie.GENRES)):
    print(f"{Movie.GENRES[i]} Has: {count[i]}")